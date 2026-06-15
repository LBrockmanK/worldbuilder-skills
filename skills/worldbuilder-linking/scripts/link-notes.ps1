<#
.SYNOPSIS
    Deterministic linker: finds unlinked note references and wraps them in
    markdown links.

.DESCRIPTION
    Builds an inventory of all notes (names + aliases), then scans target
    files for plain-text mentions that should be linked. Links the first
    unlinked occurrence per H2 section. Longer entity names are matched
    first to prevent partial matches.

    Operates on body text only — frontmatter is not modified.

    Two modes:
      -TargetFile: link outward from a single file (references TO other notes)
      -Reverse:    also scan other files for references TO the target file

    Use -DryRun to preview changes without writing.

.PARAMETER TargetFile
    Path to the file to link (relative to vault or absolute).

.PARAMETER All
    Process all .md files in the vault.

.PARAMETER Reverse
    After linking the target file, also scan other files for unlinked
    references to the target file's name and aliases.

.PARAMETER VaultPath
    Path to the vault root. Defaults to the current directory.

.PARAMETER DryRun
    Show what would change without writing files.

.EXAMPLE
    .\link-notes.ps1 -TargetFile "notes\Mira Vale.md"
    .\link-notes.ps1 -TargetFile "notes\Mira Vale.md" -Reverse
    .\link-notes.ps1 -All -DryRun
#>

param(
    [string]$TargetFile = "",
    [switch]$All,
    [switch]$Reverse,
    [string]$VaultPath = ".",
    [switch]$DryRun
)

$VaultPath = Resolve-Path $VaultPath -ErrorAction Stop | Select-Object -ExpandProperty Path

if (-not $TargetFile -and -not $All) {
    Write-Error "Specify -TargetFile or -All."
    exit 1
}

# --- Build note inventory ---

function Parse-Aliases([string]$Content) {
    $aliases = @()
    if ($Content -notmatch "(?s)^---\r?\n(.+?)\r?\n---") { return $aliases }
    $yaml = $Matches[1]
    foreach ($line in $yaml -split "\r?\n") {
        if ($line -match "^aliases:\s*\[(.+)\]") {
            $items = $Matches[1] -split ',\s*' | ForEach-Object {
                $item = $_.Trim()
                if ($item -match '^"(.*)"$' -or $item -match "^'(.*)'$") { $Matches[1] }
                else { $item }
            }
            # Strip markdown link syntax from aliases
            $aliases = $items | ForEach-Object {
                if ($_ -match '^\[([^\]]+)\]\([^)]*\)$') { $Matches[1] } else { $_ }
            }
        }
    }
    return $aliases
}

$allFiles = Get-ChildItem -Path $VaultPath -Filter "*.md" -Recurse -ErrorAction Stop |
    Where-Object { $_.FullName -notlike "*\_templates\*" }

# Build inventory: each entry = { name, aliases, path, searchTerms }
$inventory = @()
foreach ($file in $allFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    if ($null -eq $content) { continue }
    if ($content -notmatch "(?s)^---\r?\n(.+?)\r?\n---") { continue }
    $yaml = $Matches[1]
    if ($yaml -notmatch "type:\s*\w") { continue }

    $name    = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
    $aliases = Parse-Aliases $content

    # Compute vault-relative path with forward slashes
    $relPath = $file.FullName.Substring($VaultPath.Length).TrimStart('\', '/') -replace '\\', '/'

    # All searchable terms: name + aliases, deduplicated
    $terms = @($name) + $aliases | Select-Object -Unique | Where-Object { $_.Length -gt 0 }

    $inventory += [PSCustomObject]@{
        Name       = $name
        Aliases    = $aliases
        Path       = $relPath
        Terms      = $terms
        FileName   = $file.Name
        FullPath   = $file.FullName
    }
}

# Sort terms longest-first across the full inventory to prevent partial matches
$termMap = @()
foreach ($entry in $inventory) {
    foreach ($term in $entry.Terms) {
        $termMap += [PSCustomObject]@{
            Term     = $term
            Name     = $entry.Name
            Path     = $entry.Path
            FullPath = $entry.FullPath
        }
    }
}
$termMap = $termMap | Sort-Object { $_.Term.Length } -Descending

# --- Linking engine ---

function Get-BodyRange([string]$Content) {
    # Returns the start index of body text (after frontmatter)
    if ($Content -match "(?s)^---\r?\n.+?\r?\n---\r?\n?") {
        return $Matches[0].Length
    }
    return 0
}

function Split-Sections([string]$Body) {
    # Split body into sections by H2 headers. Returns array of { Start, Length, Text }
    $sections = @()
    $pattern  = "(?m)^## "
    $matches  = [regex]::Matches($Body, $pattern)

    if ($matches.Count -eq 0) {
        $sections += [PSCustomObject]@{ Start = 0; Text = $Body }
        return $sections
    }

    # Content before first H2
    if ($matches[0].Index -gt 0) {
        $sections += [PSCustomObject]@{
            Start = 0
            Text  = $Body.Substring(0, $matches[0].Index)
        }
    }

    for ($i = 0; $i -lt $matches.Count; $i++) {
        $start = $matches[$i].Index
        $end   = if ($i + 1 -lt $matches.Count) { $matches[$i + 1].Index } else { $Body.Length }
        $sections += [PSCustomObject]@{
            Start = $start
            Text  = $Body.Substring($start, $end - $start)
        }
    }
    return $sections
}

function Is-InsideLink([string]$Text, [int]$Position, [int]$Length) {
    # Check if position falls inside an existing markdown link [...](...) or code block
    $before = $Text.Substring(0, $Position)

    # Inside inline code
    $backtickCount = ($before.ToCharArray() | Where-Object { $_ -eq '``' }).Count
    if ($backtickCount % 2 -ne 0) { return $true }

    # Inside a markdown link's display text: look for [ before us without a closing ] before us
    # Pattern: we're between [ and ]( — meaning we're inside a link's display text
    $lastOpen  = $before.LastIndexOf('[')
    $lastClose = $before.LastIndexOf(']')
    if ($lastOpen -gt $lastClose) {
        # We're inside [...] — check if it's a link (followed by parenthesized URL)
        $afterMatch = $Text.Substring($Position + $Length)
        # Find the closing ] after our position
        $closingBracket = $Text.IndexOf(']', $Position)
        if ($closingBracket -ge 0 -and $closingBracket -lt $Text.Length - 1) {
            if ($Text[$closingBracket + 1] -eq '(') { return $true }
        }
        return $true  # Inside brackets regardless — don't link
    }

    # Inside a markdown link's URL: look for ]( before us without a closing ) before us
    $lastLinkOpen = $before.LastIndexOf('](')
    if ($lastLinkOpen -ge 0) {
        $lastParen = $before.LastIndexOf(')')
        if ($lastParen -lt $lastLinkOpen) { return $true }
    }

    return $false
}

function Link-Section([string]$SectionText, [string]$SourceFullPath, [array]$TermMap) {
    $result  = $SectionText
    $linked  = @{}  # Track which note paths we've already linked in this section
    $offset  = 0    # Track cumulative offset from replacements

    foreach ($entry in $TermMap) {
        # Don't link a note to itself
        if ($entry.FullPath -eq $SourceFullPath) { continue }

        # Skip if we already linked to this note in this section
        if ($linked[$entry.Path]) { continue }

        $escapedTerm = [regex]::Escape($entry.Term)
        # Word-boundary match, case-sensitive
        $match = [regex]::Match($result, "(?<=\b)$escapedTerm(?=\b)")

        if (-not $match.Success) { continue }

        # Check if this occurrence is inside an existing link or code
        if (Is-InsideLink $result $match.Index $match.Length) {
            # Try to find another occurrence outside links
            $searchFrom = $match.Index + $match.Length
            $found = $false
            while ($searchFrom -lt $result.Length) {
                $nextMatch = [regex]::Match($result.Substring($searchFrom), "(?<=\b)$escapedTerm(?=\b)")
                if (-not $nextMatch.Success) { break }
                $absIndex = $searchFrom + $nextMatch.Index
                if (-not (Is-InsideLink $result $absIndex $nextMatch.Length)) {
                    $match = $nextMatch
                    # Adjust match index to absolute
                    $match = [PSCustomObject]@{ Index = $absIndex; Length = $nextMatch.Length; Value = $nextMatch.Value }
                    $found = $true
                    break
                }
                $searchFrom = $absIndex + $nextMatch.Length
            }
            if (-not $found) { continue }
        }

        $linkText    = "[$($match.Value)]($($entry.Path))"
        $beforeMatch = $result.Substring(0, $match.Index)
        $afterMatch  = $result.Substring($match.Index + $match.Length)
        $result      = $beforeMatch + $linkText + $afterMatch

        $linked[$entry.Path] = $true
    }

    return $result
}

function Process-File([string]$FilePath, [array]$TermMap) {
    $content  = Get-Content -Path $FilePath -Raw -Encoding UTF8
    if ($null -eq $content) { return $null }

    $bodyStart = Get-BodyRange $content
    if ($bodyStart -ge $content.Length) { return $null }

    $frontmatter = $content.Substring(0, $bodyStart)
    $body        = $content.Substring($bodyStart)

    $sections    = Split-Sections $body
    $newBody     = ""
    $lastEnd     = 0

    foreach ($section in $sections) {
        # Preserve any gap between sections
        if ($section.Start -gt $lastEnd) {
            $newBody += $body.Substring($lastEnd, $section.Start - $lastEnd)
        }
        $newBody += Link-Section $section.Text $FilePath $TermMap
        $lastEnd = $section.Start + $section.Text.Length
    }

    # Preserve any trailing content
    if ($lastEnd -lt $body.Length) {
        $newBody += $body.Substring($lastEnd)
    }

    $newContent = $frontmatter + $newBody

    if ($newContent -ne $content) {
        return $newContent
    }
    return $null
}

# --- Execute ---

$filesToProcess = @()
if ($All) {
    $filesToProcess = $allFiles | ForEach-Object { $_.FullName }
} else {
    $resolved = if ([System.IO.Path]::IsPathRooted($TargetFile)) {
        $TargetFile
    } else {
        Join-Path $VaultPath $TargetFile
    }
    if (-not (Test-Path $resolved)) {
        Write-Error "File not found: $resolved"
        exit 1
    }
    $filesToProcess = @($resolved)

    if ($Reverse) {
        # Also process all other files for back-links to the target
        $targetName = [System.IO.Path]::GetFileNameWithoutExtension((Split-Path $resolved -Leaf))
        $targetEntry = $inventory | Where-Object { $_.Name -eq $targetName }

        if ($targetEntry) {
            # Build a term map containing ONLY the target's terms
            $reverseTermMap = @()
            foreach ($term in $targetEntry.Terms) {
                $reverseTermMap += [PSCustomObject]@{
                    Term     = $term
                    Name     = $targetEntry.Name
                    Path     = $targetEntry.Path
                    FullPath = $targetEntry.FullPath
                }
            }
            $reverseTermMap = $reverseTermMap | Sort-Object { $_.Term.Length } -Descending

            foreach ($file in $allFiles) {
                if ($file.FullName -eq $resolved) { continue }
                $newContent = Process-File $file.FullName $reverseTermMap
                if ($null -ne $newContent) {
                    if ($DryRun) {
                        Write-Host "[back-link] Would update: $($file.FullName)"
                    } else {
                        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
                        Write-Host "[back-link] Updated: $($file.FullName)"
                    }
                }
            }
        }
    }
}

$updated = 0
foreach ($filePath in $filesToProcess) {
    $newContent = Process-File $filePath $termMap
    if ($null -ne $newContent) {
        if ($DryRun) {
            Write-Host "[forward]   Would update: $filePath"
        } else {
            Set-Content -Path $filePath -Value $newContent -Encoding UTF8 -NoNewline
            Write-Host "[forward]   Updated: $filePath"
        }
        $updated++
    }
}

Write-Host ""
Write-Host "Files processed: $($filesToProcess.Count)"
Write-Host "Files $( if ($DryRun) {'that would be'} else {'actually'} ) updated: $updated"
