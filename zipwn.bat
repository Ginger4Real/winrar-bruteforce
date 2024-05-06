@echo off
title Zipwn
color A
if not exist "C:\Program Files\7-Zip" (
	echo 7-Zip not installed!
	pause
	exit
)

echo.
set /p archive="Enter Archive: "
if not exist "%archive%" (
	echo Archive not found!
	pause
	exit
)

set /p wordlist="Enter Wordlist: "
if not exist "%wordlist%" (
	echo Wordlist not found!
	pause
	exit
)

echo Cracking...
set attempt=1
for /f %%a in (%wordlist%) do (
	set pass=%%a
	call :attempt
)
echo shitty wordlist dumbass
pause
exit

:attempt
"C:\Program Files\7-Zip\7z.exe" x -p%pass% "%archive%" -o"cracked" -y >nul 2>&1
echo Attempt %attempt%: %pass%
set /a attempt+=1
if /I %errorlevel% EQU 0 (
	echo Success! Password Found: %pass%
	pause
	exit
)
