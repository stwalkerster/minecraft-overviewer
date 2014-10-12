#!/bin/bash -ex

mkdir -p maps

#Initiating new render job
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Initiating POI update job]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'

# /save-off
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-off'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'

# Waiting for save to complete.
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Waiting for save to complete.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'

# /save-all
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-all'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'

sleep 5

# Transferring world to render server.
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Transferring world to render server.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'

rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/ $WORKSPACE/worlds

# Transfer complete. Initiating render.
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Transfer complete. Initiating update.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'

# /save-on
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'save-on'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'

php genconfig.php > overviewerconfig

overviewer.py  --genpoi --config=overviewerconfig

# Render complete. + URL
ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: POI update complete. ]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'
