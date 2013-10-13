<?php

$worlds = array(
	"cowgate" => array(
		'path' => "worlds/minecraft/cowgate/cowgate/",
		'title' => "Underbelly Cowgate",
		'overworld' => true,
		'nether' => true,
		'end' => false,
	),
);

$renders = array(
	// DAY is required!
	"day" => array(
		'title' => 'Day',
		'rendermode' => 'smooth_lighting',
		'dimension' => 'overworld',
	),
);

$directions = array(
	// NORTH is required!
	"north" => array(
		"code" => "upper-left",
		"title" => "North",
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



