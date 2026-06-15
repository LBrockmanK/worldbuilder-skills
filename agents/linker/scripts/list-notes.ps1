<#
.SYNOPSIS
    Lists all notes in a vault with their frontmatter metadata.

.DESCRIPTION
    Reads all .md files in notes/ (and optionally root-level project docs),
    parses YAML frontmatter, and outputs a structured inventory of note name,
    type, status, aliases, and brief.

    Output format is one JSON object per line (JSONL) for easy script consumption.
    Use -Pretty for a human-readable table.

.PARAMETER VaultPath
    Path to the vault root. Defaults to the current directory.

.PARAMETER Type
    Filter to a specific note type (character, location, faction, event, concept, story).

.PARAMETER IncludeProject
    Also include root-level project docs (seed.md, worldbuilding-plan.md, etc.).

.PARAMETER Pretty
    Output as a formatted table instead of JSONL.

.EXAMPLE
    .\list-notes.ps1
    .\list-notes.ps1 -Type character -Pretty
    .\list-notes.ps1 -VaultPath "C:\Projects\MyVault" -IncludeProject
#>

param(
    [string]$VaultPath = ".",
    [string]$Type = "",
    [switch]$IncludeProject,
    [switch]$Pretty
)

$VaultPath = Resolve-Path $VaultPath -ErrorAction Stop | Select-Object -ExpandProperty Path
$notesDir  = Join-Path $VaultPath "notes"

function Parse-Frontmatter([string]$Content) {
    $result = @{}
    if ($Content -notmatch "(?s)^---\r?\n(.+?)\r?\n---") { return $result }

    $yaml = $Matches[1]
    foreach ($line in $yaml -split "\r?\n") {
        if ($line -match "^(\w[\w-]*):\s*(.*)$") {
            $key   = $Matches[1]
            $value = $Matches[2].Trim()

            # Strip quotes
            if ($value -match '^"(.*)"$' -or $value -match "^'(.*)'$") {
                $value = $Matches[1]
            }

            # Parse YAML lists: ["item1", "item2"]
            if ($value -match '^\[(.+)\]$') {
                $items = $Matches[1] -split ',\s*' | ForEach-Object {
                    $item = $_.Trim()
                    if ($item -match '^"(.*)"$' -or $item -match "^'(.*)'$") {
                        $Matches[1]
                    } else { $item }
                }
                $value = $items
            }

            # Handle multi-line brief (pipe literal)
            if ($value -eq "|") {
                $inBrief = $true
                $briefLines = @()
                continue
            }

            $result[$key] = $value
        }
        elseif ($inBrief) {
            if ($line -match "^\s+(.+)$") {
                $briefLines += $Matches[1]
            } else {
                $result["brief"] = ($briefLines -join " ").Trim()
                $inBrief = $false
                # Re-process this line
                if ($line -match "^(\w[\w-]*):\s*(.*)$") {
                    $result[$Matches[1]] = $Matches[2].Trim()
                }
            }
        }
    }
    if ($inBrief -and $briefLines.Count -gt 0) {
        $result["brief"] = ($briefLines -join " ").Trim()
    }
    return $result
}

function Extract-LinkName([string]$LinkText) {
    # Extract display name from markdown link [Name](path) or return as-is
    if ($LinkText -match '^\[([^\]]+)\]\([^)]*\)$') {
        return $Matches[1]
    }
    return $LinkText
}

# Collect files
$files = @()
if (Test-Path $notesDir) {
    $files += Get-ChildItem -Path $notesDir -Filter "*.md" -ErrorAction SilentlyContinue
}
if ($IncludeProject) {
    $files += Get-ChildItem -Path $VaultPath -Filter "*.md" -Depth 0 -ErrorAction SilentlyContinue
}

$notes = @()
foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    if ($null -eq $content) { continue }

    $fm = Parse-Frontmatter $content

    if (-not $fm["type"]) { continue }
    if ($Type -and $fm["type"] -ne $Type) { continue }

    $name = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)

    # Extract plain alias names from markdown links
    $aliases = @()
    if ($fm["aliases"] -is [array]) {
        $aliases = $fm["aliases"] | ForEach-Object { Extract-LinkName $_ }
    } elseif ($fm["aliases"] -and $fm["aliases"] -ne "[]") {
        $aliases = @(Extract-LinkName $fm["aliases"])
    }

    $brief = if ($fm["brief"]) { $fm["brief"] } else { "" }

    $note = [ordered]@{
        name    = $name
        type    = $fm["type"]
        status  = if ($fm["status"]) { $fm["status"] } else { "unknown" }
        aliases = $aliases
        brief   = $brief
        path    = "notes/$($file.Name)"
    }

    # Add path relative to vault for root-level files
    if ($file.Directory.FullName -eq $VaultPath) {
        $note["path"] = $file.Name
    }

    $notes += $note
}

# Output
if ($Pretty) {
    $notes | ForEach-Object {
        $aliasStr = if ($_["aliases"].Count -gt 0) { ($_["aliases"] -join ", ") } else { "-" }
        $briefStr = if ($_["brief"].Length -gt 80) { $_["brief"].Substring(0, 77) + "..." } else { $_["brief"] }
        if (-not $briefStr) { $briefStr = "-" }
        [PSCustomObject]@{
            Name    = $_["name"]
            Type    = $_["type"]
            Status  = $_["status"]
            Aliases = $aliasStr
            Brief   = $briefStr
        }
    } | Format-Table -AutoSize -Wrap
} else {
    foreach ($note in $notes) {
        # Manual JSON construction for PS 5.1 compatibility
        $aliasJson = ($note["aliases"] | ForEach-Object { '"' + ($_ -replace '"', '\"') + '"' }) -join ","
        $briefJson = ($note["brief"] -replace '\\', '\\\\' -replace '"', '\"' -replace "`r`n", '\n' -replace "`n", '\n')
        $nameJson  = $note["name"] -replace '"', '\"'
        $pathJson  = $note["path"] -replace '\\', '/' -replace '"', '\"'
        Write-Output "{""name"":""$nameJson"",""type"":""$($note["type"])"",""status"":""$($note["status"])"",""aliases"":[$aliasJson],""brief"":""$briefJson"",""path"":""$pathJson""}"
    }
}
