<#
.SYNOPSIS
    Updates all wikilinks in an Obsidian vault when a note is renamed.

.DESCRIPTION
    When a note is renamed using external tools (Edit/Write), Obsidian's
    auto-rename is bypassed. This script updates all wikilink references across
    the vault to point to the new name.

    This script only updates link text in other vault files.
    It does NOT rename the file itself — that is a separate operation.

.PARAMETER OldName
    The old note name without file extension.

.PARAMETER NewName
    The new note name without file extension.

.PARAMETER VaultPath
    Path to the vault root. Defaults to the current directory if not provided.

.EXAMPLE
    .\rename-note.ps1 -OldName "Aldric the Blacksmith" -NewName "Aldric"
    .\rename-note.ps1 -OldName "Old Mill" -NewName "Harrow Mill" -VaultPath "C:\Projects\MyVault"
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$OldName,

    [Parameter(Mandatory = $true)]
    [string]$NewName,

    [Parameter(Mandatory = $false)]
    [string]$VaultPath = "."
)

# Resolve vault path to absolute
$VaultPath = Resolve-Path $VaultPath -ErrorAction Stop | Select-Object -ExpandProperty Path

Write-Host "Vault:    $VaultPath"
Write-Host "Rename:   [[$OldName]] -> [[$NewName]]"
Write-Host ""

# Collect all .md files in the vault
$allFiles = Get-ChildItem -Path $VaultPath -Filter "*.md" -Recurse -ErrorAction Stop
$scanned  = $allFiles.Count
$updated  = 0
$changed  = @()

# Escape special regex characters in the note name so names like
# "Aldric (Blacksmith)" or "Note+Title" match literally.
$escapedOld = [regex]::Escape($OldName)

# Build the replacement pattern.
# Wikilink structure: [[ <path> <anchor>? <alias>? ]]
#   !? — optional embed prefix
#   \[\[ — opening brackets
#   (<escapedOld>) — the note name (captured group 1, replaced)
#   ([#^][^\|\]]*)? — optional anchor (#Heading or #^blockid), captured group 2
#   (\|[^\]]*)?     — optional alias (|display text), captured group 3
#   \]\] — closing brackets
#
# Group 1 is replaced with $NewName; groups 2 and 3 are preserved verbatim.
$pattern     = "(!?\[\[)($escapedOld)([#^][^\|\]]*)?(\|[^\]]*)?(\]\])"
$replacement = "`${1}$NewName`${3}`${4}`${5}"

foreach ($file in $allFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8

    # Skip empty files
    if ($null -eq $content) { continue }

    $newContent = [regex]::Replace($content, $pattern, $replacement)

    if ($newContent -ne $content) {
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
        $updated++
        $changed += $file.FullName
    }
}

# Report
Write-Host "Results"
Write-Host "-------"
Write-Host "Files scanned: $scanned"
Write-Host "Files updated: $updated"

if ($changed.Count -gt 0) {
    Write-Host ""
    Write-Host "Changed files:"
    foreach ($f in $changed) {
        Write-Host "  $f"
    }
} else {
    Write-Host ""
    Write-Host "No files contained links to [[$OldName]]."
}
