@echo off
set USERPROFILE=C:\Users\Admin\AgyWriting
set GEMINI_HOME=C:\Users\Admin\.gemini-writing
set ANTIGRAVITY_HOME=C:\Users\Admin\.gemini-writing

if not exist "%LOCALAPPDATA%\Programs\antigravity\Antigravity.exe" goto try_ide
echo Launching isolated Antigravity IDE...
start "" "%LOCALAPPDATA%\Programs\antigravity\Antigravity.exe" --user-data-dir "C:\Users\Admin\AgyWriting\.antigravity-ide" "%~dp0"
goto end

:try_ide
if not exist "%LOCALAPPDATA%\Programs\Antigravity IDE\Antigravity IDE.exe" goto try_legacy
echo Launching isolated Antigravity IDE (alternative path 1)...
start "" "%LOCALAPPDATA%\Programs\Antigravity IDE\Antigravity IDE.exe" --user-data-dir "C:\Users\Admin\AgyWriting\.antigravity-ide" "%~dp0"
goto end

:try_legacy
if not exist "%LOCALAPPDATA%\Programs\Antigravity\Antigravity IDE.exe" goto not_found
echo Launching isolated Antigravity IDE (alternative path 2)...
start "" "%LOCALAPPDATA%\Programs\Antigravity\Antigravity IDE.exe" --user-data-dir "C:\Users\Admin\AgyWriting\.antigravity-ide" "%~dp0"
goto end

:not_found
echo [ERROR] Antigravity IDE executable not found in AppData Local Programs.
echo Please launch it manually.
pause

:end
exit
