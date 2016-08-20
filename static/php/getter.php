<?php

$username = "root";
$password = "Rutgers123";
$hostname = "128.6.237.242";


$db_handle = mysql_connect($hostname,$username,$password) or die("Unable to connect to mysql");
$selected = mysql_select_db("wimdata", $db_handle) or die("Could not connect to database");

$query = "SELECT DISTINCT SRI FROM links WHERE sri REGEXP '__$' ORDER BY SRI";
$result = mysql_query($query);
$id = 2;
$sri = null;
$output = null;
while($sri_id = mysql_fetch_array($result))
{
	$sri = (string)$sri_id{'SRI'};
	$valueToAdd = '{"id": "'. $id++ . '", "sri": "' . $sri . '"},';
	$output = $output . $valueToAdd;
}

$output = rtrim($output, ",");
//header('Content-Type: application/json');
echo json_encode('['. $output .']');
?>


