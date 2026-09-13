param(
    [string]$Target = "dau-ra",
    [ValidateSet("lint", "strict")]
    [string]$Mode = "lint"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $Target)) {
    Write-Error "Không tìm thấy đầu ra: $Target"
    exit 1
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Error "Không tìm thấy Python để chạy validator."
    exit 1
}

& $python.Source "scripts/validate_package.py" $Target --mode $Mode
exit $LASTEXITCODE
