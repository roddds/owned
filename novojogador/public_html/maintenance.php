<?php
include "dbconnectmysql.php";
include "functions.php";
include "functions2.php";

if (isset($_COOKIE['user']) && (($_COOKIE['user']=="Douglas") xor ($_COOKIE['user']=="Simone")) xor ($_COOKIE['user']=="maya_sibylla")){echo $_COOKIE['user'].": Usu&aacute;rio Autorizado";}
else {
	echo "Tentativa de Acesso a &Aacuterea n&atilde;o Autorizada";
	die();
}

if (isset ($_GET['parg'])) {
	$parg = $_GET['parg'];
} else {$parg = 1;
}

$nextparg=$parg+1;
$lastparg=$parg-1;

if (isset ($_GET['game'])) {
	$game = $_GET['game'];
} else {$game = 1;
}

//recebe os dados da form anterior a os grava.
if (isset($_POST['op1'])){
include "recebemaintenance.php";
}

$paragraph = mysql_query("SELECT * FROM paragraphs WHERE game=$game AND parg=$parg");
while($row = mysql_fetch_array($paragraph)) {

	$title=$row['title'];
	$text=$row['text'];
	$text2=$row['text2'];
	$itens=$row['itens'];
	$flags=$row['flags'];

	$option1=$row['option1'];
	$option2=$row['option2'];
	$option3=$row['option3'];
	$option4=$row['option4'];
	$option5=$row['option5'];

	$itens1=$row['itens1'];
	$itens2=$row['itens2'];
	$itens3=$row['itens3'];
	$itens4=$row['itens4'];
	$itens5=$row['itens5'];

	$flags1=$row['flags1'];
	$flags2=$row['flags2'];
	$flags3=$row['flags3'];
	$flags4=$row['flags4'];
	$flags5=$row['flags5'];


	$target1=$row['target1'];
	$target2=$row['target2'];
	$target3=$row['target3'];
	$target4=$row['target4'];
	$target5=$row['target5'];

}

?>
<html>
<body>

<table width="100%" border="1">
<tr>
<td colspan="3">
<table width="100%">
<tr>
<td>

<form action="maintenance.php?parg=<?php echo $lastparg?>" method="post">
<input type="submit" value="Ir para <?php echo $lastparg?>" />
</form>

</td>
<td><h1>Entrada <?php echo $title;?></h1></td>
<td>

<form action="maintenance.php?parg=<?php echo $nextparg?>" method="post">
<input type="submit" value="Ir para <?php echo $nextparg?>" />
</form>

</td>
</tr>
</table>
</td>
<form action="maintenance.php?parg=<?php echo $parg?>" method="post">
</tr>
<tr>
<td><h4>Texto<input type="submit" value="Gravar" />
</h4></td>
<td><h4>Itens</h4></td>
<td><h4>Flags</h4></td>
</tr>
<tr>
<td>

<?php
echo "$text";
?>

<textarea name="op1" id="op1" cols="100" rows="8" ><?php
echo $text;
?></textarea>
<br />

<?php
echo "$text2";
?>
<textarea name="op1t2" id="op1t2" cols="100" rows="2" ><?php
echo $text2;
?></textarea>

<table width="100%" border="1">
<tr>
<td colspan="4"><h3>Esta entrada atualiza os seguintes itens e flags:</h3></td>
</tr>
<tr>
<td>Itens ( a:n:{i:n;i:q;} )</td>
<td>Flags ( a:n:{i:n;i:q;} )</td>
</tr>
<tr>
<td><input type="text" name="op2" id="op2" value="<?php echo $itens;?>" /></td>
<td><input type="text" name="op12" id="op12" value="<?php echo $flags;?>" /></td>
</tr>
</table>

<table width="100%" border="1">
<tr>
<td colspan="6">Op&ccedil;&otilde;es</td>
</tr>
<tr>
<td>Op&ccedil;&atilde;o</td>
<td>Target</td>
<td>Itens ( a:n:{i:n;i:q;} )</td>
<td>Flags ( a:n:{i:n;i:q;} )</td>
</tr>
<tr>
<td><input type="text" name="op22" id="op22" value="<?php echo $option1;?>" /></td>
<td><input type="text" name="op27" id="op27" value="<?php echo $target1;?>" /></td>
<td><input type="text" name="op32" id="op32" value="<?php echo $itens1;?>"/></td>
<td><input type="text" name="op42" id="op42" value="<?php echo $flags1;?>"/></td>
</tr>
<tr>
<td><input type="text" name="op23" id="op23" value="<?php echo $option2;?>" /></td>
<td><input type="text" name="op28" id="op28" value="<?php echo $target2;?>" /></td>
<td><input type="text" name="op33" id="op33" value="<?php echo $itens2;?>" /></td>
<td><input type="text" name="op43" id="op43" value="<?php echo $flags2;?>" /></td>
</tr>
<tr>
<td><input type="text" name="op24" id="op24" value="<?php echo $option3;?>" /></td>
<td><input type="text" name="op29" id="op29" value="<?php echo $target3;?>" /></td>
<td><input type="text" name="op34" id="op34" value="<?php echo $itens3;?>" /></td>
<td><input type="text" name="op44" id="op44" value="<?php echo $flags3;?>" /></td>
</tr>
<tr>
<td><input type="text" name="op25" id="op25" value="<?php echo $option4;?>" /></td>
<td><input type="text" name="op30" id="op30" value="<?php echo $target4;?>" /></td>
<td><input type="text" name="op35" id="op35" value="<?php echo $itens4;?>" /></td>
<td><input type="text" name="op45" id="op45" value="<?php echo $flags4;?>" /></td>
</tr>
<tr>
<td><input type="text" name="op26" id="op26" value="<?php echo $option5;?>" /></td>
<td><input type="text" name="op31" id="op31" value="<?php echo $target5;?>" /></td>
<td><input type="text" name="op36" id="op36" value="<?php echo $itens5;?>" /></td>
<td><input type="text" name="op46" id="op46" value="<?php echo $flags5;?>" /></td>
</tr>
</table>
</td>
<td>
<?php
$query = mysql_query("SELECT * FROM items WHERE game=$game ORDER BY itemnum");
while ($row = mysql_fetch_array($query)){
	echo $row['itemnum']." - ".$row['name']." <br/>";
}
?>
</td>
<td>
<?php

$query = mysql_query("SELECT * FROM flags WHERE game=$game ORDER BY flagnum");
while ($row = mysql_fetch_array($query)){
	echo $row['flagnum']." - ".$row['name']." <br/>";
}
?>
</td>
</tr>
<tr>
<td>Cadastrar novos itens ou flags:</td>
<td><input type="text" name="op47" id="op47" /></td>
<td><input type="text" name="op48" id="op48" /></td>
</tr>
</table>
<input type="submit" value="Gravar" />
</form>
</body>
</html>

<?php

@mysql_close();
?>
