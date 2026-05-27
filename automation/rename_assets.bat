@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
:: ====================================================================
:: SLOTSFREEUSA AUTOMATED ASSET BATCH RENAMER (WINDOWS)
:: Place this file inside the folder containing raw .mp4 and .mp3 files.
:: Double-click to rename unsorted assets safely.
:: ====================================================================

:: Get current local date in YYYY-MM-DD format using PowerShell.
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set "mydate=%%i"

set /a video_counter=1
set /a audio_counter=1

echo [+] Initializing SlotsFreeUSA asset organization sequence...
echo [+] Date stamp: %mydate%
echo.

:: Rename .mp4 video files that do not already start with slotsfreeusa_
for %%f in (*.mp4) do (
    set "filename=%%f"
    if /I not "!filename:~0,13!"=="slotsfreeusa_" (
        set "newname=slotsfreeusa_video_ID!video_counter!_%mydate%.mp4"
        call :safeRename "%%f" "!newname!"
        set /a video_counter+=1
    )
)

:: Rename .mp3 voiceover files that do not already start with slotsfreeusa_
for %%a in (*.mp3) do (
    set "audioname=%%a"
    if /I not "!audioname:~0,13!"=="slotsfreeusa_" (
        set "newaudio=slotsfreeusa_audio_ID!audio_counter!_%mydate%.mp3"
        call :safeRename "%%a" "!newaudio!"
        set /a audio_counter+=1
    )
)

echo.
echo [+] Asset processing complete. Ready for programmatic distribution.
pause
exit /b

:safeRename
set "oldfile=%~1"
set "newfile=%~2"

if exist "%newfile%" (
    set /a duplicate_counter=1
    :duplicateLoop
    set "candidate=%~n2_dup!duplicate_counter!%~x2"
    if exist "!candidate!" (
        set /a duplicate_counter+=1
        goto duplicateLoop
    )
    echo [RENAME] "%oldfile%" ----^> "!candidate!"
    ren "%oldfile%" "!candidate!"
) else (
    echo [RENAME] "%oldfile%" ----^> "%newfile%"
    ren "%oldfile%" "%newfile%"
)
exit /b
