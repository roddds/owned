<?php
echo "<br/>";
echo "<br/>";

	echo "

	<table>
	<tr>
	<td>
	<p>Come&ccedil;ar de novo (voc&ecirc; perder&aacute; todos os itens e progresso!)</p>
	</td>
	</tr>
	<tr>
	<td>

	<form action='index.php' method='POST'>
	<div class='buttons'>
	<button type='submit'>Reiniciar o jogo</button>
	<input type='hidden' name='disclaimer' value=false >
	<input type='hidden' name='parg' value=1 >
	</div>
	</form>
	</td>
	</tr>
	</table>
	";

echo "<br/>";

if ($logado==false){
	echo "

	<table>
	<tr>
	<td>
	<p>Save & Load (Voc&ecirc; precisa estar logado)</p>
	</td>
	</tr>
	<tr>
	<td>
		<form>
		<div class='buttons'>
		<button type='submit' disabled='disabled' style='color:Gainsboro; background:none;'>Salvar no Slot 1</button>
		</div>
		</form>
	</td>
	<td>
		<form>
		<div class='buttons'>
		<button type='submit' disabled='disabled' style='color:Gainsboro; background:none;'>Carregar do Slot 1</button>
		</div>
		</form>
	</td>
	</tr>
		<tr>
	<td>
		<form>
		<div class='buttons'>
		<button type='submit' disabled='disabled' style='color:Gainsboro; background:none;'>Salvar no Slot 2</button>
		</div>
		</form>
	</td>
	<td>
		<form>
		<div class='buttons'>
		<button type='submit' disabled='disabled' style='color:Gainsboro; background:none;'>Carregar do Slot 2</button>
		</div>
		</form>
	</td>
	</tr>
		<tr>
	<td>
		<form>
		<div class='buttons'>
		<button type='submit' disabled='disabled' style='color:Gainsboro; background:none;'>Salvar no Slot 3</button>
		</div>
		</form>
	</td>
	<td>
		<form>
		<div class='buttons'>
		<button type='submit' disabled='disabled' style='color:Gainsboro; background:none;'>Carregar do Slot 3</button>
		</div>
		</form>
	</td>
	</tr>

	</table>
";

}
if ($logado==true){
	echo "

	<table>
	<tr>
	<td>
	<p>Save & Load</p>
	</td>
	</tr>
	<tr>
	<td>
		<form action='index.php?action=save' method='POST'>
		<div class='buttons'>
		<button type='submit'>Salvar no Slot 1</button>
		<input type='hidden' name='slot' value='1' >
		</div>
		</form>
	</td>";

	//verificar se há um jogo no slot1
	$sqlquery = "SELECT * FROM saves WHERE user='$userid' AND game=$game AND slot=1";
	$resultado = mysql_query($sqlquery);
	if (mysql_num_rows($resultado)>0){
	echo "
	<td>
		<form action='index.php?action=load' method='POST'>
		<div class='buttons'>
		<button type='submit'>Carregar do Slot 1</button>
		<input type='hidden' name='slot' value='1' >
		</div>
		</form>
	</td>";}

	else {
	echo "
	<td>
		<form action='index.php?action=load' method='POST'>
		<div class='buttons'>
		<button type='submit' disabled='disabled' style='color:Gainsboro; background:none;'>Carregar do Slot 1</button>
		<input type='hidden' name='slot' value='1' >
		</div>
		</form>
	</td>";
	}


	echo"
	</tr>

		<tr>
	<td>
		<form action='index.php?action=save' method='POST'>
		<div class='buttons'>
		<button type='submit'>Salvar no Slot 2</button>
		<input type='hidden' name='slot' value='2' >
		</div>
		</form>
	</td>";
	//verificar se há um jogo no slot2
	$sqlquery = "SELECT * FROM saves WHERE user='$userid' AND game=$game AND slot=2";
	$resultado = mysql_query($sqlquery);
	if (mysql_num_rows($resultado)>0){
	echo "
	<td>
		<form action='index.php?action=load' method='POST'>
		<div class='buttons'>
		<button type='submit'>Carregar do Slot 2</button>
		<input type='hidden' name='slot' value='2' >
		</div>
		</form>
	</td>";}

	else {
	echo "
	<td>
		<form action='index.php?action=load' method='POST'>
		<div class='buttons'>
		<button type='submit' disabled='disabled' style='color:Gainsboro; background:none;'>Carregar do Slot 2</button>
		<input type='hidden' name='slot' value='2' >
		</div>
		</form>
	</td>";
	}

echo "
	</tr>

		<tr>
	<td>
		<form action='index.php?action=save' method='POST'>
		<div class='buttons'>
		<button type='submit'>Salvar no Slot 3</button>
		<input type='hidden' name='slot' value='3' >
		</div>
		</form>
	</td>";
	//verificar se há um jogo no slot3
	$sqlquery = "SELECT * FROM saves WHERE user='$userid' AND game=$game AND slot=3";
	$resultado = mysql_query($sqlquery);
	if (mysql_num_rows($resultado)>0){
	echo "
	<td>
		<form action='index.php?action=load' method='POST'>
		<div class='buttons'>
		<button type='submit'>Carregar do Slot 3</button>
		<input type='hidden' name='slot' value='3' >
		</div>
		</form>
	</td>";}

	else {
	echo "
	<td>
		<form action='index.php?action=load' method='POST'>
		<div class='buttons'>
		<button type='submit' disabled='disabled' style='color:Gainsboro; background:none;'>Carregar do Slot 3</button>
		<input type='hidden' name='slot' value='3' >
		</div>
		</form>
	</td>";
	}
	echo "
	</tr>

	</table>
";

}

echo "<br/>";
echo "<br/>";
echo "<br/>";
echo "<br/>";

?>