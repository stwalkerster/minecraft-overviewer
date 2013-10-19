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
        if poi['Text1'] == '[Underbelly]':
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4']])

def witchHutSignFilter(poi):
    if poi['id'] == 'Sign':
        if poi['Text1'] == '[Witch Hut]':
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4']])

def templeSignFilter(poi):
    if poi['id'] == 'Sign':
        if poi['Text1'] == '[Temple]':
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4']])

def houseSignFilter(poi):
    if poi['id'] == 'Sign':
        if poi['Text1'] == '[House]':
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4']])

def townSignFilter(poi):
    if poi['id'] == 'Sign':
        if poi['Text1'] == '[Town]':
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4']])

def portalSignFilter(poi):
    if poi['id'] == 'Sign':
        if poi['Text1'] == '[Portal]':
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4']])

def pointOfInterestSignFilter(poi):
    if poi['id'] == 'Sign':
        if poi['Text1'] == '[POI]':
            return "\n".join([poi['Text2'], poi['Text3'], poi['Text4']])

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
		), // manualpoi
		"markers" => array(
			array(
				"name"           => "Manual Town",
				"filterFunction" => "townFilter",
				"icon"           => "../marker_town.png",
			),
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
			),
			array(
				"name"           => "Towns",
				"filterFunction" => "townSignFilter",
				"icon"           => "../marker_town.png",
			),
			array(
				"name"           => "Portals",
				"filterFunction" => "portalSignFilter",
				"icon"           => "../marker_portal.png",
			),
			array(
				"name"           => "Points of Interest",
				"filterFunction" => "pointOfInterestSignFilter",
				"icon"           => "../treasure-mark.png",
			),
		), // markers
	), // cowgate
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
						echo "\t\tdict(name=\"" . $marker[ "name" ] . "\", filterFunction=" . $marker[ "filterFunction" ];
						if( isset( $marker[ 'icon' ] ) )
						{
							echo ", icon=\"" . $marker[ "icon" ] . "\"";
						}
						echo "),\r\n";
					}
					echo "\t],\r\n";
				}
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
		echo "}\r\n\r\n";
			
		echo 'renders["' . $worldname . '-' . $directionname . '-spawn"] = {' . "\r\n";
		echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
		echo "\t" . '"title": "Monster Spawn",' . "\r\n";
		echo "\t" . '"rendermode": [ClearBase(), SpawnOverlay()],' . "\r\n";
		echo "\t" . '"dimension": "overworld",' . "\r\n";
		echo "\t" . '"overlay": ["' . $worldname . '-overworld-day-' . $directionname . '"],' . "\r\n";
		echo "\t" . '"northdirection": "' . $direction['code'] . '",' . "\r\n";
		echo "}\r\n\r\n";
			
		echo 'renders["' . $worldname . '-' . $directionname . '-slime"] = {' . "\r\n";
		echo "\t" . '"world": "' . $world['title'] . '",' . "\r\n";
		echo "\t" . '"title": "Slime Spawn",' . "\r\n";
		echo "\t" . '"rendermode": [ClearBase(), SlimeOverlay()],' . "\r\n";
		echo "\t" . '"dimension": "overworld",' . "\r\n";
		echo "\t" . '"overlay": ["' . $worldname . '-overworld-day-' . $directionname . '"],' . "\r\n";
		echo "\t" . '"northdirection": "' . $direction['code'] . '",' . "\r\n";
		echo "}\r\n\r\n";
	}
}



