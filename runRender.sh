#!/bin/bash -xe

function serverCommand {
    ssh minecraft@ninetales.mgmt.scimonshouse.net 'echo '"'"$1"'"' > /opt/minecraft/tantallon/stdin.fifo'
}

serverCommand 'tellraw @a {"text":"[growlithe: Initiating new render job]","color":"gray","italic":true}'
serverCommand 'save-off'
serverCommand 'save-all'

sleep 5

rsync -avz minecraft@ninetales.mgmt.scimonshouse.net:/opt/minecraft/ /home/minecraft/minecraft-overviewer/worlds/

serverCommand 'save-on'
serverCommand 'tellraw @a {"text":"[growlithe: Clone of world complete. Initiating render.]","color":"gray","italic":true}'

php genconfig.php > overviewerconfig

PYTHONPATH=`pwd`

#nice --adjustment=10 /home/minecraft/overviewer/overviewer.py --config=overviewerconfig -p 24
nice --adjustment=10 /usr/bin/overviewer.py --config=overviewerconfig -p 24

serverCommand 'tellraw @a {"text":"[growlithe: Render complete. ]","color":"gray","italic":true}'
serverCommand 'tellraw @a {"text":"          https://scimonshouse.net/minecraft/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"https://scimonshouse.net/minecraft/"}}'
