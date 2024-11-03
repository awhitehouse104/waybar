#!/bin/bash

entries="\uf023\tLock\n\uf2f5\tLogout\n\uf2f1\tReboot\n\uf011\tShutdown"

selected=$(echo -e $entries | wofi --dmenu --cache-file /dev/null | awk '{print tolower($2)}')

case $selected in
  lock)
    hyprlock;;
  logout)
    hyprctl dispatch exit;;
  suspend)
    systemctl suspend;;
  reboot)
    systemctl reboot;;
  shutdown)
    systemctl poweroff -i;;
esac
