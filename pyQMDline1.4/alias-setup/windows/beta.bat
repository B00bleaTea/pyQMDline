@ECHO OFF

echo [ WARNING ]
echo ____________________________________
echo be aware that this file might break windows
echo i'm not a windows user, i don't know if this file works or not
echo !!!!!!
echo THIS FILE WILL EDIT YOUR REGISTRY !
echo please make sure to back your registry up !
echo if you don't feel like trusting this file (i wouldn't)
echo please follow the tutorial in the template.txt
echo please do your research.
echo here's some information:
echo HOW TO BACK UP AND RESTORE YOUR REGISTRY:
echo https://support.microsoft.com/en-us/topic/how-to-back-up-and-restore-the-registry-in-windows-855140ad-e318-2a13-2829-d428a2ab0692#:~:text=Back%20up%20the%20registry%20manually,-From%20the%20Start&text=In%20Registry%20Editor%2C%20locate%20and,Click%20Save.
echo HOW TO BACK UP YOUR WINDOWS INSTALLATION:
echo https://support.microsoft.com/en-us/windows/back-up-and-restore-your-pc-ac359b36-7015-4694-de9a-c5eac1ce9d9c
echo !!! BE AWARE OF THESE RISKS, BACK UP IMPORTANT FILES, REGISTRY AND MAYBE EVEN YOUR WINDOWS INSTALLATION !!!
echo !!!!!!

PAUSE
PAUSE
PAUSE

goto check_Permissions
:check_Permissions
    net session >nul 2>&1
    if %errorLevel% == 0 (
        set /p pyqmdLOC="enter the location of the pyQMDline (exs. c:\users\john\pyQMDline1.4): "
        echo the file will be saved in %userprofile%\init.cmd, that script will autorun everytime you start CMD.
        echo the alias set is pyQMD - if something breaks edit the %userprofile%\init.cmd file.
        echo this file will edit your registry, please back your registry up before running this file.
        set /p confirm="press enter to confirm or CTRL + C/the x button to exit"

        echo sleeping, please exit within 10 seconds if this was an accident
        SLEEP 10

        echo DOSKEY pyQMD=cd %pyqmdLOC% && py %pyqmdLOC%\__main__.py >> %userprofile%\init.cmd
        echo clr >> %userprofile%\init.cmd
        SLEEP 2

        reg add "HKCU\Software\Microsoft\Command Processor" /v AutoRun ^
        /t REG_EXPAND_SZ /d "%"USERPROFILE"%\init.cmd" /f

        echo if you're seeing this this probably means everything went okay,
        echo please reboot your machine for changes to take.
    ) else (
        echo please run this file as administrator.
    )
    PAUSE
