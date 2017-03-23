#!/bin/bash -ex

mkdir -p maps
mkdir -p worlds

# Old, old worlds
wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/mc1/2012-05-02T000009Z.tar.bz2
tar -xf 2012-05-02T000009Z.tar.bz2
mv mc1-world worlds/mc1
rm 2012-05-02T000009Z.tar.bz2

wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/backups.tar
tar -xf backups.tar

mkdir -p beta1.8/
tar -xf backups/1.8pre-final.tar.bz2 -C beta1.8/
mv beta1.8/world worlds/beta1.8
rmdir beta1.8/

mkdir -p freebuild/
tar -xf backups/freebuild-final.tar.bz2 -C freebuild/
mv freebuild/world3 worlds/freebuild
rmdir freebuild/

mkdir -p survival/
tar -xf backups/survival-final.tar.bz2 -C survival/
mv survival/world worlds/survival
rmdir survival/

rm -r backups/
rm backups.tar

# Old metapod worlds
wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/combatupdate.tar.gz
tar xf combatupdate.tar.gz
mv combatupdate/world/ worlds/combatupdate
rm -r combatupdate/ combatupdate.tar.gz

wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/cowgate.tar.gz
tar xf cowgate.tar.gz
mv cowgate/cowgate/ worlds/cowgate
rm -r cowgate/ cowgate.tar.gz

wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/creative.tar.gz
tar xf creative.tar.gz
mv creative/world/ worlds/creative
rm -r creative/ creative.tar.gz

wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/crew.tar.gz
tar xf crew.tar.gz
mv crew/world/ worlds/crew
rm -r crew/ crew.tar.gz

wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/mc1.5.tar.gz
tar xf mc1.5.tar.gz
mv mc1.5/world/ worlds/mc1.5
rm -r mc1.5/ mc1.5.tar.gz

wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/ohai.tar.gz
tar xf ohai.tar.gz
mv ohai/world/ worlds/ohai
rm -r ohai/ ohai.tar.gz

# Generate worlds
for wc in `ls world-config.d`; do
	mkdir -p maps/$wc
	rm -f build-parts.d/50-worldconfig.py
	ln -s ../world-config.d/$wc build-parts.d/50-worldconfig.py
	cat build-parts.d/* > overviewerconfig

	overviewer.py --config=overviewerconfig --genpoi
	overviewer.py --config=overviewerconfig
done;
