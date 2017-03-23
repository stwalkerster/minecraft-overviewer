# 10-defs.py

def townFilter(poi):
    if poi['id'] == 'Town':
        return poi['name']

def witchFilter(poi):
    if poi['id'] == 'Witch':
        return poi['name']

def horseFilter(poi):
    if poi['id'] == 'Horses':
        return poi['name']

def underbellyFilter(poi):
    if poi['id'] == 'Sign':
        if "Underbelly" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
            
def spawnerFilter(poi):
    if poi['id'] == 'Sign':
        if "[Spawner]" == poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def witchHutSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Witch Hut" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def templeSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Temple" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def houseSignFilter(poi):
    if poi['id'] == 'Sign':
        if "House" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def townSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Town" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def portalSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Portal" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def pointOfInterestSignFilter(poi):
    if poi['id'] == 'Sign':
        if "POI" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
            
def trainSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Station" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
            
def dockSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Dock" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])
      
def canalSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Canal" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def netherFastTransportSignFilter(poi):
    if poi['id'] == 'Sign':
        if "NFT" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def mineSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Mine" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def enclosureSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Enclosure" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def fieldSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Field" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def fortressSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Fortress" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def hutFilter(poi):
    if poi['id'] == 'Sign':
        if "[Hut]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def iglooFilter(poi):
    if poi['id'] == 'Sign':
        if "Igloo" in poi['Text1']:
            return "\n".join([poi['Text1'], "", poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def playerFilter(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "http://cravatar.eu/helmavatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']
