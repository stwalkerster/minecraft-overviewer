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
    if poi['id'] in ['minecraft:sign', 'minecraft:hanging_sign']:

        poi_type = 'hanging' if poi['id'] == 'minecraft:hanging_sign' else 'normal'

        front_lines = poi['front_text']['messages']
        back_lines = poi['back_text']['messages']

        if not includeFirstLine:
            front_lines = front_lines[1:]

        def trim_blank_lines(lines):
            while '' in lines:
                if lines[0] == '':
                    lines = lines[1:]
                elif lines[-1] == '':
                    lines = lines[:-1]
                else:
                    break
            return lines

        front_lines = trim_blank_lines(front_lines)
        back_lines = trim_blank_lines(back_lines)

    else:
        poi_type = 'none'
        front_lines = []
        back_lines = []

    hover = list(front_lines)
    hover.append("(" + ", ".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")")

    title_html = ''
    if title is not None:
        title_html = '<strong>' + title + '</strong><br />'
        hover.insert(0, title)

    info_window_text = title_html

    if front_lines:
        info_window_text += '<div class="signtext mcpoi-' + poi_type + ' mccolor-' + poi['front_text']['color'] + ' mcglow-' + str(poi['front_text']['has_glowing_text']) + '">' + "<br />".join(front_lines) + '</div><br />'
    if back_lines:
        info_window_text += '<div class="signtext mcpoi-' + poi_type + ' mccolor-' + poi['back_text']['color'] + ' mcglow-' + str(poi['back_text']['has_glowing_text']) + '">' + "<br />".join(back_lines) + '</div><br />'

    coords = '(' + 'X: ' + str(poi['x']) + ', Y: ' + str(poi['y']) + ', Z: ' + str(poi['z']) + ')'
    info_window_text +=  ('' if note is None else note) + coords

    return "\n".join([x for x in hover if x]), info_window_text


def globalSignFilter(poi):
    if poi['id'] in ['minecraft:sign', 'minecraft:hanging_sign']:
        return formatSign(poi, "Potato?", None, includeFirstLine=True)


def get_sign_text(poi):
    front = " ".join(poi['front_text']['messages']).strip().lower()
    back = " ".join(poi['back_text']['messages']).strip().lower()
    return front, back, front + " " + back


def sign_explicit_visibility(front, back, char):
    if len(front) > 0 and front[0] == char:
        return True

    if len(back) > 0 and back[0] == char:
        return True

    return False


def fastlizardSignFilter(poi):
    if poi['id'] in ['minecraft:sign', 'minecraft:hanging_sign']:
        front, back, all_text = get_sign_text(poi)
        sign_type = "Hanging Sign" if poi['id'] == 'minecraft:hanging_sign' else 'Sign'

        public = "claim" in all_text or "deathpile" in all_text

        is_station = ("north line" in all_text
                      or "green line" in all_text
                      or "east line" in all_text
                      or "south line" in all_text
                      or "purple line" in all_text)

        if all_text == "":
            return None  # Return nothing; sign is private
        elif is_station:
            return None  # should be handled by train filter instead
        elif sign_explicit_visibility(front, back, '#'):
            return None  # Return nothing; sign is private
        elif sign_explicit_visibility(front, back, '@'):
            return formatSign(poi, "Public " + sign_type, None, includeFirstLine=True)
        elif public:
            return formatSign(poi, sign_type, None, includeFirstLine=True)
        else:
            return None  # Return nothing; sign is private


def fastlizardHouseSignFilter(poi):
    if poi['id'] in ['minecraft:sign', 'minecraft:hanging_sign']:
        front, back, all_text = get_sign_text(poi)

        public = ("home" in all_text
                  or "house" in all_text
                  or "outpost" in all_text)

        if all_text == "":
            return None  # Return nothing; sign is private
        elif sign_explicit_visibility(front, back, '#'):
            return None  # Return nothing; sign is private
        elif public:
            return formatSign(poi, "Player House", None, includeFirstLine=True)
        else:
            return None  # Return nothing; sign is private


def fastlizardFastTravelFilter(poi):
    if poi['id'] in ['minecraft:sign', 'minecraft:hanging_sign']:
        front, back, all_text = get_sign_text(poi)

        public = ("fast travel" in all_text
                  or "faster travelling" in all_text)

        if all_text == "":
            return None  # Return nothing; sign is private
        elif sign_explicit_visibility(front, back, '#'):
            return None  # Return nothing; sign is private
        elif public:
            poi['icon'] = 'custom-icons/transport/marker_fasttravel.png'
            return formatSign(poi, "Fast Travel", None, includeFirstLine=True)
        else:
            return None  # Return nothing; sign is private


def fastlizardTransportSignFilter(poi):
    if poi['id'] in ['minecraft:sign', 'minecraft:hanging_sign']:
        front, back, all_text = get_sign_text(poi)

        is_station = ("north line" in all_text
                      or "green line" in all_text
                      or "east line" in all_text
                      or "south line" in all_text
                      or "purple line" in all_text)

        if all_text == "":
            return None  # Return nothing; sign is private
        elif sign_explicit_visibility(front, back, '#'):
            return None  # Return nothing; sign is private
        elif sign_explicit_visibility(front, back, '@') and is_station:
            poi['icon'] = "custom-icons/transport/marker_train.png"
            return formatSign(poi, "Minecart Station", None, includeFirstLine=True)
        else:
            return None  # Return nothing; sign is private


def portalSignFilter(poi, roof=None):
    if roof is True and poi['y'] < 127:
        return None
    if roof is False and poi['y'] > 127:
        return None

    if poi['id'] == 'minecraft:end_gateway':
        poi['icon'] = "custom-icons/transport/marker_endportal.png"
        return formatSign(poi, "End Gateway", None)

