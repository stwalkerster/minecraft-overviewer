def marker_definitions():
    return [
        dict(name="Player bases", filterFunction=houseSignFilter, icon="custom-icons/marker_house.png", checked="true", showIconInLegend="true"),
        dict(name="Ender Chests", filterFunction=enderchestFilter, icon="custom-icons/marker_enderchest.png", showIconInLegend="true"),
        dict(name="<abbr title='Points of Interest'>POIs</abbr>", filterFunction=pointOfInterestSignFilter, icon="custom-icons/marker_poi.png", checked="true", showIconInLegend="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="custom-icons/marker_portal.png", checked="true", showIconInLegend="true"),
        dict(name="Farms", filterFunction=farmSignFilter, icon="custom-icons/marker_farm.png", showIconInLegend="true"),
        dict(name="Fast Travel", filterFunction=fastTravelSignFilter, icon="custom-icons/marker_fasttravel.png", checked="true", showIconInLegend="true"),
        dict(name="Transport", filterFunction=transportSignFilter, icon="custom-icons/marker_train.png", checked="true", showIconInLegend="true"),

        dict(name="Towns", filterFunction=townSignFilter, icon="custom-icons/marker_town.png", checked="true", showIconInLegend="true"),

        dict(name="Structures", filterFunction=generatedStructureFilter, icon="custom-icons/marker_temple.png", showIconInLegend="true"),
        dict(name="Spawners", filterFunction=spawnerFilter, icon="custom-icons/marker_spawner.png"),
        dict(name="Pillager outposts", filterFunction=pillagerFilter, icon="custom-icons/marker_illager.png"),
        dict(name="Mansions", filterFunction=mansionFilter, icon="custom-icons/marker_mansion.png"),
        dict(name="Ocean Monuments", filterFunction=monumentFilter, icon="custom-icons/marker_monument.png"),
        dict(name="Strongholds", filterFunction=strongholdFilter, icon="custom-icons/marker_stronghold.png"),
        dict(name="Temples", filterFunction=templeSignFilter, icon="custom-icons/marker_temple.png"),
        dict(name="Witch Huts", filterFunction=witchHutSignFilter, icon="custom-icons/marker_witch.png"),
        dict(name="Ocean Ruins", filterFunction=ruinsFilter, icon="custom-icons/marker_ruins.png"),
        dict(name="Shipwrecks", filterFunction=shipwreckFilter, icon="custom-icons/marker_shipwreck.png"),
    ]


def nether_marker_definitions():
    return [
        dict(name="Houses", filterFunction=houseSignFilter, icon="custom-icons/marker_house.png", checked="true", showIconInLegend="true"),
        dict(name="Ender Chests", filterFunction=enderchestFilter, icon="custom-icons/marker_enderchest.png", checked="true", showIconInLegend="true"),
        dict(name="Points of Interest", filterFunction=pointOfInterestSignFilter, icon="custom-icons/marker_poi.png", checked="true", showIconInLegend="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="custom-icons/marker_portal.png", checked="true", showIconInLegend="true"),
        dict(name="Farms", filterFunction=farmSignFilter, icon="custom-icons/marker_farm.png", showIconInLegend="true"),
        dict(name="Transport", filterFunction=transportSignFilter, checked="true", showIconInLegend="true"),

        dict(name="Structures", filterFunction=generatedStructureFilter, icon="custom-icons/marker_temple.png", showIconInLegend="true"),
        dict(name="Spawners", filterFunction=spawnerFilter, icon="custom-icons/marker_spawner.png"),
        dict(name="Nether Fortresses", filterFunction=fortressSignFilter, icon="custom-icons/marker_fortress.png"),
        dict(name="Bastion Remnants", filterFunction=bastionRemnantSignFilter, icon="custom-icons/marker_fortress.png"),
    ]


def end_marker_definitions():
    return [
        dict(name="Houses", filterFunction=houseSignFilter, icon="custom-icons/marker_house.png", checked="true"),
        dict(name="Ender Chests", filterFunction=enderchestFilter, icon="custom-icons/marker_enderchest.png", checked="true"),
        dict(name="Points of Interest", filterFunction=pointOfInterestSignFilter, icon="custom-icons/marker_poi.png", checked="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="../marker_portal.png", checked="true"),
        dict(name="Farms", filterFunction=farmSignFilter, icon="custom-icons/marker_farm.png", checked="false", showIconInLegend="true"),
        dict(name="Transport", filterFunction=transportSignFilter, checked="true"),
        dict(name="Structures", filterFunction=generatedStructureFilter, icon="custom-icons/marker_temple.png", showIconInLegend="true"),
    ]


def generatedStructureFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[not yet implemented]" == poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def spawnerFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Spawner]" == poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def witchHutSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Witch Hut]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def templeSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Temple]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def houseSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[House]" in poi['Text1']:
            poi['icon'] = "custom-icons/marker_house.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Hut]" in poi['Text1']:
            poi['icon'] = "custom-icons/marker_hut.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Mine]" in poi['Text1']:
            poi['icon'] = "custom-icons/marker_mines.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Minecamp]" in poi['Text1']:
            poi['icon'] = "custom-icons/marker_hut.png"
            return "\n".join("<em>Deprecated tag, please replace with [Farm].</em><br />", [poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def townSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Town]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def portalSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Portal]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def pointOfInterestSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[POI]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def transportSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Station]" in poi['Text1'] or "[NFT]" in poi['Text1']:
            poi['icon'] = "custom-icons/marker_train.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Dock]" in poi['Text1']:
            poi['icon'] = "custom-icons/marker_dock.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Canal]" in poi['Text1']:
            poi['icon'] = "custom-icons/marker_canal.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Stable]" in poi['Text1']:
            poi['icon'] = "custom-icons/marker_stable.png"
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def fastTravelSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Fast Travel" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def farmSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Farm]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
        if "[Enclosure]" in poi['Text1'] or "[Field]" in poi['Text1'] or "[Arboretum]" in poi['Text1']:
            return "\n".join(["<em>Deprecated tag, please replace with [Farm].</em><br />", poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def fortressSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Fortress]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def bastionRemnantSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Bastion]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def strongholdFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Stronghold]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def shipwreckFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Shipwreck]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def mansionFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Mansion]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def monumentFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Monument]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def ruinsFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Ruins]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def iglooFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Igloo]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def pillagerFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Illager]" in poi['Text1'] or "[Pillager]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def enderchestFilter(poi):
    if poi['id'] == 'minecraft:ender_chest':
        return "\n".join(["Ender Chest", "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
