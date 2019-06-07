#!/bin/bash -xe

export ServerHost=ninetales
export RenderHost=growlithe
export InstanceName=pillage

function serverCommand {
    ssh minecraft@${ServerHost}.scimonshouse.net 'echo '"'"$1"'"' > /opt/minecraft/'$InstanceName'/stdin.fifo'
}

serverCommand 'tellraw @a {"text":"['$RenderHost': Initiating POI update job]","color":"gray","italic":true}'
serverCommand 'save-off'
serverCommand 'save-all flush'

sleep 5

rsync -avz minecraft@${ServerHost}.scimonshouse.net:/opt/minecraft/ /home/minecraft/minecraft-overviewer/worlds/

serverCommand 'save-on'

php genconfig-${InstanceName}.php > overviewerconfig-${InstanceName}

PYTHONPATH=`pwd`

#nice --adjustment=10 /home/minecraft/overviewer/overviewer.py --config=overviewerconfig --genpoi
nice --adjustment=10 overviewer.py --config=overviewerconfig-${InstanceName} --genpoi

serverCommand 'tellraw @a {"text":"['$RenderHost': Update complete.]","color":"gray","italic":true}'
serverCommand 'tellraw @a {"text":"          https://scimonshouse.net/mcmaps/'$InstanceName'/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"https://scimonshouse.net/mcmaps/'$Instance$
