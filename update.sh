#!/bin/bash

rsync -avz -e "ssh -i /home/stwalkerster/minecraft.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/ /home/stwalkerster/public_html/minecraft/worlds

overviewer.py --config=overviewerconfig
