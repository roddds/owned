<?php
//recebe o POST

if (isset ($_POST['op1'])) {
	$op1 = $_POST['op1'];
}
if (isset ($_POST['op1t2'])) {
	$op1t2 = $_POST['op1t2'];
}
if (isset ($_POST['op2'])) {
	$op2 = $_POST['op2'];
}
if (isset ($_POST['op3'])) {
	$op3 = $_POST['op3'];
}
if (isset ($_POST['op4'])) {
	$op4 = $_POST['op4'];
}
if (isset ($_POST['op5'])) {
	$op5 = $_POST['op5'];
}
if (isset ($_POST['op6'])) {
	$op6 = $_POST['op6'];
}
if (isset ($_POST['op7'])) {
	$op7 = $_POST['op7'];
}
if (isset ($_POST['op8'])) {
	$op8 = $_POST['op8'];
}
if (isset ($_POST['op9'])) {
	$op9 = $_POST['op9'];
}
if (isset ($_POST['op10'])) {
	$op10 = $_POST['op10'];
}
if (isset ($_POST['op11'])) {
	$op11 = $_POST['op11'];
}
if (isset ($_POST['op12'])) {
	$op12 = $_POST['op12'];
}
if (isset ($_POST['op13'])) {
	$op13 = $_POST['op13'];
}
if (isset ($_POST['op14'])) {
	$op14 = $_POST['op14'];
}
if (isset ($_POST['op15'])) {
	$op15 = $_POST['op15'];
}
if (isset ($_POST['op16'])) {
	$op16 = $_POST['op16'];
}
if (isset ($_POST['op17'])) {
	$op17 = $_POST['op17'];
}
if (isset ($_POST['op18'])) {
	$op18 = $_POST['op18'];
}
if (isset ($_POST['op19'])) {
	$op19 = $_POST['op19'];
}
if (isset ($_POST['op20'])) {
	$op20 = $_POST['op20'];
}
if (isset ($_POST['op21'])) {
	$op21 = $_POST['op21'];
}
if (isset ($_POST['op22'])) {
	$op22 = $_POST['op22'];
}
if (isset ($_POST['op23'])) {
	$op23 = $_POST['op23'];
}
if (isset ($_POST['op24'])) {
	$op24 = $_POST['op24'];
}
if (isset ($_POST['op25'])) {
	$op25 = $_POST['op25'];
}
if (isset ($_POST['op26'])) {
	$op26 = $_POST['op26'];
}
if (isset ($_POST['op27'])) {
	$op27 = $_POST['op27'];
}
if (isset ($_POST['op28'])) {
	$op28 = $_POST['op28'];
}
if (isset ($_POST['op29'])) {
	$op29 = $_POST['op29'];
}
if (isset ($_POST['op30'])) {
	$op30 = $_POST['op30'];
}
if (isset ($_POST['op31'])) {
	$op31 = $_POST['op31'];
}
if (isset ($_POST['op32'])) {
	$op32 = $_POST['op32'];
}
if (isset ($_POST['op33'])) {
	$op33 = $_POST['op33'];
}
if (isset ($_POST['op34'])) {
	$op34 = $_POST['op34'];
}
if (isset ($_POST['op35'])) {
	$op35 = $_POST['op35'];
}
if (isset ($_POST['op36'])) {
	$op36 = $_POST['op36'];
}
if (isset ($_POST['op37'])) {
	$op37 = $_POST['op37'];
}
if (isset ($_POST['op38'])) {
	$op38 = $_POST['op38'];
}
if (isset ($_POST['op39'])) {
	$op39 = $_POST['op39'];
}
if (isset ($_POST['op40'])) {
	$op40 = $_POST['op40'];
}
if (isset ($_POST['op41'])) {
	$op41 = $_POST['op41'];
}
if (isset ($_POST['op42'])) {
	$op42 = $_POST['op42'];
}
if (isset ($_POST['op43'])) {
	$op43 = $_POST['op43'];
}
if (isset ($_POST['op44'])) {
	$op44 = $_POST['op44'];
}
if (isset ($_POST['op45'])) {
	$op45 = $_POST['op45'];
}
if (isset ($_POST['op46'])) {
	$op46 = $_POST['op46'];
}
if (isset ($_POST['op47'])) {
	$op47 = $_POST['op47'];
}
if (isset ($_POST['op48'])) {
	$op48 = $_POST['op48'];
}

//se tiver itens novos (op47), grava
if ($op47>""){
//descobre o último itemnum
	$query = mysql_query("SELECT MAX(itemnum) FROM items WHERE game=$game");
	$row = mysql_fetch_array($query);
	$in=$row['MAX(itemnum)'];
	$in++;
	$query = mysql_query("INSERT INTO `items` (`game`,`name`,`itemnum`,`imagem`) VALUES ($game, '$op47', $in, '$in.jpg')");
}
//se tiver flags novas (op48), grava
if ($op48>""){
//descobre o último flagmnum
$query = mysql_query("SELECT MAX(flagnum) FROM flags WHERE game=$game");
$row = mysql_fetch_array($query);
$fn=$row['MAX(flagnum)'];
$fn++;
$query = mysql_query("INSERT INTO `flags` (`game`,`name`,`flagnum`) VALUES ($game, '$op48', $fn)");
}

//prepara variáveis
//cria opitens
$opitens=$op2;

//cria opflags
$opflags=$op12;


$opitens1=$op32;
$opitens2=$op33;
$opitens3=$op34;
$opitens4=$op35;
$opitens5=$op36;
$opflags1=$op42;
$opflags2=$op43;
$opflags3=$op44;
$opflags4=$op45;
$opflags5=$op46;

//grava tudo.
if (isset($op1)){
$query = mysql_query("UPDATE `paragraphs` SET `text`='$op1', `text2`='$op1t2', `itens`='$opitens', `flags`='$opflags', `option1`='$op22', `option2`='$op23', `option3`='$op24', `option4`='$op25', `option5`='$op26', `target1`='$op27',`target2`='$op28',`target3`='$op29',`target4`='$op30',`target5`='$op31', `itens1`='$opitens1', `itens2`='$opitens2', `itens3`='$opitens3', `itens4`='$opitens4', `itens5`='$opitens5', `flags1`='$opflags1', `flags2`='$opflags2', `flags3`='$opflags3', `flags4`='$opflags4', `flags5`='$opflags5' WHERE `game`=$game AND `parg`=$parg") or die (mysql_error());
}





?>
