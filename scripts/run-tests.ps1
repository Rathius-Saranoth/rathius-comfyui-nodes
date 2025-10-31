param(
    [string]$VenvActivate = ".\.venv\Scripts\Activate.ps1"
)

if (Test-Path -Path $VenvActivate) {
    & $VenvActivate
}

Write-Host "Running pytest..."
pytest -q
