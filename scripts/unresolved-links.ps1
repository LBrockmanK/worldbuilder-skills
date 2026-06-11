<#
.SYNOPSIS
    Reports all markdown links pointing to non-existent files.

.DESCRIPTION
    Scans all .md files in the vault for markdown links [text](path) and
    checks whether the target file exists. Reports broken/phantom links
    grouped by target (to show which missing notes are most referenced)
    or by source.

.PARAMETER VaultPath
    Path to the vault root. Defaults to the current directory.

.PARAMETER GroupBy
    How to group output: "target" (default) groups by the missing file,
    "source" groups by the file containing the link.

.EXAMPLE
    .\unresolved-links.ps1
    .\unresolved-links.ps1 -GroupBy source
    .\unresolved-links.ps1 -VaultPath "C:\Projects\MyVault"
#>

param(
    [string]$VaultPath = ".",
    [ValidateSet("target", "source")]
    [string]$GroupBy = "target"
)

$VaultPath = Resolve-Path $VaultPath -ErrorAction Stop | Select-Object -ExpandProperty Path

$allFiles = Get-ChildItem -Path $VaultPath -Filter "*.md" -Recurse -ErrorAction Stop

# Pattern: [display text](path) but not ![image](path)
$linkPattern = "(?<!!)\[([^\]]+)\]\(([^)]+)\)"

$unresolvedLinks = @()

foreach ($file in $allFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    if ($null -eq $content) { continue }

    $matches = [regex]::Matches($content, $linkPattern)
    foreach ($m in $matches) {
        $displayText = $m.Groups[1].Value
        $linkPath    = $m.Groups[2].Value

        # Skip external URLs
        if ($linkPath -match "^https?://" -or $linkPath -match "^mailto:") { continue }

        # Skip anchor-only links
        if ($linkPath -match "^#") { continue }

        # Strip any anchor from the path
        $cleanPath = ($linkPath -split '#')[0]
        if (-not $cleanPath) { continue }

        # Resolve relative to vault root
        $targetFull = Join-Path $VaultPath $cleanPath

        if (-not (Test-Path $targetFull)) {
            $sourceRel = $file.FullName.Substring($VaultPath.Length).TrimStart('\', '/') -replace '\\', '/'
            $unresolvedLinks += [PSCustomObject]@{
                Source      = $sourceRel
                Target      = $cleanPath
                DisplayText = $displayText
            }
        }
    }
}

if ($unresolvedLinks.Count -eq 0) {
    Write-Host "No unresolved links found."
    exit 0
}

Write-Host "Unresolved links: $($unresolvedLinks.Count)"
Write-Host ""

if ($GroupBy -eq "target") {
    $grouped = $unresolvedLinks | Group-Object -Property Target | Sort-Object Count -Descending
    foreach ($group in $grouped) {
        $refCount = $group.Count
        Write-Host "$($group.Name)  ($refCount reference$(if ($refCount -gt 1) {'s'}))"
        foreach ($link in $group.Group) {
            Write-Host "    <- $($link.Source)  [$($link.DisplayText)]"
        }
        Write-Host ""
    }
} else {
    $grouped = $unresolvedLinks | Group-Object -Property Source | Sort-Object Name
    foreach ($group in $grouped) {
        Write-Host "$($group.Name)"
        foreach ($link in $group.Group) {
            Write-Host "    -> $($link.Target)  [$($link.DisplayText)]"
        }
        Write-Host ""
    }
}

Write-Host "---"
Write-Host "Total unresolved: $($unresolvedLinks.Count)"
$uniqueTargets = ($unresolvedLinks | Select-Object -Property Target -Unique).Count
Write-Host "Unique missing targets: $uniqueTargets"
