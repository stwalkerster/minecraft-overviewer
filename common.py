def marker_definitions():
    return [
        dict(name="Witch Huts", filterFunction=witchHutSignFilter, icon="../marker_witch.png"),
        dict(name="Temples", filterFunction=templeSignFilter, icon="../temple-2.png"),
        dict(name="Houses", filterFunction=houseSignFilter, icon="../marker_house.png", checked="true"),
        dict(name="Towns", filterFunction=townSignFilter, icon="../marker_town.png", checked="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="../marker_portal.png", checked="true"),
        dict(name="Points of Interest", filterFunction=pointOfInterestSignFilter, icon="../treasure-mark.png",
             checked="true"),
        dict(name="Minecart Station", filterFunction=trainSignFilter, icon="../marker-train.png", checked="true"),
        dict(name="Dock", filterFunction=dockSignFilter, icon="../harbor.png", checked="true"),
        dict(name="Canal", filterFunction=canalSignFilter, icon="../taxiboat.png", checked="true"),
        dict(name="Spawners", filterFunction=spawnerFilter, icon="../zombie-outbreak1.png", checked="false"),
        dict(name="Mines", filterFunction=mineSignFilter, icon="../mine.png", checked="true"),
        dict(name="Farming: Fields", filterFunction=fieldSignFilter, icon="../field.png", checked="true"),
        dict(name="Farming: Enclosures", filterFunction=enclosureSignFilter, icon="../enclosure.png", checked="true"),
        dict(name="Huts", filterFunction=hutFilter, icon="../bunker-2-2.png", checked="true"),
        dict(name="Igloos", filterFunction=iglooFilter, icon="../bunker.png", checked="true"),
    ]


def nether_marker_definitions():
    return [
        dict(name="Nether Fast Transport", filterFunction=netherFastTransportSignFilter, icon="../underground.png",
             checked="true"),
        dict(name="Points of Interest", filterFunction=pointOfInterestSignFilter, icon="../treasure-mark.png",
             checked="true"),
        dict(name="Houses", filterFunction=houseSignFilter, icon="../marker_house.png", checked="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="../marker_portal.png", checked="true"),
        dict(name="Nether Fortresses", filterFunction=fortressSignFilter, icon="../castle-2.png", checked="true"),
        dict(name="Spawners", filterFunction=spawnerFilter, icon="../zombie-outbreak1.png", checked="false"),
        dict(name="Huts", filterFunction=hutFilter, icon="../bunker-2-2.png", checked="true"),
    ]


def end_marker_definitions():
    return [
        dict(name="Points of Interest", filterFunction=pointOfInterestSignFilter, icon="../treasure-mark.png",
             checked="true"),
        dict(name="Huts", filterFunction=hutFilter, icon="../bunker-2-2.png", checked="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="../marker_portal.png", checked="true"),
    ]



def underbellyFilter(poi):
    if poi['id'] == 'Sign':
        if "Underbelly" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def spawnerFilter(poi):
    if poi['id'] == 'Sign':
        if "[Spawner]" == poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def witchHutSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Witch Hut" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def templeSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Temple" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def houseSignFilter(poi):
    if poi['id'] == 'Sign':
        if "House" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def townSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Town" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def portalSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Portal" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def pointOfInterestSignFilter(poi):
    if poi['id'] == 'Sign':
        if "POI" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def trainSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Station" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def dockSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Dock" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def canalSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Canal" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def netherFastTransportSignFilter(poi):
    if poi['id'] == 'Sign':
        if "NFT" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def mineSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Mine" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def enclosureSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Enclosure" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def fieldSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Field" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def fortressSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Fortress" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def hutFilter(poi):
    if poi['id'] == 'Sign':
        if "Hut" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])


def iglooFilter(poi):
    if poi['id'] == 'Sign':
        if "Igloo" in poi['Text1']:
            return "\n".join([poi['Text1'], "", poi['Text2'], poi['Text3'], poi['Text4'],
                              "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
