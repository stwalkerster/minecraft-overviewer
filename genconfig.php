<?php

$worlds = array(
	"cowgate" => array(
		'path' => "worlds/minecraft/cowgate/cowgate/",
		'title' => "Underbelly Cowgate",
		'overworld' => true,
		'nether' => true,
		'end' => false,
	),
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
);

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
				echo "}\r\n\r\n";
			}
		}
	}
	
	echo 'renders["' . $worldname . '-biome"] = {' . "\r\n";
	echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
	echo "\t" . '"title": "Biomes",' . "\r\n";
	echo "\t" . '"rendermode": [ClearBase(), BiomeOverlay()],' . "\r\n";
	echo "\t" . '"overlay": [\'' . $worldname . '-overworld-day-north\'],' . "\r\n";
	echo "}\r\n\r\n";
}



