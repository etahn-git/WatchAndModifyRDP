# WatchAndModifyRDP

This python program waits/scanning for a new .rdp fie downloaded on your computer, onece its downloaded it will config the rdp file to use all monitors, then start the RDP file and after start it will be deleted.

This was made for Citrix Gateway remote sessions, basically you add your computer to it then you can click on it and it will give you a temporary rdp file to connect to it, if you dont connect within 15 minutes the rdp file expires, but when you download it, it doesnt have all monitors enabled so this is why I created this script to automatically change that when its downloaded. It can be used for other programs this is just the reason why I made it.
