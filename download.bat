@echo off
echo downloading songs\%1 %2

if exist songs\%1\ (
  :choice
  set /P c=Are you sure you want to continue[Y/N]?
  if /I "%c%" EQU "Y" goto :start
  goto :end
) else (
  echo "Creating a folder %1"
  mkdir songs\%1
)

:start
@echo off
cd songs\%1
..\..\youtube-dl --extract-audio --audio-format mp3 -i "%2"
cd ..\..


:END