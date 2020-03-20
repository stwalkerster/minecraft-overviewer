#!/bin/bash -xe

export ServerHost=gloom.lon.stwalkerster.net
export RenderHost=spearow.lon.stwalkerster.net
export InstanceName=gloom

function serverCommand {
    ssh -vv -o 'StrictHostKeyChecking accept-new' minecraft@${ServerHost} 'echo '"'"$1"'"' > /run/minecraft-'$InstanceName'.control'
}

serverCommand 'tellraw @a {"text":"['$RenderHost': Initiating new render job]","color":"gray","italic":true}'
serverCommand 'save-off'
serverCommand 'save-all'

sleep 5

rsync -avz  --delete minecraft@${ServerHost}:/opt/minecraft/ /opt/render/worlds

ln -sf /opt/render/worlds/${InstanceName}/world_nether/DIM-1 /opt/render/worlds/${InstanceName}/world/DIM-1
ln -sf /opt/render/worlds/${InstanceName}/world_the_end/DIM1 /opt/render/worlds/${InstanceName}/world/DIM1

serverCommand 'save-on'
serverCommand 'tellraw @a {"text":"['$RenderHost': Clone of world complete. Initiating render.]","color":"gray","italic":true}'

php genconfig-${InstanceName}.php > overviewerconfig-${InstanceName}

PYTHONPATH=`pwd`

nice --adjustment=10 /usr/bin/overviewer.py --config=overviewerconfig-${InstanceName} -p 4

serverCommand 'tellraw @a {"text":"['$RenderHost': Render complete. ]","color":"gray","italic":true}'
serverCommand 'tellraw @a {"text":"          https://minecraft.stwalkerster.co.uk/","italic":false,"color":"yellow","clickEvent":{"action":"open_url","value":"https://minecraft.stwalkerster.co.uk/"}}'
