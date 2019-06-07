def underbellyFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Underbelly" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def spawnerFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Spawner" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def witchHutSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Witch Hut" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def templeSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Temple" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def houseSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "House" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def townSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Town" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def portalSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Portal" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def pointOfInterestSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "POI" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def trainSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Station" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def dockSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Dock" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def canalSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Canal" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def netherFastTransportSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "NFT" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def mineSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "[Mine]" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def mineshaftSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Mineshaft" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def enclosureSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Enclosure" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def fieldSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Field" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def fortressSignFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Fortress" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def hutFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Hut" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def strongholdFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Stronghold" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def shipwreckFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Shipwreck" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def mansionFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Mansion" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def monumentFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Monument" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def ruinsFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Ruins" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def minecampFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Minecamp" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def arboretaFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Arboretum" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def iglooFilter(poi):
    if poi['id'] == 'Sign' or poi['id'] == 'minecraft:sign':
        if "Igloo" in poi['Text1']:
            return "\n".join([poi['Text1'], "", poi['Text2'], poi['Text3'], poi['Text4'], "(" + ",".join([str(poi['x']), str(poi['y']), str(poi['z'])]) + ")"])

def playerFilter(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "http://cravatar.eu/helmavatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']

outputdir = "maps-pillage"
customwebassets = "assets"
processes = 2

from observer import JSObserver,ServerAnnounceObserver,MultiplexingObserver
observer = MultiplexingObserver(JSObserver(outputdir=outputdir, minrefresh=10))

<?php

$worlds = array(
	"pillage" => array(
		'path' => "worlds/pillage/world",
		'title' => "Village+Pillage",
		'renderchecks' => 0,
		'overworld' => true,
		'nether' => false,
		'end' => false,
		'manualpois' => array(
[ 'x'=>1253, 'y'=>64 , 'z'=>1377, 'Text1'=>'[POI]', 'Text2'=>'Witch hut', 'Text3'=>'', 'Text4'=>'', 'id'=>'minecraft:sign' ],
[ 'x'=>1742, 'y'=>64 , 'z'=>776, 'Text1'=>'[POI]', 'Text2'=>'Temple', 'Text3'=>'', 'Text4'=>'', 'id'=>'minecraft:sign' ],
[ 'x'=>1829, 'y'=>64 , 'z'=>2038, 'Text1'=>'[POI]', 'Text2'=>'Town', 'Text3'=>'', 'Text4'=>'', 'id'=>'minecraft:sign' ],
[ 'x'=>2341, 'y'=>64 , 'z'=>1700, 'Text1'=>'[POI]', 'Text2'=>'Town', 'Text3'=>'', 'Text4'=>'', 'id'=>'minecraft:sign' ],
[ 'x'=>2783, 'y'=>64 , 'z'=>1078, 'Text1'=>'[POI]', 'Text2'=>'Town', 'Text3'=>'', 'Text4'=>'', 'id'=>'minecraft:sign' ],
[ 'x'=>3147, 'y'=>64 , 'z'=>2320, 'Text1'=>'[POI]', 'Text2'=>'Illager outpost', 'Text3'=>'', 'Text4'=>'', 'id'=>'minecraft:sign' ],
[ 'x'=>3133, 'y'=>64 , 'z'=>1017, 'Text1'=>'[POI]', 'Text2'=>'Town', 'Text3'=>'', 'Text4'=>'', 'id'=>'minecraft:sign' ],
[ 'x'=>3234, 'y'=>64 , 'z'=>669, 'Text1'=>'[POI]', 'Text2'=>'Odd town', 'Text3'=>'', 'Text4'=>'', 'id'=>'minecraft:sign' ],
		),
		"markers" => array(
			array(
				"name"           => "Witch Huts",
				"filterFunction" => "witchHutSignFilter",
				"icon"           => "custom-icons/marker_witch.png",
			),
			array(
				"name"           => "Temples",
				"filterFunction" => "templeSignFilter",
				"icon"           => "custom-icons/temple-2.png",
			),
			array(
				"name"           => "Houses",
				"filterFunction" => "houseSignFilter",
				"icon"           => "custom-icons/marker_house.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Towns",
				"filterFunction" => "townSignFilter",
				"icon"           => "custom-icons/marker_town.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Portals",
				"filterFunction" => "portalSignFilter",
				"icon"           => "custom-icons/marker_portal.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Points of Interest",
				"filterFunction" => "pointOfInterestSignFilter",
				"icon"           => "custom-icons/treasure-mark.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Minecart Station",
				"filterFunction" => "trainSignFilter",
				"icon"           => "custom-icons/marker-train.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Dock",
				"filterFunction" => "dockSignFilter",
				"icon"           => "custom-icons/harbor.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Canal",
				"filterFunction" => "canalSignFilter",
				"icon"           => "custom-icons/taxiboat.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Spawners",
				"filterFunction" => "spawnerFilter",
				"icon"           => "custom-icons/zombie-outbreak1.png",
				"checked"        => "false",
			),
			array(
				"name"           => "Mines",
				"filterFunction" => "mineSignFilter",
				"icon"           => "custom-icons/construction.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Abandoned Mineshafts",
				"filterFunction" => "mineshaftSignFilter",
				"icon"           => "custom-icons/mine.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Mining camps",
				"filterFunction" => "minecampFilter",
				"icon"           => "custom-icons/tents.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Farming: Fields",
				"filterFunction" => "fieldSignFilter",
				"icon"           => "custom-icons/field.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Farming: Enclosures",
				"filterFunction" => "enclosureSignFilter",
				"icon"           => "custom-icons/enclosure.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Huts",
				"filterFunction" => "hutFilter",
				"icon"           => "custom-icons/bunker-2-2.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Strongholds",
				"filterFunction" => "strongholdFilter",
				"icon"           => "custom-icons/citywalls.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Shipwrecks",
				"filterFunction" => "shipwreckFilter",
				"icon"           => "custom-icons/shipwreck.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Mansions",
				"filterFunction" => "mansionFilter",
				"icon"           => "custom-icons/hostel_0star.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Ocean Monuments",
				"filterFunction" => "monumentFilter",
				"icon"           => "custom-icons/arch.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Ruins",
				"filterFunction" => "ruinsFilter",
				"icon"           => "custom-icons/ruins-2.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Arboreta",
				"filterFunction" => "arboretaFilter",
				"icon"           => "custom-icons/forest2.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Players",
				"filterFunction" => "playerFilter",
				"checked"        => "true",
			),
		), // markers
		"netherMarkers" => array(
			array(
				"name"           => "Nether Fast Transport",
				"filterFunction" => "netherFastTransportSignFilter",
				"icon"           => "../icons/underground.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Points of Interest",
				"filterFunction" => "pointOfInterestSignFilter",
				"icon"           => "../icons/treasure-mark.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Houses",
				"filterFunction" => "houseSignFilter",
				"icon"           => "../icons/marker_house.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Portals",
				"filterFunction" => "portalSignFilter",
				"icon"           => "../icons/marker_portal.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Nether Fortresses",
				"filterFunction" => "fortressSignFilter",
				"icon"           => "../icons/castle-2.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Spawners",
				"filterFunction" => "spawnerFilter",
				"icon"           => "../icons/zombie-outbreak1.png",
				"checked"        => "false",
			),
			array(
				"name"           => "Huts",
				"filterFunction" => "hutFilter",
				"icon"           => "../icons/bunker-2-2.png",
				"checked"        => "true",
			),
		), // netherMarkers
	), // combatupdate
); // worlds

if(getenv('forcerender') == 'true')
{
	foreach($worlds as $key => $world)
	{
		if($world['rendermode'] != 3)
		{
			$world['rendermode'] = 2;
		}
	}
}

$renders = array(
	// DAY is required!
	"day" => array(
		'title' => 'Day',
		'rendermode' => 'smooth_lighting',
		'dimension' => 'overworld',
	),
	"night" => array(
		'title' => 'Night',
		'rendermode' => 'smooth_night',
		'dimension' => 'overworld',
	),
	"nether" => array(
		'title' => 'Nether',
		'rendermode' => 'nether_smooth_lighting',
		'dimension' => 'nether',
	),
	"nether-unlit" => array(
		'title' => 'Nether (no lighting)',
		'rendermode' => 'nether',
		'dimension' => 'nether',
	),
	"end" => array(
		'title' => 'The End',
		'rendermode' => 'normal',
		'dimension' => 'end',
	),
);

$directions = array(
	// NORTH is required!
	"north" => array(
		"code" => "upper-left",
		"title" => "North",
	),
	"south" => array(
		"code" => "lower-right",
		"title" => "South",
	),
	"east" => array(
		"code" => "upper-right",
		"title" => "East",
	),
	"west" => array(
		"code" => "lower-left",
		"title" => "West",
	),
);

// END OF CONFIGURATION

// World Declarations
foreach( $worlds as $name => $data )
{
	echo 'worlds["' . $data['title'] . '"] = "' . $data['path'] . '"' . "\r\n";
}

echo "\r\n";

function markerGeneration($world, $dimension)
{
    if( $dimension == "overworld" && isset( $world['manualpois' ] ) && is_array( $world[ 'manualpois' ] ) )
    {
        echo "\t" . '"manualpois": [' . "\r\n";
        foreach( $world[ 'manualpois' ] as $poi )
        {
            echo "\t\t{\r\n";
            foreach( $poi as $poikey => $poivalue )
            {
                echo "\t\t\t'" . $poikey . "' : " . ( is_numeric( $poivalue ) ? $poivalue : "'" . $poivalue . "'" ) . ",\r\n";
            }
            echo "\t\t},\r\n";
        }
        echo "\t" . '],' . "\r\n";
        echo "\t'markers' : [\r\n";
        foreach( $world[ "markers" ] as $marker )
        {
            echo "\t\tdict(name=\"" . $marker[ "name" ] . "\", filterFunction=" . $marker[ "filterFunction" ];
            if( isset( $marker[ 'icon' ] ) )
            {
                echo ", icon=\"" . $marker[ "icon" ] . "\"";
            }
            if( isset( $marker[ 'checked' ] ) )
            {
                echo ", checked=\"" . $marker[ "checked" ] . "\"";
            }
            echo "),\r\n";
        }
        echo "\t],\r\n";
    }

    if( $dimension == "nether" && isset( $world['netherMarkers' ] ) && is_array( $world[ 'netherMarkers' ] ) )
    {
        echo "\t'markers' : [\r\n";
        foreach( $world[ "netherMarkers" ] as $marker )
        {
            echo "\t\tdict(name=\"" . $marker[ "name" ] . "\", filterFunction=" . $marker[ "filterFunction" ];
            if( isset( $marker[ 'icon' ] ) )
            {
                echo ", icon=\"" . $marker[ "icon" ] . "\"";
            }
            if( isset( $marker[ 'checked' ] ) )
            {
                echo ", checked=\"" . $marker[ "checked" ] . "\"";
            }
            echo "),\r\n";
        }
        echo "\t],\r\n";
    }
}

// Render Declarations
foreach( $worlds as $worldname => $world )
{
	foreach( $directions as $directionname => $direction )
	{
		foreach( $renders as $mapname => $map )
		{
			if( $world[ $map[ 'dimension' ] ] )
			{
				echo 'renders["' . $worldname . '-' . $map['dimension'] . '-' . $mapname . '-' . $directionname . '"] = {' . "\r\n";
				echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
				echo "\t" . '"title": "' . $map['title'] . ' - ' . $direction['title'] . '",' . "\r\n";
				echo "\t" . '"rendermode": "' . $map['rendermode'] . '",' . "\r\n";
				echo "\t" . '"dimension": "' . $map['dimension'] . '",' . "\r\n";
				echo "\t" . '"northdirection": "' . $direction['code'] . '",' . "\r\n";
				echo "\t" . '"renderchecks": "' . $world['renderchecks'] . '",' . "\r\n";
				markerGeneration($world, $map[ 'dimension' ]);
				echo "}\r\n\r\n";
			}
		}

		echo 'renders["' . $worldname . '-' . $directionname . '-biome"] = {' . "\r\n";
		echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
		echo "\t" . '"title": "Biomes (' . $directionname . ')",' . "\r\n";
		echo "\t" . '"rendermode": [ClearBase(), BiomeOverlay()],' . "\r\n";
		echo "\t" . '"dimension": "overworld",' . "\r\n";
		echo "\t" . '"overlay": ["' . $worldname . '-overworld-day-' . $directionname . '"],' . "\r\n";
		echo "\t" . '"northdirection": "' . $direction['code'] . '",' . "\r\n";
		echo "\t" . '"renderchecks": "' . $world['renderchecks'] . '",' . "\r\n";
        markerGeneration($world, "overworld");
		echo "}\r\n\r\n";

		echo 'renders["' . $worldname . '-' . $directionname . '-slime"] = {' . "\r\n";
		echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
		echo "\t" . '"title": "Slime Spawn",' . "\r\n";
		echo "\t" . '"rendermode": [ClearBase(), SlimeOverlay()],' . "\r\n";
		echo "\t" . '"dimension": "overworld",' . "\r\n";
		echo "\t" . '"overlay": ["' . $worldname . '-overworld-day-' . $directionname . '"],' . "\r\n";
		echo "\t" . '"northdirection": "' . $direction['code'] . '",' . "\r\n";
		echo "\t" . '"renderchecks": "' . $world['renderchecks'] . '",' . "\r\n";
        markerGeneration($world, "overworld");
		echo "}\r\n\r\n";
	}
}
