#!/bin/bash -ex

echo "Building world '" $BUILD_WORLD_NAME "' with unix name '" $BUILD_WORLD_UNIX_NAME "'"

mkdir -p maps/$BUILD_WORLD_UNIX_NAME

function serverCommand {
    ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"$1"'"' > /mnt/minecraft/minecraft-'$BUILD_WORLD_UNIX_NAME'.fifo'
}

serverCommand 'tellraw @a {"text":"[Jenkins: Initiating new render job]","color":"gray","italic":true}'
serverCommand 'save-off'
serverCommand 'save-all force'
serverCommand 'tellraw @a {"text":"[Jenkins: Waiting for save to complete, then transferring world]","color":"gray","italic":true}'

sleep 5

rsync -avz -e "ssh -i /var/lib/jenkins/.ssh/minecraft.metapod.id_rsa" --exclude lost+found --exclude '*.tar.bz' minecraft@metapod.lon.stwalkerster.net:/mnt/minecraft/$BUILD_WORLD_UNIX_NAME/ $WORKSPACE/server

serverCommand 'tellraw @a {"text":"[Jenkins: Transfer complete. Initiating render.]","color":"gray","italic":true}'
serverCommand 'save-on'

PYTHONPATH=`pwd` overviewer.py --config=config.py --genpoi
PYTHONPATH=`pwd` overviewer.py --config=config.py

serverCommand 'tellraw @a {"text":"[Jenkins: Render complete. ]","color":"gray","italic":true}'
serverCommand 'tellraw @a {"text":"          http://'$BUILD_WORLD_UNIX_NAME'.mc.stwalkerster.co.uk/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"http://'$BUILD_WORLD_UNIX_NAME'.mc.stwalkerster.co.uk/"}}'