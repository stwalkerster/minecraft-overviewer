#!/bin/bash -ex

mkdir -p maps

#Initiating new render job
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Initiating new render job]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Initiating new render job]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-crew.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Initiating new render job]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-combatupdate.fifo'

# /save-off
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-off'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-off'"'"' > /mnt/minecraft/minecraft-crew.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-off'"'"' > /mnt/minecraft/minecraft-combatupdate.fifo'

# Waiting for save to complete.
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Waiting for save to complete.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Waiting for save to complete.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-crew.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Waiting for save to complete.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-combatupdate.fifo'

# /save-all
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-all'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-all'"'"' > /mnt/minecraft/minecraft-crew.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-all'"'"' > /mnt/minecraft/minecraft-combatupdate.fifo'


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

# Transferring world to render server.
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Transferring world to render server.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Transferring world to render server.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-crew.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Transferring world to render server.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-combatupdate.fifo'

rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/combatupdate/ $WORKSPACE/worlds2
rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/crew/ $WORKSPACE/worlds2
rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/cowgate/ $WORKSPACE/worlds2
rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/creative/ $WORKSPACE/worlds2
rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/mc1.5/ $WORKSPACE/worlds2
rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/ohai/ $WORKSPACE/worlds2
rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/os-gb/ $WORKSPACE/worlds2

# Transfer complete. Initiating render.
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Transfer complete. Initiating render.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Transfer complete. Initiating render.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-crew.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Transfer complete. Initiating render.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-combatupdate.fifo'

# /save-on
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-on'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-on'"'"' > /mnt/minecraft/minecraft-crew.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-on'"'"' > /mnt/minecraft/minecraft-combatupdate.fifo'

php genconfig.php > overviewerconfig

overviewer.py --config=overviewerconfig --genpoi

overviewer.py --config=overviewerconfig

# Render complete. + URL
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Render complete. ]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"          http://cowgate.mc.stwalkerster.co.uk/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"http://cowgate.mc.stwalkerster.co.uk/"}}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'

ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Render complete. ]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-crew.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"          http://crew.mc.stwalkerster.co.uk/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"http://crew.mc.stwalkerster.co.uk/"}}'"'"' > /mnt/minecraft/minecraft-crew.fifo'

ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Render complete. ]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-combatupdate.fifo'
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"          http://cowgate.mc.stwalkerster.co.uk/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"http://cowgate.mc.stwalkerster.co.uk/"}}'"'"' > /mnt/minecraft/minecraft-combatupdate.fifo'
