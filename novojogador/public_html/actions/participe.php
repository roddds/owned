<?php

if ((isset($_POST['remetente'])) &&  (isset($_POST['remetente'])) && (isset($_POST['remetente']))) {

	//pegar os dados do post
	if (isset($_POST['mensagem']))
	{
		$mensagem=$_POST['mensagem'];
	}
	if (isset($_POST['remetente'])) {
		$remetente=$_POST['remetente'];
	}
	if (isset($_POST['email'])) {
		$email=$_POST['email'];
	}
	if (isset($_POST['assunto'])) {
		$assunto=$_POST['assunto'];
	}



	$to = "'Simone Campos' <simonecampos@gmail.com>";
	$assunto = "[Contato OWNED!] $assunto";

	$message = wordwrap($mensagem);

	$headers = "From: $remetente <$email>" . "\n";
	$headers .= 'MIME-Version: 1.0' . "\n";
	$headers .= 'Content-type: text/html; charset=utf-8' . "\r\n";

	if (mail($to, $assunto, $mensagem, $headers)) {
	echo "<p style='color:green'>Mensagem enviada com sucesso!</p>";
	}


}
?>

<div style="width:100%;"><img src="images/titleparticipe.jpg" width="525" height="66" align="right"></div>
<br />
<br />
<br />

<div style="width:100%;">
<p>O formul&aacute;rio abaixo &eacute; para entrar em contato com a autora, reclamar de problemas no site ou at&eacute; participar mandando o link de alguma ilustra&ccedil;&atilde;o ou texto inspirados no universo de <i>Owned</i>*.</p>
<form action="index.php?action=participe"  method='POST'>

<table with=100%>
<tr>
	<td>
		<p>Seu nome:</p>
	</td>
	<td>
		<input type='text' size="70" name='remetente'>
	</td>
</tr>

<tr>
	<td>
		<p>Seu e-mail:</p>
	</td>
	<td>
		<input type='text' size="70" name='email'>
	</td>
</tr>

<tr>
	<td>
		<p>Assunto:</p>
	</td>
	<td>
		<input type='text' size="70" name='assunto'>
	</td>
</tr>

</table>

<p><textarea cols='75' rows='15' name='mensagem'></textarea> </p>

<p><input type='submit' value="Enviar!" /></p>

</form>
<p>* <i>Owned</i> est&aacute; registrado sob Creative Commons By-Nc-Sa. Ou seja, permitem-se trabalhos derivados de <i>Owned</i> &#8211; um novo jogador sem fins lucrativos e com o devido cr&eacute;dito &agrave; autora (Simone Campos) e do livro (<i>OWNED</i>). Vale ilustra&ccedil;&atilde;o, v&iacute;deo, fanfic... Se voc&ecirc; fizer algum trabalho nesses moldes relacionado a Owned e quiser divulgar, mande para n&oacute;s avaliarmos e, gostando, colocaremos o <i>link</i> nesse site. </p>
<p>&nbsp;</p>

</div>