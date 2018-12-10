#!/bin/bash -xe

function serverCommand {
    echo "$1" > /opt/minecraft/tantallon/stdin.fifo
}

serverCommand 'tellraw @a {"text":"[ninetales: Initiating POI update job]","color":"gray","italic":true}'
serverCommand 'save-off'
serverCommand 'save-all flush'

sleep 5

rsync -avz /opt/minecraft/ /home/minecraft/minecraft-overviewer/worlds/

serverCommand 'save-on'

php genconfig.php > overviewerconfig

PYTHONPATH=`pwd`

nice --adjustment=10 /home/minecraft/overviewer/overviewer.py --config=overviewerconfig --genpoi
# nice --adjustment=10 /home/minecraft/overviewer/overviewer.py --config=overviewerconfig -p 4

serverCommand 'tellraw @a {"text":"[ninetales: Update complete.]","color":"gray","italic":true}'
serverCommand 'tellraw @a {"text":"          https://scimonshouse.net/minecraft/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"https://scimonshouse.net/minecraft/"}}'
