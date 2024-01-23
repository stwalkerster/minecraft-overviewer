import os


def overworld_marker_definitions():
    markers = [
        dict(name="Signs", filterFunction=fastlizardSignFilter, checked="true", icon="signpost_icon.png", showIconInLegend="true"),
        dict(name="Player bases", filterFunction=fastlizardHouseSignFilter, icon="custom-icons/player/marker_house.png", checked="true", showIconInLegend="true"),
        dict(name="Fast Travel", filterFunction=fastlizardFastTravelFilter, icon="custom-icons/transport/marker_fasttravel.png", checked="true", showIconInLegend="true"),
        dict(name="Transport", filterFunction=fastlizardTransportSignFilter, icon="custom-icons/transport/marker_train.png", checked="true", showIconInLegend="true"),
    ]

    return markers


def nether_marker_definitions():
    return [
        dict(name="Signs", filterFunction=fastlizardSignFilter, checked="true", icon="signpost_icon.png", showIconInLegend="true"),
        dict(name="Player bases", filterFunction=fastlizardHouseSignFilter, icon="custom-icons/player/marker_house.png", checked="true", showIconInLegend="true"),
    ]


def nether_roof_marker_definitions():
    return [
        dict(name="Signs", filterFunction=fastlizardSignFilter, checked="true", icon="signpost_icon.png", showIconInLegend="true"),
    ]


def end_marker_definitions():
    return [
        dict(name="Portals", filterFunction=portalSignFilter, icon="custom-icons/transport/marker_endportal.png", checked="true", showIconInLegend="true"),
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

        if 'fast travel' in sign_text.lower() or 'faster travelling' in sign_text.lower():
            poi['icon'] = 'custom-icons/transport/marker_fasttravel.png'
            return formatSign(poi, "Fast Travel", None, includeFirstLine=True)

def fastlizardTransportSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        signLine = " ".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']]).strip().lower()

        is_station = "north line" in signLine or "green line" in signLine or "east line" in signLine or "south line" in signLine or "purple line" in signLine

        if signLine == "":
            return None # Sign is empty
        elif signLine[0] == '@' and is_station:
            poi['icon'] = "custom-icons/transport/marker_train.png"

            return formatSign(poi, "Minecart Station", None, includeFirstLine=True)


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

