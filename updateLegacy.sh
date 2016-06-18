#!/bin/bash -ex

mkdir -p maps
mkdir -p worlds

wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/mc1/2012-05-02T000009Z.tar.bz2

wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/backups.tar

tar -xf 2012-05-02T000009Z.tar.bz2
tar -xf backups.tar
mkdir -p beta1.8/
tar -xf backups/1.8pre-final.tar.bz2 -C beta1.8/
mkdir -p freebuild/
tar -xf backups/freebuild-final.tar.bz2 -C freebuild/
mkdir -p survival/
tar -xf backups/survival-final.tar.bz2 -C survival/

rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/creative/ $WORKSPACE/worlds/creative
rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/mc1.5/ $WORKSPACE/worlds/mc1.5
rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/ohai/ $WORKSPACE/worlds/ohai
rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/os-gb/ $WORKSPACE/worlds/os-gb

exit

php genconfig.php > overviewerconfig

overviewer.py --config=overviewerconfig --genpoi

overviewer.py --config=overviewerconfig