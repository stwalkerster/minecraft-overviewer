def townFilter(poi):
    if poi['id'] == 'Town':
        return poi['name']

def witchFilter(poi):
    if poi['id'] == 'Witch':
        return poi['name']

def horseFilter(poi):
    if poi['id'] == 'Horses':
        return poi['name']

def templeFilter(poi):
    if poi['id'] == 'Temple':
        return poi['name']

def underbellyFilter(poi):
    if poi['id'] == 'Underbelly':
        return poi['name']

<?php

$worlds = array(
	"cowgate" => array(
		'path' => "worlds/minecraft/cowgate/cowgate/",
		'title' => "Underbelly Cowgate",
		'overworld' => true,
		'nether' => true,
		'end' => false,
		'manualpois' => array(
			array(
				'id'   => 'Town',
				'x'    => 163,
				'y'    => 64,
				'z'    => 304,
				'name' => 'Ghost Town'
			),
			array(
				'id'   => 'Town',
				'x'    => 709,
				'y'    => 70,
				'z'    => 597,
				'name' =>'Desert Town 1'
			),
			array(
				'id'   => 'Town',
				'x'    => -136,
				'y'    => 85,
				'z'    => -194,
				'name' => 'Desert Town 2'
			),
			array(
				'id'   => 'Town',
				'x'    => 815,
				'y'    => 70,
				'z'    => -891,
				'name' => 'Plains Town 2'
			),
			array(
				'id'   => 'Witch',
				'x'    => 115,	
				'y'    => 64,
				'z'    => 1092,
				'name' => 'Witch Hut'
			),
			array(
				'id'   => 'Underbelly',
				'x'    => -38,
				'y'    => 64,
				'z'    => 381,
				'name' => 'Bottom of the Lane'
			),
			array(
				'id'   => 'Temple',
				'x'    => 323,
				'y'    => 64,
				'z'    => 865,
				'name' => 'Desert Temple'
			),
			array(
				'id'   => 'Temple',
				'x'    => 237,
				'y'    => 64,
				'z'    => -209,
				'name' => 'Jungle Temple'
			),
		), // manualpoi
		"markers" => array(
			array(
				"name"           => "Towns",
				"filterFunction" => "townFilter",
				"icon"           => "../marker_town.png",
			),
			array(
				"name"           => "Witch Huts",
				"filterFunction" => "witchFilter",
				"icon"           => "../marker_witch.png",
			),
			array(
				"name"           => "Temples",
				"filterFunction" => "templeFilter",
				"icon"           => "../marker_temple.png",
			),
			array(
				"name"           => "Underbelly",
				"filterFunction" => "underbellyFilter",
				"icon"           => "../marker_ub.png",
			),
		), // markers
	), // cowgate
	"creative" => array(
		'path' => "worlds/minecraft/creative/world/",
		'title' => "Creative",
		'overworld' => true,
		'nether' => false,
		'end' => false,
	),
	"ohai" => array(
		'path' => "worlds/minecraft/ohai/world/",
		'title' => "Ohai!",
		'overworld' => true,
		'nether' => false,
		'end' => false,
	),
	"mc1.5" => array(
		'path' => "worlds/minecraft/mc1.5/world/",
		'title' => "MC 1.5",
		'overworld' => true,
		'nether' => true,
		'end' => false,
	),
	"mc1" => array(
		'path' => "mc1-world/",
		'title' => "MC 1",
		'overworld' => true,
		'nether' => true,
		'end' => true,
	),
# MCRegion, needs upgrading.	
#	"beta1.8" => array(
#		'path' => "beta1.8/world/",
#		'title' => "Beta 1.8",
#		'overworld' => true,
#		'nether' => true,
#		'end' => false,
#	),
#	"freebuild" => array(
#		'path' => "freebuild/world3/",
#		'title' => "Freebuild",
#		'overworld' => true,
#		'nether' => true,
#		'end' => false,
#	),
#	"survival" => array(
#		'path' => "survival/world/",
#		'title' => "Survival",
#		'overworld' => true,
#		'nether' => true,
#		'end' => false,
#	),
); // worlds

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

// Output directory

echo 'outputdir = "maps"' . "\r\n";

echo "\r\n";

// World Declarations
foreach( $worlds as $name => $data ) 
{
	echo 'worlds["' . $data['title'] . '"] = "' . $data['path'] . '"' . "\r\n";
}

echo "\r\n";

// Render Declarations
foreach( $worlds as $worldname => $world )
{
	foreach( $renders as $mapname => $map )
	{
		foreach( $directions as $directionname => $direction )
		{
			if( $world[ $map[ 'dimension' ] ] )
			{
				echo 'renders["' . $worldname . '-' . $map['dimension'] . '-' . $mapname . '-' . $directionname . '"] = {' . "\r\n";
				echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
				echo "\t" . '"title": "' . $map['title'] . ' - ' . $direction['title'] . '",' . "\r\n";
				echo "\t" . '"rendermode": "' . $map['rendermode'] . '",' . "\r\n";
				echo "\t" . '"dimension": "' . $map['dimension'] . '",' . "\r\n";
				echo "\t" . '"northdirection": "' . $direction['code'] . '",' . "\r\n";
				if( $map[ 'dimension' ] == "overworld" && isset( $world['manualpois' ] ) && is_array( $world[ 'manualpois' ] ) )
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
						echo "\t\tdict(name=\"" . $marker[ "name" ] . "\", filterFunction=" . $marker[ "filterFunction" ] . ", icon=\"" . $marker[ "icon" ] . "\"),\r\n";
					}
					echo "\t],\r\n";
				}
				echo "}\r\n\r\n";
			}
		}
	}
	
	echo 'renders["' . $worldname . '-biome"] = {' . "\r\n";
	echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
	echo "\t" . '"title": "Biomes",' . "\r\n";
	echo "\t" . '"rendermode": [ClearBase(), BiomeOverlay()],' . "\r\n";
	echo "\t" . '"dimension": "overworld",' . "\r\n";
	echo "\t" . '"overlay": [],' . "\r\n";
	echo "}\r\n\r\n";
		
	echo 'renders["' . $worldname . '-spawn"] = {' . "\r\n";
	echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
	echo "\t" . '"title": "Monster Spawn",' . "\r\n";
	echo "\t" . '"rendermode": [ClearBase(), SpawnOverlay()],' . "\r\n";
	echo "\t" . '"dimension": "overworld",' . "\r\n";
	echo "\t" . '"overlay": [],' . "\r\n";
	echo "}\r\n\r\n";
		
	echo 'renders["' . $worldname . '-slime"] = {' . "\r\n";
	echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
	echo "\t" . '"title": "Slime Spawn",' . "\r\n";
	echo "\t" . '"rendermode": [ClearBase(), SlimeOverlay()],' . "\r\n";
	echo "\t" . '"dimension": "overworld",' . "\r\n";
	echo "\t" . '"overlay": [],' . "\r\n";
	echo "}\r\n\r\n";
}



