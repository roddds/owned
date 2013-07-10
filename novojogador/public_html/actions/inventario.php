<?php

$temitens = array_search(1, $itens);
if($temitens)
{
	echo "<p>Voc&ecirc; carrega os seguintes itens:</p>";
}
else {
	echo "<p>Voc&ecirc; n&atilde;o possui nenhum item no momento.</p>";
}



foreach ($itens as $key=>$value){

	if ($value > 0) {
	$query = mysql_query("SELECT * FROM items WHERE game=$game AND itemnum=$key");
	$row = mysql_fetch_array($query);
	$nomeitem=$row['name'];
	$imageitem=$row['imagem'];

	//mostra


	echo "<table width=60px height=150px  style='text-align:center; position:relative; clear:none; float:left'>";
	echo "<tr><td><strong>$nomeitem</strong></td><tr/>";
	echo "<tr><td><img src='itens/$imageitem' style='border:0px'><br/></td><tr/>";
	echo "</table>";






	}
}







?>