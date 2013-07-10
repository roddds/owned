<?php

$erro=0;
$saveuserid = $userid;
$savesession = serialize($_SESSION);

if (isset($_SESSION['game'])) {
	$savegame=(int)$_SESSION['game'];
} else {$erro=1;}

if (isset($_SESSION['itens'])) {
	$saveitens=serialize($_SESSION['itens']);
} else {$erro=1;}

if (isset($_SESSION['flags'])) {
	$saveflags=serialize($_SESSION['flags']);
} else {$erro=1;}

if (isset($_SESSION['parg'])) {
	$saveparg=(int)$_SESSION['parg'];
} else {$erro=1;}

if (isset($_POST['slot'])) {
	$saveslot=(int)$_POST['slot'];
} else {$erro=1;}

//se não tiver erro, em frente

if ($erro==0){

//verificando se o save não está ocupado
$query="SELECT * FROM saves WHERE user='$saveuserid' AND game=$savegame AND slot=$saveslot" ;
$resultado=mysql_query($query);
if (mysql_num_rows($resultado)>0)
//se estiver ocupado, updatear

{
$query="UPDATE `saves` SET `game`=$savegame, `user`=$saveuserid, `slot`=$saveslot, `itens`='$saveitens', `flags`='$saveflags', `parg`=$saveparg WHERE  user=$saveuserid AND game=$savegame AND slot=$saveslot";
$resultado=mysql_query($query) or die(mysql_error());
}

//se não estiver, salvar novo
else
{
$query="INSERT INTO `saves` (`game`, `user`, `slot`, `itens`, `flags`, `parg`) VALUES ($savegame, $saveuserid, $saveslot, '$saveitens', '$saveflags', $saveparg)";
$resultado=mysql_query($query) or die(mysql_error());
}

echo "<p style='color:green'>Jogo salvo no Slot $saveslot</p>";
echo "<br/>";

include "game.php";

}

else {

	include "game.php";
}

?>