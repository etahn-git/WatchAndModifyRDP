# WatchAndModifyRDP
## What it does:
This program waits/scans for a new .rdp fie to be downloaded on your computer, when it finds a .rdp file downloaded it will configure the rdp file to use all of your monitors, then start the RDP connection and after the connection opens it will delete the file so .rdp files dont build up in your download folder after awhile.
<br><br>

## Purpose / What its made for:
WatchAndModifyRDP is made for single sign-on(SSO) gateways, that give you a shorterm .rdp file to use that opens a remote dekstop connection to another computer(eg. a work pc). However when you download the .rdp files they are not setup to use all your monitors by default, but WatchAndModifyRDP automically changes it to use all monitors the second it is installed.<br><br>
<b>If you dont wanna use this program these are the steps to change it manually:</b>
- Download the .rdp file from your gateway
- Open the .rdp file with a text editor
- Find the line that says 
```use multimon:i:0``` and change the 0 to a 1 so you have ```use multimon:i:1```
- Save the file and launch the .rdp file again.

Download the latest release/installer here: https://github.com/etahn-git/WatchAndModifyRDP/releases/tag/v1.0 or in the source code there is a exe file, you can just download it and run that exe, you shouldnt need python installed to use it.

<hr>
<b>Todo:</b><br>
- Make the system tray icon change color from white to black on light theme<br>
- Option to change the downloads folder that its scanning.<br>
- Amount of monitors to use<br>
- Toggle deleting files.<br>
- Autostart<br>
<br>
