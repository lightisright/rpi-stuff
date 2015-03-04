#!/bin/sh

# activer la sortie HDMI
# tvservice -p
# si problème d'affichage du slideshow après extinction de l'écran :
tvservice -p
sleep 0.2
chvt 1
sleep 0.2
chvt 2

