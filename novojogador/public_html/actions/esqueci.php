<?php

if (isset($_POST['email'])) {

	//pegar os dados do post
	if (isset($_POST['email'])) {
		$email=$_POST['email'];
	}

	$sqlquery = "SELECT * FROM users WHERE email = '$email'";
	$resultado = mysql_query($sqlquery);

	echo "e-mail informado: $email<br/><br/>";

	if (mysql_num_rows($resultado) == 0) {$registrado = false;}
	else {$registrado = true;}

	if ($registrado==true){
		$dadosusuario = mysql_fetch_array($resultado);
		$userusuario = $dadosusuario['user'];
		$senhausuario = $dadosusuario['pass'];
		$mensagem = "Os seus dados de login s&atilde;o:<br/>login: $userusuario<br/>senha: $senhausuario<br/>";

	$headers = "From: Recuperação de Senha do OWNED! <no-reply@novojogador.com.br>" . "\n";
	$headers .= 'MIME-Version: 1.0' . "\n";
	$headers .= 'Content-type: text/html; charset=utf-8' . "\r\n";

	//echo $mensagem;

	if (mail($email, "Recuperação de Senha do OWNED!", $mensagem, $headers)) {
	echo "<p style='color:green'>OK, verifique sua caixa de e-mails! Se o e-mail informado &eacute; v&aacute;lido, voc&ecirc; em breve receber&aacute; seus dados!</p>";
	}

	}
	else {
	echo "<p style='color:green'>OK, verifique sua caixa de e-mails! Se o e-mail informado &eacute; v&aacute;lido, voc&ecirc; em breve receber&aacute; seus dados!</p>";
	}


}

else {
?>

<div style="width:100%;">Esqueceu a Senha?</div>
<br />
<br />
<br />

<div style="width:100%;">
<p>Esqueceu a senha? Sem problemas. Insira o e-mail usado para se cadastrar no site no campo abaixo, clique em "Enviar" e pronto - se o seu e-mail estiver realmente na nossa base de dados, voc&ecirc; vai receber um e-mail em breve com seu login e senha.</p>
<form action="index.php?action=esqueci"  method='POST'>

<table with=100%>

<tr>
	<td>
		<p>Seu e-mail:</p>
	</td>
	<td>
		<input type='text' size="70" name='email'>
	</td>
</tr>

</table>

<p><input type='submit' value="Enviar!" /></p>

</form>

<p>&nbsp;</p>

</div>
<?php
}
?>