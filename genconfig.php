<?php

$worlds = array();
$worlds["cowgate"] = array( 'path' => "worlds/minecraft/cowgate/cowgate/", 'title' => "Underbelly Cowgate" );
$worlds["creative"] = array( 'path' => "worlds/minecraft/creative/world/", 'title' => "Creative" );
$worlds["ohai"] = array( 'path' => "worlds/minecraft/ohai/world/", 'title' => "Ohai!" );
$worlds["mc1.5"] = array( 'path' => "worlds/minecraft/mc1.5/world/", 'title' => "MC 1.5" );

foreach( $worlds as $name => $data ) 
{
	echo 'worlds["' . $data['title'] . '"] = "' . $data['path'] . '"' . "\r\n";
}
foreach( $worlds as $name => $data ) 
{
?>

renders["<?php echo $name; ?>-overworld-day-north"] = {
    "world": "<?php echo $data['title']; ?>",
    "title": "Day",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
}

renders["<?php echo $name; ?>-overworld-night-north"] = {
    "world": "<?php echo $data['title']; ?>",
    "title": "Night",
    "rendermode": smooth_night,
    "dimension": "overworld",
}

renders["<?php echo $name; ?>-nether-north"] = {
    "world": "<?php echo $data['title']; ?>",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}
<?php
}
?>

outputdir = "maps"
