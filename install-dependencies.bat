@echo off
setlocal

set install_dir=%cd%

set sevenz_URL="https://www.7-zip.org/a/7za920.zip"
set ytdl_URL="https://yt-dl.org/downloads/2021.03.14/youtube-dl.exe"
set ffmpeg_URL="https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z"

rem Download and Extract 7-Zip
bitsadmin /transfer 7zip /download /priority FOREGROUND %sevenz_URL% "%install_dir%\7z.zip"
mkdir %install_dir%\7z\
Call :UnZipFile "%install_dir%\7z\" "%install_dir%\7z.zip"
del %install_dir%\7z.zip

rem Download Youtube-dl
bitsadmin /transfer youtubedl /download /priority FOREGROUND %ytdl_URL% "%install_dir%\youtube-dl.exe"

rem Download and extract FFMPEG
bitsadmin /transfer ffmpeg /download /priority FOREGROUND %ffmpeg_URL% "%install_dir%\ffmpeg.7z"
%install_dir%\7z\7za.exe e "%install_dir%\ffmpeg.7z" -o%install_dir%\ *.exe -r
del %install_dir%\ffmpeg.7z
cls
pip install mutagen numpy
cls

echo ************************************************
echo **************FINISHED INSTALLING***************
echo ************************************************
pause 

:UnZipFile <ExtractTo> <newzipfile>
set vbs="%temp%\_.vbs"
if exist %vbs% del /f /q %vbs%
>%vbs%  echo Set fso = CreateObject("Scripting.FileSystemObject")
>>%vbs% echo If NOT fso.FolderExists(%1) Then
>>%vbs% echo fso.CreateFolder(%1)
>>%vbs% echo End If
>>%vbs% echo set objShell = CreateObject("Shell.Application")
>>%vbs% echo set FilesInZip=objShell.NameSpace(%2).items
>>%vbs% echo objShell.NameSpace(%1).CopyHere(FilesInZip)
>>%vbs% echo Set fso = Nothing
>>%vbs% echo Set objShell = Nothing
cscript //nologo %vbs%
if exist %vbs% del /f /q %vbs%