#!/usr/bin/env bash -ex

function serverCommand {
    ssh -p 8022 -o StrictHostKeyChecking=no jenkins@localhost 'echo '"'"$1"'"' > /mnt/minecraft/minecraft-'$BUILD_WORLD_UNIX_NAME'.fifo'
}

echo "deb http://overviewer.org/debian ./" | sudo tee /etc/apt/sources.list.d/overviewer.list
wget -O - http://overviewer.org/debian/overviewer.gpg.asc | sudo apt-key add -

sudo apt-get update
sudo apt-get install minecraft-overviewer -qy

# open SSH tunnel to metapod
ssh -Nf -L 8022:metapod:22 -o ExitOnForwardFailure=yes -o ControlPath=~/.ssh/fearow.lon.stwalkerster.net.ctl jenkins@fearow.lon.stwalkerster.net

sudo chmod a+rwx /mnt

mkdir -p /mnt/maps/$BUILD_WORLD_UNIX_NAME

serverCommand 'tellraw @a {"text":"[Jenkins: Initiating new render job]","color":"gray","italic":true}'
serverCommand 'save-off'
serverCommand 'save-all force'
serverCommand 'tellraw @a {"text":"[Jenkins: Waiting for save to complete, then transferring world]","color":"gray","italic":true}'

sleep 5

rsync -avz -e "ssh -o StrictHostKeyChecking=no -p 8022" --exclude lost+found --exclude '*.tar.bz' minecraft@localhost:/mnt/minecraft/$BUILD_WORLD_UNIX_NAME/ $WORKSPACE/server

serverCommand 'tellraw @a {"text":"[Jenkins: Transfer complete. Initiating render.]","color":"gray","italic":true}'
serverCommand 'save-on'

PYTHONPATH=`pwd` overviewer.py --config=config.py --genpoi
PYTHONPATH=`pwd` overviewer.py --config=config.py

serverCommand 'tellraw @a {"text":"[Jenkins: Render complete. ]","color":"gray","italic":true}'
serverCommand 'tellraw @a {"text":"          http://'$BUILD_WORLD_UNIX_NAME'.mc.stwalkerster.co.uk/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"http://'$BUILD_WORLD_UNIX_NAME'.mc.stwalkerster.co.uk/"}}'

# close control connection
ssh -T -O exit fearow.lon.stwalkerster.net