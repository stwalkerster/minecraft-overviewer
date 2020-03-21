def marker_definitions():
    return [
        dict(name="Witch Huts", filterFunction=witchHutSignFilter, icon="custom-icons/marker_witch.png", checked="true"),
        dict(name="Temples", filterFunction=templeSignFilter, icon="custom-icons/marker_temple.png", checked="true"),
        dict(name="Houses", filterFunction=houseSignFilter, icon="custom-icons/marker_house.png", checked="true"),
        dict(name="Towns", filterFunction=townSignFilter, icon="custom-icons/marker_town.png", checked="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="custom-icons/marker_portal.png", checked="true"),
        dict(name="Points of Interest", filterFunction=pointOfInterestSignFilter, icon="custom-icons/marker_poi.png", checked="true"),
        dict(name="Minecart Station", filterFunction=trainSignFilter, icon="custom-icons/marker-train.png", checked="true"),
        dict(name="Dock", filterFunction=dockSignFilter, icon="custom-icons/marker_dock.png", checked="true"),
        dict(name="Canal", filterFunction=canalSignFilter, icon="custom-icons/marker_canal.png", checked="true"),
        dict(name="Spawners", filterFunction=spawnerFilter, icon="custom-icons/marker_spawner.png", checked="false"),
        dict(name="Mines", filterFunction=mineSignFilter, icon="custom-icons/marker_mines.png", checked="true"),
        dict(name="Abandoned Mineshafts", filterFunction=mineshaftSignFilter, icon="custom-icons/marker_mineshaft.png", checked="true"),
        dict(name="Mining camps", filterFunction=minecampFilter, icon="custom-icons/marker_miningcamp.png", checked="true"),
        dict(name="Farming: Fields", filterFunction=fieldSignFilter, icon="custom-icons/field.png", checked="true"),
        dict(name="Farming: Enclosures", filterFunction=enclosureSignFilter, icon="custom-icons/enclosure.png", checked="true"),
        dict(name="Huts", filterFunction=hutFilter, icon="custom-icons/marker_hut.png", checked="true"),
        dict(name="Strongholds", filterFunction=strongholdFilter, icon="custom-icons/marker_stronghold.png", checked="true"),
        dict(name="Shipwrecks", filterFunction=shipwreckFilter, icon="custom-icons/shipwreck.png", checked="true"),
        dict(name="Mansions", filterFunction=mansionFilter, icon="custom-icons/marker_mansion.png", checked="true"),
        dict(name="Ocean Monuments", filterFunction=monumentFilter, icon="custom-icons/marker_monument.png", checked="true"),
        dict(name="Ruins", filterFunction=ruinsFilter, icon="custom-icons/marker_ruins.png", checked="true"),
        dict(name="Arboreta", filterFunction=arboretaFilter, icon="custom-icons/marker_arboreta.png", checked="true"),
        dict(name="Illager outposts", filterFunction=illagerFilter, icon="custom-icons/marker_illager.png", checked="true"),
        dict(name="Players", filterFunction=playerFilter, checked="true"),
    ]


def nether_marker_definitions():
    return [
        dict(name="Nether Fast Transport", filterFunction=netherFastTransportSignFilter, icon="custom-icons/underground.png", checked="true"),
        dict(name="Points of Interest", filterFunction=pointOfInterestSignFilter, icon="custom-icons/marker_poi.png", checked="true"),
        dict(name="Houses", filterFunction=houseSignFilter, icon="custom-icons/marker_house.png", checked="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="custom-icons/marker_portal.png", checked="true"),
        dict(name="Nether Fortresses", filterFunction=fortressSignFilter, icon="custom-icons/marker_fortress.png", checked="true"),
        dict(name="Spawners", filterFunction=spawnerFilter, icon="custom-icons/marker_spawner.png", checked="false"),
        dict(name="Huts", filterFunction=hutFilter, icon="custom-icons/marker_hut.png", checked="true"),
    ]


def end_marker_definitions():
    return [
        dict(name="Points of Interest", filterFunction=pointOfInterestSignFilter, icon="../treasure-mark.png", checked="true"),
        dict(name="Huts", filterFunction=hutFilter, icon="../bunker-2-2.png", checked="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="../marker_portal.png", checked="true"),
    ]


def underbellyFilter(poi):
    if poi['id'] == 'Sign':
        if "[Underbelly]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def spawnerFilter(poi):
    if poi['id'] == 'Sign':
        if "[Spawner]" == poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def witchHutSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[Witch Hut]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def templeSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[Temple]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def houseSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[House]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def townSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[Town]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def portalSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[Portal]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def pointOfInterestSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[POI]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def trainSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[Station]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def dockSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[Dock]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def canalSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[Canal]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def netherFastTransportSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[NFT]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def mineSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[Mine]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def mineshaftSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Mineshaft]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def enclosureSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[Enclosure]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def fieldSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[Field]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def fortressSignFilter(poi):
    if poi['id'] == 'Sign':
        if "[Fortress]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def hutFilter(poi):
    if poi['id'] == 'Sign':
        if "[Hut]" in poi['Text1']:
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

def minecampFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Minecamp]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def arboretaFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Arboretum]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def iglooFilter(poi):
    if poi['id'] == 'Sign':
        if "[Igloo]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def illagerFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Illager]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def playerFilter(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "http://cravatar.eu/helmavatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']
