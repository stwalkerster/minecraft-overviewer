#!/bin/bash -ex

rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/ $WORKSPACE/worlds

php genconfig.php > overviewerconfig

overviewer.py --config=overviewerconfig
