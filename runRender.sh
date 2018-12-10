#!/bin/bash -xe

function serverCommand {
    echo "$1" > /opt/minecraft/tantallon/stdin.fifo
}

serverCommand 'tellraw @a {"text":"[ninetales: Initiating new render job]","color":"gray","italic":true}'
serverCommand 'save-off'
serverCommand 'save-all'

sleep 5

rsync -avz /opt/minecraft/ /home/minecraft/minecraft-overviewer/worlds/

serverCommand 'save-on'
serverCommand 'tellraw @a {"text":"[ninetales: Clone of world complete. Initiating render.]","color":"gray","italic":true}'

php genconfig.php > overviewerconfig

PYTHONPATH=`pwd`

nice --adjustment=10 /home/minecraft/overviewer/overviewer.py --config=overviewerconfig -p 4

serverCommand 'tellraw @a {"text":"[ninetales: Render complete. ]","color":"gray","italic":true}'
serverCommand 'tellraw @a {"text":"          https://scimonshouse.net/minecraft/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"https://scimonshouse.net/minecraft/"}}'
