<?php

$worlds = array();
$worlds["cowgate"] = array( 'path' => "worlds/minecraft/cowgate/cowgate/", 'title' => "Underbelly Cowgate", 'nether' => true, 'end' => false );
$worlds["creative"] = array( 'path' => "worlds/minecraft/creative/world/", 'title' => "Creative", 'nether' => false, 'end' => false );
$worlds["ohai"] = array( 'path' => "worlds/minecraft/ohai/world/", 'title' => "Ohai!", 'nether' => true, 'end' => true );
$worlds["mc1.5"] = array( 'path' => "worlds/minecraft/mc1.5/world/", 'title' => "MC 1.5", 'nether' => true, 'end' => true );

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
<?php
if( $data['nether'] ) {
?>
renders["<?php echo $name; ?>-nether-north"] = {
    "world": "<?php echo $data['title']; ?>",
    "title": "Nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
}
<?php
}

if( $data['end'] ) {
?>
renders["<?php echo $name; ?>-end-north"] = {
    "world": "<?php echo $data['title']; ?>",
    "title": "The End",
    "rendermode": smooth_lighting,
    "dimension": "end",
}
<?php
}
}
?>

outputdir = "maps"
