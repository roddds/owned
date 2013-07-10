<?php

function mostraparagrafo($game, $parg) {
	$paragraph = mysql_query("SELECT * FROM paragraphs WHERE parg=$parg");
	while($row = mysql_fetch_array($paragraph)) {
		$title=$row['title'];
		$text=$row['text'];
		$parg=$row['parg'];

	echo "<h3>$title</h3>";
	echo "<p>$text</p>";
	}
}
function mostraparagrafo2($game, $parg) {
	$paragraph = mysql_query("SELECT * FROM paragraphs WHERE parg=$parg");
	while($row = mysql_fetch_array($paragraph)) {
		$text2=$row['text2'];

	echo "<p>$text2</p>";
	}
}





function mostraopcao($game, $parg, $n) {
	global $game;
	global $itens;
	global $flags;

	$paragraph = mysql_query("SELECT * FROM paragraphs WHERE parg=$parg");
	while($row = mysql_fetch_array($paragraph)) {

		$option=$row['option'.$n];
		$target=$row['target'.$n];
		$itenso=$row['itens'.$n];
		$flagso=$row['flags'.$n];

		$itenso=unserialize($itenso);
		$flagso=unserialize($flagso);

		if (is_array($itenso)){} else {$itenso = array();}
		if (is_array($flagso)){} else {$flagso = array();}

	}	//fim do while

		$opcaohabilitada=true;

		//varrer $itenso. Qualquer diferença desabilita a opção.

		if (count($itenso)>0){
		foreach ($itenso as $key => $value){
				if ($itenso[$key]==$itens[$key]){} else {$opcaohabilitada=false;}
			}}

		if (count($flagso)>0){
		foreach ($flagso as $key => $value){
				if ($flagso[$key]==$flags[$key]){} else {$opcaohabilitada=false;}
			}}

		// mostrar a opção, como habilitada
		if (($target > 0)&&($opcaohabilitada==true)){

			echo "
			<form action='index.php?action=game' method='POST'>
			<div class='buttons'>
			<button type='submit'>$option</button>
			</div>
			<input type='hidden' name='parg' value='".$target."' >
			<input type='hidden' name='game' value='".$game."' >
			</form>	";
			}

		// mostrar a opção, como desabilitada
		if (($target > 0)&&($opcaohabilitada==false)){

			echo "
			<form action='index.php?action=game' method='POST'>
			<div class='buttons'>
			<button type='submit' disabled='disabled' style='color:Gainsboro; background:none;'>$option</button>
			</div>
			<input type='hidden' name='parg' value='".$target."' >
			<input type='hidden' name='game' value='".$game."' >
			</form>	";
			}

	}	//fim da funcao





function criabotao($nome, $arquivo, $action, $target) {
	echo "
	<form method='post' action='$arquivo'>
	<div class='buttons'>
	<button type='submit'>$nome</button>
    <INPUT TYPE='hidden' NAME='action' VALUE='$action'>
    <INPUT TYPE='hidden' NAME='target' VALUE='$target'>
    </div>
	</form>
	";
}

function criaitem($nome, $acao) {
	echo "<a href='index.php?action=$acao'>$nome</a>";
}



function atualizaitens() { //função OK
	global $game;
	global $parg;
	global $itens;
	$query = mysql_query("SELECT itens FROM paragraphs WHERE parg=$parg");
	$row = mysql_fetch_array($query);
	$acao=$row['itens'];
	if ($acao!=null) {
		$acao = unserialize($acao);
		foreach ($acao as $key => $value){
			$itens[$key] = $value;
		}
		}
	$_SESSION['itens'] = $itens;
	}

function atualizaflags() {
		//função OK
		global $game;
		global $parg;
		global $flags;
		$query = mysql_query("SELECT flags FROM paragraphs WHERE parg=$parg");
		$row = mysql_fetch_array($query);
		$acao=$row['flags'];
		if ($acao!=null) {
			$acao = unserialize($acao);
			foreach ($acao as $key => $value){
				$flags[$key] = $value;
			}
		}
		$_SESSION['flags'] = $flags;
	}



