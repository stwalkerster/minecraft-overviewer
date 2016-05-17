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

outputdir = "maps"
customwebassets = "assets"
processes = 2
			
from observer import JSObserver
observer = JSObserver(outputdir=outputdir, minrefresh=10)

<?php

$worlds = array(
	"combatupdate" => array(
		'path' => "worlds/combatupdate/world/",
		'title' => "Combat Update",
		'renderchecks' => 0,
		'overworld' => true,
		'nether' => true,
		'end' => false,
		'manualpois' => array(),
		"markers" => array(
			array(
				"name"           => "Witch Huts",
				"filterFunction" => "witchHutSignFilter",
				"icon"           => "../icons/marker_witch.png",
			),
			array(
				"name"           => "Temples",
				"filterFunction" => "templeSignFilter",
				"icon"           => "../icons/temple-2.png",
			),
			array(
				"name"           => "Houses",
				"filterFunction" => "houseSignFilter",
				"icon"           => "../icons/marker_house.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Towns",
				"filterFunction" => "townSignFilter",
				"icon"           => "../icons/marker_town.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Portals",
				"filterFunction" => "portalSignFilter",
				"icon"           => "../icons/marker_portal.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Points of Interest",
				"filterFunction" => "pointOfInterestSignFilter",
				"icon"           => "../icons/treasure-mark.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Minecart Station",
				"filterFunction" => "trainSignFilter",
				"icon"           => "../icons/marker-train.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Dock",
				"filterFunction" => "dockSignFilter",
				"icon"           => "../icons/harbor.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Canal",
				"filterFunction" => "canalSignFilter",
				"icon"           => "../icons/taxiboat.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Spawners",
				"filterFunction" => "spawnerFilter",
				"icon"           => "../icons/zombie-outbreak1.png",
				"checked"        => "false",
			),
			array(
				"name"           => "Mines",
				"filterFunction" => "mineSignFilter",
				"icon"           => "../icons/mine.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Farming: Fields",
				"filterFunction" => "fieldSignFilter",
				"icon"           => "../icons/field.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Farming: Enclosures",
				"filterFunction" => "enclosureSignFilter",
				"icon"           => "../icons/enclosure.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Huts",
				"filterFunction" => "hutFilter",
				"icon"           => "../icons/bunker-2-2.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Igloos",
				"filterFunction" => "iglooFilter",
				"icon"           => "../icons/bunker.png",
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
	"cowgate" => array(
		'path' => "worlds/cowgate/cowgate/",
		'title' => "Underbelly Cowgate",
		'renderchecks' => 0,
		'overworld' => true,
		'nether' => true,
		'end' => false,
		'manualpois' => array(
			/*array(
				'id'   => 'Town',
				'x'    => 815,
				'y'    => 70,
				'z'    => -891,
				'name' => 'Plains Town 2'
			),*/
		), // manualpoi
		"markers" => array(
			array(
				"name"           => "Witch Huts",
				"filterFunction" => "witchHutSignFilter",
				"checked"        => "true",
				"icon"           => "../icons/marker_witch.png",
			),
			array(
				"name"           => "Temples",
				"filterFunction" => "templeSignFilter",
				"icon"           => "../icons/temple-2.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Underbelly",
				"filterFunction" => "underbellyFilter",
				"icon"           => "../icons/marker_ub.png",
			),
			array(
				"name"           => "Houses",
				"filterFunction" => "houseSignFilter",
				"icon"           => "../icons/marker_house.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Towns",
				"filterFunction" => "townSignFilter",
				"icon"           => "../icons/marker_town.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Portals",
				"filterFunction" => "portalSignFilter",
				"icon"           => "../icons/marker_portal.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Points of Interest",
				"filterFunction" => "pointOfInterestSignFilter",
				"icon"           => "../icons/treasure-mark.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Minecart Station",
				"filterFunction" => "trainSignFilter",
				"icon"           => "../icons/marker-train.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Dock",
				"filterFunction" => "dockSignFilter",
				"icon"           => "../icons/harbor.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Canal",
				"filterFunction" => "canalSignFilter",
				"icon"           => "../icons/taxiboat.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Spawners",
				"filterFunction" => "spawnerFilter",
				"icon"           => "../icons/zombie-outbreak1.png",
				"checked"        => "false",
			),
			array(
				"name"           => "Mines",
				"filterFunction" => "mineSignFilter",
				"icon"           => "../icons/mine.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Farming: Fields",
				"filterFunction" => "fieldSignFilter",
				"icon"           => "../icons/field.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Farming: Enclosures",
				"filterFunction" => "enclosureSignFilter",
				"icon"           => "../icons/enclosure.png",
				"checked"        => "true",
			),
			array(
				"name"           => "Huts",
				"filterFunction" => "hutFilter",
				"icon"           => "../icons/bunker-2-2.png",
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
	), // cowgate
	"creative" => array(
		'path' => "worlds/creative/world/",
		'title' => "Creative",
		'renderchecks' => 3,
		'overworld' => true,
		'nether' => false,
		'end' => false,
		'markers' => array(
			array(
				"name"           => "Players",
				"filterFunction" => "playerFilter",
				"checked"        => "true",
			),
		),
	),
	"ohai" => array(
		'path' => "worlds/ohai/world/",
		'title' => "Ohai!",
		'renderchecks' => 3,
		'overworld' => true,
		'nether' => false,
		'end' => false,
		'markers' => array(
			array(
				"name"           => "Players",
				"filterFunction" => "playerFilter",
				"checked"        => "true",
			),
		),
	),
	"mc1.5" => array(
		'path' => "worlds/mc1.5/world/",
		'title' => "MC 1.5",
		'renderchecks' => 3,
		'overworld' => true,
		'nether' => true,
		'end' => false,
		'markers' => array(
			array(
				"name"           => "Players",
				"filterFunction" => "playerFilter",
				"checked"        => "true",
			),
		),
	),
	"mc1" => array(
		'path' => "mc1-world/",
		'title' => "MC 1",
		'renderchecks' => 3,
		'overworld' => true,
		'nether' => true,
		'end' => true,
		'markers' => array(
			array(
				"name"           => "Players",
				"filterFunction" => "playerFilter",
				"checked"        => "true",
			),
		),
	),
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
		echo "\t" . '"title": "Biomes",' . "\r\n";
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



