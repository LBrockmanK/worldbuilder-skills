<#
.SYNOPSIS
    Updates all markdown links in an Obsidian vault when a note is renamed.

.DESCRIPTION
    When a note is renamed using external tools (Edit/Write), Obsidian's
    auto-rename is bypassed. This script updates all markdown link references
    across the vault to point to the new name and path.

    Handles both body-text links [Name](notes/name.md) and frontmatter links
    inside YAML strings. Derives filenames by lowercasing and replacing spaces
    with hyphens.

    This script only updates link text in other vault files.
    It does NOT rename the file itself — that is a separate operation.

.PARAMETER OldName
    The old note display name without file extension.

.PARAMETER NewName
    The new note display name without file extension.

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

$VaultPath = Resolve-Path $VaultPath -ErrorAction Stop | Select-Object -ExpandProperty Path

$oldFilename = "$OldName.md"
$newFilename = "$NewName.md"
$newPath     = "notes/$newFilename"

Write-Host "Vault:    $VaultPath"
Write-Host "Rename:   [$OldName](...) -> [$NewName]($newPath)"
Write-Host ""

$allFiles = Get-ChildItem -Path $VaultPath -Filter "*.md" -Recurse -ErrorAction Stop
$scanned  = $allFiles.Count
$updated  = 0
$changed  = @()

$escapedOld     = [regex]::Escape($OldName)
$escapedOldFile = [regex]::Escape($oldFilename)

# Match markdown links with the old display name: [OldName](any/path.md)
# Negative lookbehind for ! prevents matching image embeds ![Name](path)
$pattern     = "(?<!!)\[$escapedOld\]\([^)]*\)"
$replacement = "[$NewName]($newPath)"

# Also match links found by path alone (display text may differ):
# [anything](notes/old-name.md) or [...](path/old-name.md)
$pathPattern     = "(?<!!)\[([^\]]*)\]\(([^)]*/)?$escapedOldFile\)"
$pathReplacement = "[`$1]($newPath)"

foreach ($file in $allFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8

    if ($null -eq $content) { continue }

    $newContent = [regex]::Replace($content, $pattern, $replacement)
    $newContent = [regex]::Replace($newContent, $pathPattern, $pathReplacement)

    if ($newContent -ne $content) {
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
        $updated++
        $changed += $file.FullName
    }
}

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
    Write-Host "No files contained links to [$OldName]."
}
