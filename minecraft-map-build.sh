#!/bin/bash -ex

mkdir -p maps
mkdir -p worlds

# Old, old worlds
if [ -d worlds/mc1 ]; then
	echo "Skipping MC1 download"
else
	wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/mc1/2012-05-02T000009Z.tar.bz2
	tar -xf 2012-05-02T000009Z.tar.bz2
	mv mc1-world worlds/mc1
	rm 2012-05-02T000009Z.tar.bz2
fi

if [ -d worlds/survival ]; then
	echo "Skipping backups.tar download"
else
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
fi

# Old metapod worlds
if [ -d worlds/combatupdate ]; then
	echo "Skipping combatupdate download"
else
	wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/combatupdate.tar.gz
	tar xf combatupdate.tar.gz
	mv combatupdate/world/ worlds/combatupdate
	rm -r combatupdate/ combatupdate.tar.gz
fi

if [ -d worlds/cowgate ]; then
	echo "Skipping cowgate download"
else
	wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/cowgate.tar.gz
	tar xf cowgate.tar.gz
	mv cowgate/cowgate/ worlds/cowgate
	rm -r cowgate/ cowgate.tar.gz
fi

if [ -d worlds/creative ]; then
	echo "Skipping creative download"
else
	wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/creative.tar.gz
	tar xf creative.tar.gz
	mv creative/world/ worlds/creative
	rm -r creative/ creative.tar.gz
fi

if [ -d worlds/crew ]; then
	echo "Skipping crew download"
else
	wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/crew.tar.gz
	tar xf crew.tar.gz
	mv crew/world/ worlds/crew
	rm -r crew/ crew.tar.gz
fi

if [ -d worlds/mc1.5 ]; then
	echo "Skipping mc1.5 download"
else
	wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/mc1.5.tar.gz
	tar xf mc1.5.tar.gz
	mv mc1.5/world/ worlds/mc1.5
	rm -r mc1.5/ mc1.5.tar.gz
fi

if [ -d worlds/ohai ]; then
	echo "Skipping ohai download"
else
	wget -N https://s3-eu-west-1.amazonaws.com/minecraft-worlds/smp/ohai.tar.gz
	tar xf ohai.tar.gz
	mv ohai/world/ worlds/ohai
	rm -r ohai/ ohai.tar.gz
fi

# Generate worlds
for wc in `ls world-config.d`; do
	mkdir -p maps/$wc
	rm -f build-parts.d/50-worldconfig.py
	cp world-config.d/$wc build-parts.d/50-worldconfig.py
	cat build-parts.d/* > overviewerconfig

	overviewer.py --config=overviewerconfig --genpoi
	overviewer.py --config=overviewerconfig
	
	rm -f build-parts.d/50-worldconfig.py
done;
