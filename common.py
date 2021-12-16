# Misc: #c259b6
# Transport: #9d7050
# Players: #128e4e
# Structures: #f34648
import os


def marker_definitions():
    markers = [
        dict(name="Player bases", filterFunction=houseSignFilter, icon="custom-icons/player/marker_house.png",
             checked="true", showIconInLegend="true"),
        dict(name="Farms", filterFunction=farmSignFilter, icon="custom-icons/player/marker_farm.png",
             showIconInLegend="true"),

        dict(name="Ender Chests", filterFunction=enderchestFilter, icon="custom-icons/auto/marker_enderchest.png",
             showIconInLegend="true"),

        dict(name="Towns", filterFunction=townSignFilter, icon="custom-icons/misc/marker_town.png", checked="true",
             showIconInLegend="true"),
        dict(name="<abbr title='Points of Interest'>POIs</abbr>", filterFunction=pointOfInterestSignFilter,
             icon="custom-icons/misc/marker_poi.png", checked="true", showIconInLegend="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="custom-icons/misc/marker_portal.png",
             checked="true", showIconInLegend="true")
    ]

    if os.environ.get('BUILD_MARKER_FASTTRAVEL') == 'yes':
        markers.append(dict(name="Fast Travel", filterFunction=fastTravelSignFilter, icon="custom-icons/transport/marker_fasttravel.png", checked="true", showIconInLegend="true"))

    markers.append(dict(name="Transport", filterFunction=transportSignFilter, icon="custom-icons/transport/marker_train.png", checked="true", showIconInLegend="true"))
    markers.append(dict(name="<abbr title='Structures generated with the world'>Structures</abbr>",
             filterFunction=generatedStructureFilter, icon="custom-icons/structures/marker_temple.png",
             showIconInLegend="true"))

    return markers


def nether_marker_definitions():
    return [
        dict(name="Player bases", filterFunction=houseSignFilter, icon="custom-icons/player/marker_house.png", checked="true", showIconInLegend="true"),
        dict(name="Farms", filterFunction=farmSignFilter, icon="custom-icons/player/marker_farm.png", showIconInLegend="true"),

        dict(name="Ender Chests", filterFunction=enderchestFilter, icon="custom-icons/auto/marker_enderchest.png", checked="true", showIconInLegend="true"),

        dict(name="<abbr title='Points of Interest'>POIs</abbr>", filterFunction=pointOfInterestSignFilter, icon="custom-icons/misc/marker_poi.png", checked="true", showIconInLegend="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="custom-icons/misc/marker_portal.png", checked="true", showIconInLegend="true"),

        dict(name="Transport", filterFunction=transportSignFilter, icon="custom-icons/transport/marker_train.png", checked="true", showIconInLegend="true"),

        dict(name="<abbr title='Structures generated with the world'>Structures</abbr>", filterFunction=generatedStructureFilter, icon="custom-icons/structures/marker_temple.png", showIconInLegend="true"),
    ]


def end_marker_definitions():
    return [
        dict(name="Player bases", filterFunction=houseSignFilter, icon="custom-icons/player/marker_house.png", checked="true", showIconInLegend="true"),
        dict(name="Farms", filterFunction=farmSignFilter, icon="custom-icons/player/marker_farm.png", showIconInLegend="true"),

        dict(name="Ender Chests", filterFunction=enderchestFilter, icon="custom-icons/auto/marker_enderchest.png", checked="true", showIconInLegend="true"),

        dict(name="<abbr title='Points of Interest'>POIs</abbr>", filterFunction=pointOfInterestSignFilter, icon="custom-icons/misc/marker_poi.png", showIconInLegend="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="custom-icons/transport/marker_endportal.png", checked="true", showIconInLegend="true"),

        dict(name="Transport", filterFunction=transportSignFilter, icon="custom-icons/transport/marker_train.png", checked="true", showIconInLegend="true"),

        dict(name="<abbr title='Structures generated with the world'>Structures</abbr>", filterFunction=generatedStructureFilter, icon="custom-icons/structures/marker_temple.png", showIconInLegend="true"),
    ]

def getCoords(poi):
    return "(" + ", ".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"

def generatedStructureFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Spawner]" == poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_spawner.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />", getCoords(poi)])
        if "[Witch Hut]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_witch.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Temple]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_temple.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Stronghold]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_stronghold.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Shipwreck]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_shipwreck.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Mansion]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_mansion.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Monument]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_monument.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Ruins]" in poi['Text1'] or "[Ruin]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_ruins.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Igloo]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_igloo.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Illager]" in poi['Text1'] or "[Pillager]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_illager.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Ruined Portal]" in poi['Text1'] or "[Pillager]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_ruinedportal.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Fortress]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_fortress.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Bastion]" in poi['Text1'] or "[Bastion Remnant]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_bastion.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[End City]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_endcity.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def houseSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[House]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_house.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Hut]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_hut.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Mine]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_mines.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Minecamp]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_hut.png"
            return "\n".join(["<em>Deprecated tag, please replace with [Hut].</em><br />", poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def townSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Town]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def portalSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Portal]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
    if poi['id'] == 'minecraft:end_gateway':
        poi['icon'] = "custom-icons/transport/marker_endportal.png"
        return "\n".join(["End Gateway", "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def pointOfInterestSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[POI]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Villager Trading]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_tradinghall.png"
            return "Villager Trading Hall\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def transportSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Station]" in poi['Text1'] or "[NFT]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_train.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Dock]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_dock.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Canal]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_canal.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Stable]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_stable.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def fastTravelSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Fast Travel" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def farmSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Farm]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Enclosure]" in poi['Text1'] or "[Field]" in poi['Text1'] or "[Arboretum]" in poi['Text1']:
            return "\n".join(["<em>Deprecated tag, please replace with [Farm].</em><br />", poi['Text2'], poi['Text3'], poi['Text4'], "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def enderchestFilter(poi):
    if poi['id'] == 'minecraft:ender_chest':
        return "\n".join(["Ender Chest", "<br />(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
