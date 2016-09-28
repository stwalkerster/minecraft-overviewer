import os
from observer import JSObserver
from common import marker_definitions, nether_marker_definitions, end_marker_definitions

# General config
end_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.5)]
d_directions = dict(North="upper-left", South="lower-right", East="upper-right", West="lower-left")

# Configuration
configWorldUnixName = os.environ.get('BUILD_WORLD_UNIX_NAME')
configWorldHumanName = os.environ.get('BUILD_WORLD_NAME')

configWorldPath = "server/world"

configRenderNether = os.path.isdir(configWorldPath + "/DIM-1/region")
configRenderEnd = os.path.isdir(configWorldPath + "/DIM1/region")

# Start of overviewer config
outputdir = "/mnt/maps/" + configWorldUnixName
customwebassets = "assets"
processes = 2

observer = JSObserver(outputdir=outputdir, minrefresh=10)

worlds = dict()
worlds[configWorldHumanName] = configWorldPath

# Render defaults
world = configWorldHumanName


for directionName, directionCode in d_directions.iteritems():
    renders[configWorldUnixName + "-overworld-day-" + directionName] = {
        "title": "Day - " + directionName,
        "dimension": "overworld",
        "northdirection": directionCode,
        "rendermode": "smooth_lighting",
        'markers': marker_definitions(),
    }
    renders[configWorldUnixName + "-overworld-night-" + directionName] = {
        "title": "Night - " + directionName,
        "dimension": "overworld",
        "northdirection": directionCode,
        "rendermode": "smooth_night",
        'markers': marker_definitions(),
    }

    if configRenderNether:
        renders[configWorldUnixName + "-nether-" + directionName] = {
            "title": directionName,
            "dimension": "nether",
            "northdirection": directionCode,
            "rendermode": "nether_smooth_lighting",
            'markers': nether_marker_definitions(),
        }

    if configRenderEnd:
        renders[configWorldUnixName + "-end-" + directionName] = {
            "title": directionName,
            "dimension": "end",
            "northdirection": directionCode,
            "rendermode": "end_smooth_lighting",
            'markers': end_marker_definitions(),
        }

    renders[configWorldUnixName + "-overworld-overlay-biome-" + directionName] = {
        "title": "Biomes",
        "rendermode": [ClearBase(), BiomeOverlay()],
        "dimension": "overworld",
        "overlay": [configWorldUnixName + "-overworld-day-" + directionName,
                    configWorldUnixName + "-overworld-night-" + directionName],
        "northdirection": directionCode,
    }

    renders[configWorldUnixName + "-overworld-overlay-slime-" + directionName] = {
        "title": "Slime Spawn",
        "rendermode": [ClearBase(), SlimeOverlay(), BiomeOverlay(biomes=[("Swamp", (0, 255, 0))])],
        "dimension": "overworld",
        "overlay": [configWorldUnixName + "-overworld-day-" + directionName,
                    configWorldUnixName + "-overworld-night-" + directionName],
        "northdirection": directionCode,
    }
