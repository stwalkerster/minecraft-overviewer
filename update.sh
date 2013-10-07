#!/bin/bash -ex

rsync -avz -e "ssh -vi /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/ $WORKSPACE/worlds

# overviewer.py --config=overviewerconfig
