#!/bin/bash -xe

export ServerHost=ninetales
export RenderHost=growlithe
export InstanceName=covid

function serverCommand {
    ssh minecraft@${ServerHost}.scimonshouse.net 'echo '"'"$1"'"' > /opt/minecraft/'$InstanceName'/stdin.fifo'
}

serverCommand 'tellraw @a {"text":"['$RenderHost': Initiating new render job]","color":"gray","italic":true}'
serverCommand 'save-off'
serverCommand 'save-all'

sleep 5

rsync -avz  --delete minecraft@${ServerHost}.scimonshouse.net:/opt/minecraft/ /home/minecraft/minecraft-overviewer/worlds/

ln -sf /home/minecraft/minecraft-overviewer/worlds/${InstanceName}/world_nether/DIM-1 /home/minecraft/minecraft-overviewer/worlds/${InstanceName}/world/DIM-1
ln -sf /home/minecraft/minecraft-overviewer/worlds/${InstanceName}/world_the_end/DIM1 /home/minecraft/minecraft-overviewer/worlds/${InstanceName}/world/DIM1

serverCommand 'save-on'
serverCommand 'tellraw @a {"text":"['$RenderHost': Clone of world complete. Initiating render.]","color":"gray","italic":true}'

php genconfig-${InstanceName}.php > overviewerconfig-${InstanceName}

PYTHONPATH=`pwd`

nice --adjustment=10 /home/minecraft/overviewer/overviewer.py --config=overviewerconfig-${InstanceName} -p 24
#nice --adjustment=10 /usr/bin/overviewer.py --config=overviewerconfig-${InstanceName} -p 24

serverCommand 'tellraw @a {"text":"['$RenderHost': Render complete. ]","color":"gray","italic":true}'
serverCommand 'tellraw @a {"text":"          https://scimonshouse.net/mcmaps/'$InstanceName'/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"https://scimonshouse.net/mcmaps/'$InstanceName'/"}}'
