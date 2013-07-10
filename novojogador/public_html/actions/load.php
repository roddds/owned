<?php
//
$erro=0;
$loaduserid = $userid;

if (isset($_SESSION['game'])) {
	$loadgame=(int)$_SESSION['game'];
} else {$erro=1;
}
if (isset($_SESSION['parg'])) {
	$loadparg=(int)$_SESSION['parg'];
} else {$erro=1;
}
if (isset($_POST['slot'])) {
	$loadslot=(int)$_POST['slot'];
} else {$erro=1;
}

//se não tiver erro, em frente

if ($erro==0){

	$sqlquery = "SELECT * FROM saves WHERE user='$loaduserid' AND game=$loadgame AND slot=$loadslot";
	$resultado = mysql_query($sqlquery);
	$dadosdoload = mysql_fetch_array($resultado);

	$itens=unserialize($dadosdoload['itens']);
	$flags=unserialize($dadosdoload['flags']);	
	$parg=$dadosdoload['parg'];

	$_SESSION['parg']=$parg;
	$_SESSION['itens']=$itens;
	$_SESSION['flags']=$flags;

	echo "<p style='color:green'>Continuando o jogo salvo no Slot $loadslot...</p>";
	echo "<br/>";


	include "game.php";

	}
	else {

		include "game.php";


	}


	?>