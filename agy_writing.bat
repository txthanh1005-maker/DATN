@echo off
set USERPROFILE=C:\Users\Admin\AgyWriting
set GEMINI_HOME=C:\Users\Admin\.gemini-writing
set ANTIGRAVITY_HOME=C:\Users\Admin\.gemini-writing

:: Clear IDE integration variables to force standalone CLI mode
set ANTIGRAVITY_LS_ADDRESS=
set ANTIGRAVITY_CSRF_TOKEN=
set ANTIGRAVITY_TRAJECTORY_ID=
set ANTIGRAVITY_AGENT=

echo [Isolated CLI Session] using profile: C:\Users\Admin\AgyWriting
echo Launching agy CLI in standalone mode...
agy.exe %*
