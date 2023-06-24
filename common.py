# Misc: #c259b6
# Transport: #9d7050
# Players: #128e4e
# Structures: #f34648
import os


def overworld_marker_definitions():
    markers = [
        #dict(name="Player bases", filterFunction=houseSignFilter, icon="custom-icons/player/marker_house.png",
        #     checked="true", showIconInLegend="true"),
        #dict(name="Farms", filterFunction=farmSignFilter, icon="custom-icons/player/marker_farm.png",
        #     showIconInLegend="true"),

        #dict(name="Ender Chests", filterFunction=enderchestFilter, icon="custom-icons/auto/marker_enderchest.png",
        #     showIconInLegend="true"),

        #dict(name="Towns", filterFunction=townSignFilter, icon="custom-icons/misc/marker_town.png", checked="true",
        #     showIconInLegend="true"),
        #dict(name="<abbr title='Points of Interest'>POIs</abbr>", filterFunction=pointOfInterestSignFilter,
        #     icon="custom-icons/misc/marker_poi.png", checked="true", showIconInLegend="true"),
        #dict(name="Portals", filterFunction=portalSignFilter, icon="custom-icons/misc/marker_portal.png",
        #     checked="true", showIconInLegend="true")

        dict(name="Signs", filterFunction=fastlizardSignFilter, checked="true", icon="signpost_icon.png", showIconInLegend="true"),
        dict(name="Player bases", filterFunction=fastlizardHouseSignFilter, icon="custom-icons/player/marker_house.png", checked="true", showIconInLegend="true"),
        dict(name="Fast Travel", filterFunction=fastlizardFastTravelFilter, icon="custom-icons/transport/marker_fasttravel.png", checked="true", showIconInLegend="true"),
    ]

    #if os.environ.get('BUILD_MARKER_FASTTRAVEL') == 'yes':
    #    markers.append(dict(name="Fast Travel", filterFunction=fastTravelSignFilter, icon="custom-icons/transport/marker_fasttravel.png", checked="true", showIconInLegend="true"))

    markers.append(dict(name="Transport", filterFunction=fastlizardTransportSignFilter, icon="custom-icons/transport/marker_train.png", checked="true", showIconInLegend="true"))

    #markers.append(dict(name="<abbr title='Structures generated with the world'>Structures</abbr>",
    #         filterFunction=generatedStructureFilter, icon="custom-icons/structures/marker_temple.png",
    #         showIconInLegend="true"))

    return markers


def nether_marker_definitions():
    return [
        #dict(name="Player bases", filterFunction=houseSignNether, icon="custom-icons/player/marker_house.png", checked="true", showIconInLegend="true"),
        #dict(name="Farms", filterFunction=farmSignNether, icon="custom-icons/player/marker_farm.png", showIconInLegend="true"),

        #dict(name="Ender Chests", filterFunction=enderchestNether, icon="custom-icons/auto/marker_enderchest.png", checked="true", showIconInLegend="true"),

        #dict(name="<abbr title='Points of Interest'>POIs</abbr>", filterFunction=pointOfInterestSignNether, icon="custom-icons/misc/marker_poi.png", checked="true", showIconInLegend="true"),
        #dict(name="Portals", filterFunction=portalSignNether, icon="custom-icons/misc/marker_portal.png", checked="true", showIconInLegend="true"),

        #dict(name="Transport", filterFunction=transportSignNether, icon="custom-icons/transport/marker_train.png", checked="true", showIconInLegend="true"),

        #dict(name="<abbr title='Structures generated with the world'>Structures</abbr>", filterFunction=generatedStructureFilter, icon="custom-icons/structures/marker_temple.png", showIconInLegend="true"),
        dict(name="Signs", filterFunction=fastlizardSignFilter, checked="true", icon="signpost_icon.png", showIconInLegend="true"),
        dict(name="Player bases", filterFunction=fastlizardHouseSignFilter, icon="custom-icons/player/marker_house.png", checked="true", showIconInLegend="true"),
    ]


def nether_roof_marker_definitions():
    return [
        #dict(name="Player bases", filterFunction=houseSignRoof, icon="custom-icons/player/marker_house.png", checked="true", showIconInLegend="true"),
        #dict(name="Farms", filterFunction=farmSignRoof, icon="custom-icons/player/marker_farm.png", showIconInLegend="true"),

        #dict(name="Ender Chests", filterFunction=enderchestRoof, icon="custom-icons/auto/marker_enderchest.png", checked="true", showIconInLegend="true"),

        #dict(name="<abbr title='Points of Interest'>POIs</abbr>", filterFunction=pointOfInterestSignRoof, icon="custom-icons/misc/marker_poi.png", checked="true", showIconInLegend="true"),
        #dict(name="Portals", filterFunction=portalSignRoof, icon="custom-icons/misc/marker_portal.png", checked="true", showIconInLegend="true"),

        #dict(name="Transport", filterFunction=transportSignRoof, icon="custom-icons/transport/marker_train.png", checked="true", showIconInLegend="true"),
        dict(name="Signs", filterFunction=fastlizardSignFilter, checked="true", icon="signpost_icon.png", showIconInLegend="true"),
    ]


def end_marker_definitions():
    return [
        #dict(name="Player bases", filterFunction=houseSignFilter, icon="custom-icons/player/marker_house.png", checked="true", showIconInLegend="true"),
        #dict(name="Farms", filterFunction=farmSignFilter, icon="custom-icons/player/marker_farm.png", showIconInLegend="true"),

        #dict(name="Ender Chests", filterFunction=enderchestFilter, icon="custom-icons/auto/marker_enderchest.png", checked="true", showIconInLegend="true"),

        #dict(name="<abbr title='Points of Interest'>POIs</abbr>", filterFunction=pointOfInterestSignFilter, icon="custom-icons/misc/marker_poi.png", showIconInLegend="true"),
        dict(name="Portals", filterFunction=portalSignFilter, icon="custom-icons/transport/marker_endportal.png", checked="true", showIconInLegend="true"),

        #dict(name="Transport", filterFunction=transportSignFilter, icon="custom-icons/transport/marker_train.png", checked="true", showIconInLegend="true"),

        #dict(name="<abbr title='Structures generated with the world'>Structures</abbr>", filterFunction=generatedStructureFilter, icon="custom-icons/structures/marker_temple.png", showIconInLegend="true"),

        #dict(name="END FILTER", filterFunction=endFilter, checked="true", icon="signpost_icon.png", showIconInLegend="true"),
        dict(name="Signs", filterFunction=fastlizardSignFilter, checked="true", icon="signpost_icon.png", showIconInLegend="true"),
        dict(name="Player bases", filterFunction=fastlizardHouseSignFilter, icon="custom-icons/player/marker_house.png", checked="true", showIconInLegend="true"),
    ]


def formatSign(poi, title, note, includeFirstLine=False):
    if poi['id'] == 'minecraft:sign':
        lines = [poi['Text2'], poi['Text3'], poi['Text4']]

        if includeFirstLine:
            lines = [poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']]

        while '' in lines:
            if lines[0] == '':
                lines.pop(0)
            elif lines[-1] == '':
                lines.pop(-1)
            else:
                break
    else:
        lines = []

    hover = list(lines)
    hover.append("(" + ", ".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")")

    title_html = ''
    if title is not None:
        title_html = '<strong>' + title + '</strong><br />'
        hover.insert(0, title)

    coords = '(' + 'X: ' + str(poi['x']) + ', Y: ' + str(poi['y']) + ', Z: ' + str(poi['z']) + '</a>)'

    if lines:
        info_window_text = title_html + '<div class="signtext mccolor-' + poi['Color'] + ' mcglow-' + str(poi['GlowingText']) + '">' + "<br />".join(lines) + '</div><br />'  + ('' if note is None else note) + coords
    else:
        info_window_text = title_html + ('' if note is None else note) + coords

    return ("\n".join([x for x in hover if x]), info_window_text)


def fastlizardSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == "minecraft:sign":
        signLine = " ".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']]).strip().lower()

        public = "claim" in signLine or "deathpile" in signLine
        is_station = "north line" in signLine or "green line" in signLine or "east line" in signLine or "south line" in signLine or "purple line" in signLine

        if signLine == "":
            return None #Return nothing; sign is private
        elif is_station:
            return None # should be handled by train filter instead
        elif signLine[0] == '@':
            return formatSign(poi, "Public Sign", None, includeFirstLine=True)
        elif signLine[0] == '#':
            return None #Return nothing; sign is private
        elif public:
            return formatSign(poi, "Sign", None, includeFirstLine=True)
        else:
            return None #Return nothing; sign is private

def fastlizardHouseSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == "minecraft:sign":
        signLine = " ".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']]).strip().lower()

        public = "home" in signLine or "house" in signLine or "outpost" in signLine

        if signLine == "":
            return None #Return nothing; sign is private
        elif signLine[0] == '#':
            return None #Return nothing; sign is private
        elif public:
            return formatSign(poi, "Player House", None, includeFirstLine=True)
        else:
            return None #Return nothing; sign is private


def fastlizardFastTravelFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        sign_text = ' '.join([poi['Text1'],poi['Text2'],poi['Text3'],poi['Text4']])
        if sign_text[0] == '#':
            return None

        if 'fast travel' in sign_text.lower():
            poi['icon'] = 'custom-icons/transport/marker_fasttravel.png'
            return formatSign(poi, "Fast Travel", None, includeFirstLine=True)

def fastlizardTransportSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        signLine = " ".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']]).strip().lower()

        is_station = "north line" in signLine or "green line" in signLine or "east line" in signLine or "south line" in signLine or "purple line" in signLine

        if signLine[0] == '@' and is_station:
            poi['icon'] = "custom-icons/transport/marker_train.png"

            return formatSign(poi, "Minecart Station", None, includeFirstLine=True)

def generatedStructureFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Spawner]" == poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_spawner.png"
            return formatSign(poi, "Monster Spawner", None)
        if "[Witch Hut]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_witch.png"
            return formatSign(poi, "Witch Hut", None)
        if "[Temple]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_temple.png"
            return formatSign(poi, "Desert / Jungle Temple", None)
        if "[Stronghold]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_stronghold.png"
            return formatSign(poi, "Stronghold", None)
        if "[Shipwreck]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_shipwreck.png"
            return formatSign(poi, "Shipwreck", None)
        if "[Mansion]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_mansion.png"
            return formatSign(poi, "Woodland Mansion", None)
        if "[Monument]" in poi['Text1'] or "[Ocean Monument]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_monument.png"
            return formatSign(poi, "Ocean Monument", None)
        if "[Ruins]" in poi['Text1'] or "[Ruin]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_ruins.png"
            return formatSign(poi, "Underwater Ruins", None)
        if "[Igloo]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_igloo.png"
            return formatSign(poi, "Igloo", None)
        if "[Illager]" in poi['Text1'] or "[Pillager]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_illager.png"
            return formatSign(poi, "Illager Outpost", None)
        if "[Ruined Portal]" in poi['Text1'] or "[Pillager]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_ruinedportal.png"
            return formatSign(poi, "Ruined Portal", None)
        if "[Fortress]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_fortress.png"
            return formatSign(poi, "Nether Fortress", None)
        if "[Bastion]" in poi['Text1'] or "[Bastion Remnant]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_bastion.png"
            return formatSign(poi, "Bastion Remnant", None)
        if "[End City]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_endcity.png"
            return formatSign(poi, "End City", None)


# region houseSign

def houseSignNether(poi):
    return houseSignFilter(poi, False)


def houseSignRoof(poi):
    return houseSignFilter(poi, True)


def houseSignFilter(poi, roof=None):
    if roof is True and poi['y'] < 127:
        return None
    if roof is False and poi['y'] > 127:
        return None

    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[House]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_house.png"
            return formatSign(poi, None, None)
        if "[Hut]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_hut.png"
            return formatSign(poi, "Hut", None)
        if "[Mine]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_mines.png"
            return formatSign(poi, "Mine", None)
        if "[Minecamp]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_hut.png"
            return formatSign(poi, None, '<em>Deprecated tag, please replace with [Hut].</em>')


# endregion

def townSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Town]" in poi['Text1']:
            return formatSign(poi, "Town", None)

# region portalSign

def portalSignNether(poi):
    return portalSignFilter(poi, False)


def portalSignRoof(poi):
    return portalSignFilter(poi, True)


def portalSignFilter(poi, roof=None):
    if roof is True and poi['y'] < 127:
        return None
    if roof is False and poi['y'] > 127:
        return None

    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Portal]" in poi['Text1']:
            return formatSign(poi, None, None)
    if poi['id'] == 'minecraft:end_gateway':
        poi['icon'] = "custom-icons/transport/marker_endportal.png"
        return formatSign(poi, "End Gateway", None)


def endFilter(poi):
    if poi['id'] == 'minecraft:chest':
        poi['icon'] = "custom-icons/structures/marker_endcity.png"
        return formatSign(poi, "CHEST", None)

# endregion

# region poiSign
def pointOfInterestSignNether(poi):
    return pointOfInterestSignFilter(poi, False)


def pointOfInterestSignRoof(poi):
    return pointOfInterestSignFilter(poi, True)


def pointOfInterestSignFilter(poi, roof=None):
    if roof is True and poi['y'] < 127:
        return None
    if roof is False and poi['y'] > 127:
        return None

    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[POI]" in poi['Text1']:
            return formatSign(poi, None, None)
        if "[Villager Trading]" in poi['Text1']:
            poi['icon'] = "custom-icons/misc/marker_tradinghall.png"
            return formatSign(poi, "Villager Trading Hall", None)
        if "[Chest]" in poi['Text1']:
            poi['icon'] = "custom-icons/misc/marker_chest.png"
            return formatSign(poi, "Chest", None)


# endregion

# region transport

def transportSignNether(poi):
    return transportSignFilter(poi, False)


def transportSignRoof(poi):
    return transportSignFilter(poi, True)


def transportSignFilter(poi, roof=None):
    if roof is True and poi['y'] < 127:
        return None
    if roof is False and poi['y'] > 127:
        return None

    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Station]" in poi['Text1'] or "[NFT]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_train.png"
            return formatSign(poi, "Minecart Station", None)
        if "[Dock]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_dock.png"
            return formatSign(poi, "Dock", None)
        if "[Canal]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_canal.png"
            return formatSign(poi, "Canal", None)
        if "[Stable]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_stable.png"
            return formatSign(poi, "Horse Stable", None)


# endregion

# region fastTravel

def fastTravelSignNether(poi):
    return fastTravelSignFilter(poi, False)


def fastTravelSignRoof(poi):
    return fastTravelSignFilter(poi, True)


def fastTravelSignFilter(poi, roof=None):
    if roof is True and poi['y'] < 127:
        return None
    if roof is False and poi['y'] > 127:
        return None

    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Fast Travel" in poi['Text1']:
            return formatSign(poi, None, None)


# endregion

# region farm
def farmSignNether(poi):
    return farmSignFilter(poi, False)


def farmSignRoof(poi):
    return farmSignFilter(poi, True)


def farmSignFilter(poi, roof=None):
    if roof is True and poi['y'] < 127:
        return None
    if roof is False and poi['y'] > 127:
        return None

    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Farm]" in poi['Text1']:
            return formatSign(poi, "Farm", None)
        if "[Enclosure]" in poi['Text1'] or "[Field]" in poi['Text1'] or "[Arboretum]" in poi['Text1']:
            return formatSign(poi, None, '<em>Deprecated tag, please replace with [Farm].</em>')


# endregion

# region ender chest
def enderchestNether(poi):
    return enderchestFilter(poi, False)


def enderchestRoof(poi):
    return enderchestFilter(poi, True)


def enderchestFilter(poi, roof=None):
    if roof is True and poi['y'] < 127:
        return None
    if roof is False and poi['y'] > 127:
        return None

    if poi['id'] == 'minecraft:ender_chest':
        return formatSign(poi, "Ender Chest", None)


# end region
