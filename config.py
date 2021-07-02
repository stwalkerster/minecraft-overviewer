import os
from .observer import JSObserver
from common import marker_definitions, nether_marker_definitions, end_marker_definitions

# General config
end_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.5)]
d_directions = dict(North="upper-left", South="lower-right", East="upper-right", West="lower-left")

# Configuration
configWorldUnixName = os.environ.get('BUILD_WORLD_UNIX_NAME')
configWorldHumanName = os.environ.get('BUILD_WORLD_NAME')
configWorldPath = os.environ.get('BUILD_WORLD_PATH')

configRenderNether = os.path.isdir(configWorldPath + "/DIM-1/region")
configRenderEnd = os.path.isdir(configWorldPath + "/DIM1/region")

configRenderFancyBits = os.environ.get('BUILD_RENDER_FANCY_BITS')

# Start of overviewer config
outputdir = "/map/" + configWorldUnixName
customwebassets = "/config/assets"
processes = 2

observer = JSObserver(outputdir=outputdir, minrefresh=10)

worlds = dict()
worlds[configWorldHumanName] = configWorldPath

# Render defaults
world = configWorldHumanName


for directionName, directionCode in d_directions.items():
    renders[configWorldUnixName + "-overworld-day-" + directionName] = {
        "title": "Day - " + directionName,
        "dimension": "overworld",
        "northdirection": directionCode,
        "rendermode": "smooth_lighting",
        'markers': marker_definitions(),
    }

    if configRenderFancyBits == "yes":
        renders[configWorldUnixName + "-overworld-night-" + directionName] = {
            "title": "Night - " + directionName,
            "dimension": "overworld",
            "northdirection": directionCode,
            "rendermode": "smooth_night",
            'markers': marker_definitions(),
        }

    if configRenderNether:
        renders[configWorldUnixName + "-nether-nolighting-" + directionName] = {
            "title": "No lighting - " + directionName,
            "dimension": "nether",
            "northdirection": directionCode,
            "rendermode": [Base(), EdgeLines(), Depth(max=127), Nether()],
            'markers': nether_marker_definitions(),
        }

        if configRenderFancyBits == "yes":
            renders[configWorldUnixName + "-nether-" + directionName] = {
                "title": directionName,
                "dimension": "nether",
                "northdirection": directionCode,
                "rendermode": [Base(), EdgeLines(), Depth(min=0,max=127), Nether(), SmoothLighting()],
                'markers': nether_marker_definitions(),
            }
            renders[configWorldUnixName + "-nether-roof-" + directionName] = {
                "title": "Roof - " + directionName,
                "dimension": "nether",
                "northdirection": directionCode,
                "rendermode": [Base(), EdgeLines(), Depth(min=127)],
                'markers': nether_marker_definitions(),
            }
            renders[configWorldUnixName + "-nether-overlay-biome-" + directionName] = {
                "title": "Biomes",
                "rendermode": [ClearBase(), BiomeOverlay()],
                "dimension": "nether",
                "overlay": [configWorldUnixName + "-nether-" + directionName,
                            configWorldUnixName + "-nether-nolighting-" + directionName,
                            configWorldUnixName + "-nether-roof-" + directionName],
                "northdirection": directionCode,
            }

    if configRenderEnd:
        renders[configWorldUnixName + "-end-nolighting-" + directionName] = {
            "title": "No lighting - " + directionName,
            "dimension": "end",
            "northdirection": directionCode,
            "rendermode": "normal",
            'markers': end_marker_definitions(),
        }

        if configRenderFancyBits == "yes":
            renders[configWorldUnixName + "-end-" + directionName] = {
                "title": directionName,
                "dimension": "end",
                "northdirection": directionCode,
                "rendermode": "smooth_lighting",
                'markers': end_marker_definitions(),
            }

    if configRenderFancyBits == "yes":
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
