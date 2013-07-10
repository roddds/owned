
<?php

unset($itens);
$itens = array();
$_SESSION['itens'] = $itens;
unset($flags);
$flags = array();
$_SESSION['flags'] = $flags;
$_SESSION['parg'] = 1;
$parg=$_SESSION['parg'];


?>


<span style="font-size: 14px">

<p><em>OWNED &ndash; um novo jogador</em> &eacute; um livro interativo. Voc&ecirc; decide o final.</p>
<p>Em <em>OWNED</em> voc&ecirc; &eacute; Andr&eacute;, um t&eacute;cnico de inform&aacute;tica viciado em videogames que vai tentar conquistar pelo menos uma dentre <strong>sete</strong> garotas. Para jogar, basta clicar em uma das op&ccedil;&otilde;es no final de cada trecho de hist&oacute;ria, dando um rumo &agrave; vida de Andr&eacute;.</p>
<p>Voc&ecirc; vai ter como salvar o jogo e pode jogar de novo quantas vezes quiser. &Eacute; gr&aacute;tis!</p>
<p>Alguma palavra desconhecida? Consulte o <strong><a href="index.php?action=glossario">gloss&aacute;rio</a></strong>.</p>


<table width="100%" border="0">

<tr><td align="center">
<strong>
<p style="color:red">Aten&ccedil;&atilde;o:</p>
<p style="color:red">Esse livro-jogo &eacute; recomendado para maiores de 18 anos.</p>
<p style="color:red">Cont&eacute;m sexo, drogas, viol&ecirc;ncia, palavras chulas, cenas sangrentas.</p>
</strong>
<br/>
<br/>


<table>
<tr>

<td></tr>

<td>
<?php
echo "

	<form action='index.php?action=game' method='POST'>
	<div class='buttons'>
	<button type='submit'>Iniciar o Jogo</button>
	<input type='hidden' name='disclaimer' value=true >
	<input type='hidden' name='parg' value=1 >
	</div>
	</form>

	<form action='http://www.simonecampos.net' method='POST'>
	<div class='buttons'>
	<button type='submit'>Sair do Site</button>
	</div>
	</form>	";

	?>
</td>

<td></tr>

</tr>
</table>

</table>
</span>


