<?php


$itens = array();

$itens[1]=1;
$itens[3]="3";

unset($itens[3]);

echo json_encode($itens);


?>