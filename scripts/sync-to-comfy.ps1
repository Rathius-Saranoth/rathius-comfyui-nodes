param(
    [string]$Dest = "C:\Projects\ComfyUI\custom_nodes"
)

# Activate venv if present
if (Test-Path -Path ".\.venv\Scripts\Activate.ps1") {
    & .\.venv\Scripts\Activate.ps1
}

Write-Host "Syncing package to $Dest"
python .\tools\sync_to_comfy.py --dest $Dest

# Attempt to restart ComfyUI if running (look for python processes running main.py)
try {
    $comfyRoot = "C:\Projects\ComfyUI"
    $procs = Get-CimInstance Win32_Process | Where-Object {
        $_.CommandLine -and (
            ($_.CommandLine -match "main.py") -or
            ($_.ExecutablePath -like "*\\python.exe" -and $_.CommandLine -like "*$comfyRoot*")
        )
    }
    if ($procs) {
        Write-Host "Found ComfyUI process(es). Restarting..."
        foreach ($p in $procs) {
            Write-Host "Stopping PID $($p.ProcessId)"
            Stop-Process -Id $p.ProcessId -Force -ErrorAction SilentlyContinue
        }

        # Start ComfyUI using the venv python if available
        $venvpy = Join-Path -Path $comfyRoot -ChildPath ".venv\Scripts\python.exe"
        if (Test-Path $venvpy) {
            Write-Host "Starting ComfyUI with venv python: $venvpy"
            Start-Process -FilePath $venvpy -ArgumentList "main.py" -WorkingDirectory $comfyRoot
        } else {
            Write-Host "Starting ComfyUI with system python"
            Start-Process -FilePath "python" -ArgumentList "main.py" -WorkingDirectory $comfyRoot
        }
        Write-Host "ComfyUI restarted."
    } else {
        Write-Host "No running ComfyUI process found. Copy complete."
    }
} catch {
    Write-Host "Warning: could not automatically restart ComfyUI: $_"
}
