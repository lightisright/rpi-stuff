<?php 

$file = '/var/lib/ds18b20/kitchen.log';

$MY_str_getcsv = function($arg) { 
  $res = str_getcsv($arg, ";");
  if ( count($res) == 3 ) {
    return array('time'=>$res[0], 'timestamp'=>$res[1], 'temp'=>(strlen($res[2])?$res[2]:0));
  }
  return $res;
};

$csv = array_map($MY_str_getcsv, file($file));

// remove last line if empty
if ( count($csv[count($csv)-1]) != 3 ) {
  unset($csv[count($csv)-1]);
}

header('Content-type: application/json');
echo json_encode($csv);

