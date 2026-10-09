# Suspicious Link Inspector

Inspect links for common warning signs without opening them.

A standalone, offline desktop utility for Python 3.9+ using built-in Tkinter. No external packages, API keys, telemetry, or network requests.

## Run

1. Install Python 3.9+ with Tkinter support.
2. Download or clone this repository.
3. In its folder run: `python app.py` (Windows: `py app.py`).
4. Run tests with: `python -m unittest discover -s tests -v`.

**Note:** This is source code, not a precompiled Windows executable. Run it on a machine with a graphical desktop and Python/Tkinter installed.

## Limitations

Inspects text only. Does not visit links, check reputation, follow redirects, or guarantee safety. URLs can contain secrets; avoid sharing them.

## Privacy

All checks are performed locally. No telemetry, network calls, or background monitoring.

## License
MIT — see LICENSE.


## Windows .exe (no Python required for end users)

**Build on GitHub:** Push the contents of this project directory to a GitHub repository (make sure `.github/workflows/windows-exe.yml` is at repository root). Open **Actions → Build Windows EXE → Run workflow**. Once it finishes, download `Suspicious-Link-Inspector-Windows` under **Artifacts** and extract `Suspicious-Link-Inspector.exe`. GitHub Actions can also run when changes are pushed to `main` or `master`.

**Build locally on Windows:** Install Python 3.12, then double-click `build-windows.bat`. The finished file will be in `dist\Suspicious-Link-Inspector.exe`. The builder requires an internet connection to install PyInstaller; the compiled app doesn't need Python installed.

**Build status:** This package contains Windows build instructions and automation, *not* a precompiled EXE. The GUI hasn't been tested in Windows in this environment. Windows and antivirus warnings can occur for unsigned executables.
