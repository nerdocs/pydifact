#/bin/sh

gen="python -m pydifact.generator.runner"


$gen service 1
$gen service 2
$gen service 3
$gen service 4

$gen d24a
$gen d23a
$gen d21a
