#!/bin/bash -xe

function serverCommand {
    ssh minecraft@ninetales.mgmt.scimonshouse.net 'echo '"'"$1"'"' > /opt/minecraft/tantallon/stdin.fifo'
}

serverCommand 'tellraw @a {"text":"[growlithe: Initiating POI update job]","color":"gray","italic":true}'
serverCommand 'save-off'
serverCommand 'save-all flush'

sleep 5

rsync -avz minecraft@ninetales.mgmt.scimonshouse.net:/opt/minecraft/ /home/minecraft/minecraft-overviewer/worlds/

serverCommand 'save-on'

php genconfig.php > overviewerconfig

PYTHONPATH=`pwd`

#nice --adjustment=10 /home/minecraft/overviewer/overviewer.py --config=overviewerconfig --genpoi
nice --adjustment=10 overviewer.py --config=overviewerconfig --genpoi

serverCommand 'tellraw @a {"text":"[growlithe: Update complete.]","color":"gray","italic":true}'
serverCommand 'tellraw @a {"text":"          https://scimonshouse.net/minecraft/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"https://scimonshouse.net/minecraft/"}}'
