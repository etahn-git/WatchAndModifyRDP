# WatchAndModifyRDP
## What it does:
This program waits/scans for a new .rdp file to be downloaded on your computer, when it finds a .rdp file downloaded it will configure the rdp file to use all of your monitors, then start the RDP connection and after the connection opens it will delete the file so .rdp files dont build up in your download folder after awhile.
<br>

## Purpose / What its made for:
WatchAndModifyRDP is made for single sign-on(SSO) gateways, that give you a short term .rdp file to use that opens a remote desktop connection to another computer(eg. a work pc). However when you download the .rdp files they are not setup to use all your monitors by default, but WatchAndModifyRDP automically changes it to use all monitors the second it is installed.<br><br>
<b>If you dont wanna use this program these are the steps to change it manually:</b>
- Download the .rdp file from your gateway
- Open the .rdp file with a text editor
- Find the line that says 
```use multimon:i:0``` and change the 0 to a 1 so you have ```use multimon:i:1```
- Save the file and launch the .rdp file again.

## How to install
- Dowload the latest installer [here](https://github.com/etahn-git/WatchAndModifyRDP/releases/download/v1.0/WatchAndModifyRDP.Installer.exe) (Chrome and Windows Defender may flag it as suspicious because of the way the python code is compiled into an exe, heres the [VirusTotal results](https://www.virustotal.com/gui/url/c47b5e6a2b039db4055c38553bacfb2d61b41b340366168226245685e4b20b74/detection))
- Finish installing it and then it should be running in your system tray if it is, your good to go if its not in your system tray just search for it in your start menu.
