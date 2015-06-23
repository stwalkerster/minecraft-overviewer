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

def witchHutSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Witch Hut" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], str(poi['x']), str(poi['y']), str(poi['z'])])

def templeSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Temple" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], str(poi['x']), str(poi['y']), str(poi['z'])])

def houseSignFilter(poi):
    if poi['id'] == 'Sign':
        if "House" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], str(poi['x']), str(poi['y']), str(poi['z'])])

def townSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Town" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], str(poi['x']), str(poi['y']), str(poi['z'])])

def portalSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Portal" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], str(poi['x']), str(poi['y']), str(poi['z'])])

def pointOfInterestSignFilter(poi):
    if poi['id'] == 'Sign':
        if "POI" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], str(poi['x']), str(poi['y']), str(poi['z'])])
            
def trainSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Station" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], str(poi['x']), str(poi['y']), str(poi['z'])])
            
def dockSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Dock" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], str(poi['x']), str(poi['y']), str(poi['z'])])
			
def canalSignFilter(poi):
    if poi['id'] == 'Sign':
        if "Canal" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], str(poi['x']), str(poi['y']), str(poi['z'])])

			
def netherFastTransportSignFilter(poi):
    if poi['id'] == 'Sign':
        if "NFT" in poi['Text1']:
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4'], str(poi['x']), str(poi['y']), str(poi['z'])])

outputdir = "maps"
customwebassets = "assets"
processes = 2
			
from observer import JSObserver
observer = JSObserver(outputdir=outputdir, minrefresh=10)

<?php

$worlds = array(
    "crew" => array(
		'path' => "worlds/minecraft/crew/world/",
		'title' => "HW Events Crew",
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
			/*array(
				"name"           => "Manual Town",
				"filterFunction" => "townFilter",
				"icon"           => "../marker_town.png",
			),*/
			array(
				"name"           => "Witch Huts",
				"filterFunction" => "witchHutSignFilter",
				"icon"           => "../marker_witch.png",
			),
			array(
				"name"           => "Temples",
				"filterFunction" => "templeSignFilter",
				"icon"           => "../marker_temple.png",
			),
			array(
				"name"           => "Houses",
				"filterFunction" => "houseSignFilter",
				"icon"           => "../marker_house.png",
                "checked"        => "true",
			),
			array(
				"name"           => "Towns",
				"filterFunction" => "townSignFilter",
				"icon"           => "../marker_town.png",
                "checked"        => "true",
			),
			array(
				"name"           => "Portals",
				"filterFunction" => "portalSignFilter",
				"icon"           => "../marker_portal.png",
                "checked"        => "true",
			),
			array(
				"name"           => "Points of Interest",
				"filterFunction" => "pointOfInterestSignFilter",
				"icon"           => "../treasure-mark.png",
                "checked"        => "true",
			),/*
			array(
				"name"           => "Minecart Station",
				"filterFunction" => "trainSignFilter",
				"icon"           => "../marker-train.png",
                "checked"        => "true",
			),
			array(
				"name"           => "Dock",
				"filterFunction" => "dockSignFilter",
				"icon"           => "../harbor.png",
			),
			array(
				"name"           => "Canal",
				"filterFunction" => "canalSignFilter",
				"icon"           => "../taxiboat.png",
                "checked"        => "true",
			),
			array(
				"name"           => "Nether Fast Transport",
				"filterFunction" => "netherFastTransportSignFilter",
				"icon"           => "../underground.png",
                "checked"        => "true",
			),*/
		), // markers
	), // crew
	"cowgate" => array(
		'path' => "worlds/minecraft/cowgate/cowgate/",
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
				"icon"           => "../marker_witch.png",
			),
			array(
				"name"           => "Temples",
				"filterFunction" => "templeSignFilter",
				"icon"           => "../marker_temple.png",
			),
			array(
				"name"           => "Underbelly",
				"filterFunction" => "underbellyFilter",
				"icon"           => "../marker_ub.png",
			),
			array(
				"name"           => "Houses",
				"filterFunction" => "houseSignFilter",
				"icon"           => "../marker_house.png",
                "checked"        => "true",
			),
			array(
				"name"           => "Towns",
				"filterFunction" => "townSignFilter",
				"icon"           => "../marker_town.png",
                "checked"        => "true",
			),
			array(
				"name"           => "Portals",
				"filterFunction" => "portalSignFilter",
				"icon"           => "../marker_portal.png",
                "checked"        => "true",
			),
			array(
				"name"           => "Points of Interest",
				"filterFunction" => "pointOfInterestSignFilter",
				"icon"           => "../treasure-mark.png",
                "checked"        => "true",
			),
			array(
				"name"           => "Minecart Station",
				"filterFunction" => "trainSignFilter",
				"icon"           => "../marker-train.png",
                "checked"        => "true",
			),
			array(
				"name"           => "Dock",
				"filterFunction" => "dockSignFilter",
				"icon"           => "../harbor.png",
			),
			array(
				"name"           => "Canal",
				"filterFunction" => "canalSignFilter",
				"icon"           => "../taxiboat.png",
                "checked"        => "true",
			),
			array(
				"name"           => "Nether Fast Transport",
				"filterFunction" => "netherFastTransportSignFilter",
				"icon"           => "../underground.png",
                "checked"        => "true",
			),
		), // markers
	), // cowgate
	"creative" => array(
		'path' => "worlds/minecraft/creative/world/",
		'title' => "Creative",
		'renderchecks' => 3,
		'overworld' => true,
		'nether' => false,
		'end' => false,
	),
	"ohai" => array(
		'path' => "worlds/minecraft/ohai/world/",
		'title' => "Ohai!",
		'renderchecks' => 3,
		'overworld' => true,
		'nether' => false,
		'end' => false,
	),
	"mc1.5" => array(
		'path' => "worlds/minecraft/mc1.5/world/",
		'title' => "MC 1.5",
		'renderchecks' => 3,
		'overworld' => true,
		'nether' => true,
		'end' => false,
	),
	"mc1" => array(
		'path' => "mc1-world/",
		'title' => "MC 1",
		'renderchecks' => 3,
		'overworld' => true,
		'nether' => true,
		'end' => true,
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
		'rendermode' => 'nether',
		'dimension' => 'nether',
	),
	"end" => array(
		'title' => 'The End',
		'rendermode' => 'smooth_lighting',
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
			
		echo 'renders["' . $worldname . '-' . $directionname . '-spawn"] = {' . "\r\n";
		echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
		echo "\t" . '"title": "Monster Spawn",' . "\r\n";
		echo "\t" . '"rendermode": [ClearBase(), SpawnOverlay()],' . "\r\n";
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
			
		echo 'renders["' . $worldname . '-' . $directionname . '-horse"] = {' . "\r\n";
		echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
		echo "\t" . '"title": "Horse Spawn",' . "\r\n";
		echo "\t" . '"rendermode": [ClearBase(), BiomeOverlay(biomes=[("Plains", (0, 255, 0))])],' . "\r\n";
		echo "\t" . '"dimension": "overworld",' . "\r\n";
		echo "\t" . '"overlay": ["' . $worldname . '-overworld-day-' . $directionname . '"],' . "\r\n";
		echo "\t" . '"northdirection": "' . $direction['code'] . '",' . "\r\n";
		echo "\t" . '"renderchecks": "' . $world['renderchecks'] . '",' . "\r\n";
        markerGeneration($world, "overworld");
		echo "}\r\n\r\n";
			
		echo 'renders["' . $worldname . '-' . $directionname . '-ocelot"] = {' . "\r\n";
		echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
		echo "\t" . '"title": "Ocelot Spawn",' . "\r\n";
		echo "\t" . '"rendermode": [ClearBase(), BiomeOverlay(biomes=[("Jungle", (0, 255, 0))])],' . "\r\n";
		echo "\t" . '"dimension": "overworld",' . "\r\n";
		echo "\t" . '"overlay": ["' . $worldname . '-overworld-day-' . $directionname . '"],' . "\r\n";
		echo "\t" . '"northdirection": "' . $direction['code'] . '",' . "\r\n";
		echo "\t" . '"renderchecks": "' . $world['renderchecks'] . '",' . "\r\n";
        markerGeneration($world, "overworld");
		echo "}\r\n\r\n";
			
		echo 'renders["' . $worldname . '-' . $directionname . '-wolf"] = {' . "\r\n";
		echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
		echo "\t" . '"title": "Wolf Spawn",' . "\r\n";
		echo "\t" . '"rendermode": [ClearBase(), BiomeOverlay(biomes=[("Forest", (0, 255, 0)), ("Taiga", (0, 255, 0))])],' . "\r\n";
		echo "\t" . '"dimension": "overworld",' . "\r\n";
		echo "\t" . '"overlay": ["' . $worldname . '-overworld-day-' . $directionname . '"],' . "\r\n";
		echo "\t" . '"northdirection": "' . $direction['code'] . '",' . "\r\n";
		echo "\t" . '"renderchecks": "' . $world['renderchecks'] . '",' . "\r\n";
        markerGeneration($world, "overworld");
		echo "}\r\n\r\n";
	}
}



