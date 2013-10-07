#!/bin/bash -ex

wget -N https://s3.amazonaws.com/Minecraft.Download/versions/1.6.4/1.6.4.jar -P ~/.minecraft/versions/1.6.4/

wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/mc1/2012-05-02T000009Z.tar.bz2

tar -xf 2012-05-02T000009Z.tar.bz2

rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/ $WORKSPACE/worlds

php genconfig.php > overviewerconfig

overviewer.py --config=overviewerconfig
