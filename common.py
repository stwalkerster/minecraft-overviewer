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


def formatSign(poi, title, note):
    if poi['id'] == 'minecraft:sign':
        lines = [poi['Text2'], poi['Text3'], poi['Text4']]
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


def generatedStructureFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Spawner]" == poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_spawner.png"
            return formatSign(poi, None, None)
        if "[Witch Hut]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_witch.png"
            return formatSign(poi, None, None)
        if "[Temple]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_temple.png"
            return formatSign(poi, None, None)
        if "[Stronghold]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_stronghold.png"
            return formatSign(poi, None, None)
        if "[Shipwreck]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_shipwreck.png"
            return formatSign(poi, None, None)
        if "[Mansion]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_mansion.png"
            return formatSign(poi, None, None)
        if "[Monument]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_monument.png"
            return formatSign(poi, None, None)
        if "[Ruins]" in poi['Text1'] or "[Ruin]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_ruins.png"
            return formatSign(poi, None, None)
        if "[Igloo]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_igloo.png"
            return formatSign(poi, None, None)
        if "[Illager]" in poi['Text1'] or "[Pillager]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_illager.png"
            return formatSign(poi, None, None)
        if "[Ruined Portal]" in poi['Text1'] or "[Pillager]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_ruinedportal.png"
            return formatSign(poi, None, None)
        if "[Fortress]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_fortress.png"
            return formatSign(poi, None, None)
        if "[Bastion]" in poi['Text1'] or "[Bastion Remnant]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_bastion.png"
            return formatSign(poi, None, None)
        if "[End City]" in poi['Text1']:
            poi['icon'] = "custom-icons/structures/marker_endcity.png"
            return formatSign(poi, None, None)


def houseSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[House]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_house.png"
            return formatSign(poi, None, None)
        if "[Hut]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_hut.png"
            return formatSign(poi, None, None)
        if "[Mine]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_mines.png"
            return formatSign(poi, None, None)
        if "[Minecamp]" in poi['Text1']:
            poi['icon'] = "custom-icons/player/marker_hut.png"
            return formatSign(poi, None, '<em>Deprecated tag, please replace with [Hut].</em>')


def townSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Town]" in poi['Text1']:
            return formatSign(poi, None, None)


def portalSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Portal]" in poi['Text1']:
            return formatSign(poi, None, None)
    if poi['id'] == 'minecraft:end_gateway':
        poi['icon'] = "custom-icons/transport/marker_endportal.png"
        return formatSign(poi, "End Gateway", None)


def pointOfInterestSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[POI]" in poi['Text1']:
            return formatSign(poi, None, None)
        if "[Villager Trading]" in poi['Text1']:
            poi['icon'] = "custom-icons/misc/marker_tradinghall.png"
            return formatSign(poi, "Villager Trading Hall", None)


def transportSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Station]" in poi['Text1'] or "[NFT]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_train.png"
            return formatSign(poi, None, None)
        if "[Dock]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_dock.png"
            return formatSign(poi, None, None)
        if "[Canal]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_canal.png"
            return formatSign(poi, None, None)
        if "[Stable]" in poi['Text1']:
            poi['icon'] = "custom-icons/transport/marker_stable.png"
            return formatSign(poi, None, None)


def fastTravelSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Fast Travel" in poi['Text1']:
            return formatSign(poi, None, None)


def farmSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Farm]" in poi['Text1']:
            return formatSign(poi, None, None)
        if "[Enclosure]" in poi['Text1'] or "[Field]" in poi['Text1'] or "[Arboretum]" in poi['Text1']:
            return formatSign(poi, None, '<em>Deprecated tag, please replace with [Farm].</em>')


def enderchestFilter(poi):
    if poi['id'] == 'minecraft:ender_chest':
        return formatSign(poi, "Ender Chest", None)
