#!/bin/bash -ex

#wget -N https://s3.amazonaws.com/Minecraft.Download/versions/1.6.4/1.6.4.jar -P ~/.minecraft/versions/1.6.4/

#rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/ $WORKSPACE/worlds

php genconfig.php > overviewerconfig

overviewer.py --config=overviewerconfig --genpoi

#overviewer.py --config=overviewerconfig
