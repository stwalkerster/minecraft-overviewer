#!/bin/bash

ssh jenkins@metapod.lon.stwalkerster.net 'echo '"'"'tellraw @a {"text":"[Jenkins: Build aborted by '$1'.]","color":"gray","italic":true}'"'"' > /mnt/minecraft/minecraft-cowgate.fifo'
