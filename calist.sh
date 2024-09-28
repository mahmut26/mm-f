#!/bin/sh
xset -dpms
xset s off
xset s noblank
matchbox-window-manager&
midori -e Fullscreen -a http://localhost:8080/ &
python3 ./reboot.py
