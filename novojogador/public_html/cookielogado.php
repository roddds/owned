<?php
//este c�digo, que carrega no in�cio d� p�gina, verifica se o cookie est� logado e retorna uma vari�vel booleana para informar, $logado.

if (isset($_COOKIE["user"])) {$user = $_COOKIE["user"];}//pegamos o cookie user, gravado em gravar_login.php
if (isset($_COOKIE["pass"])) {$pass = $_COOKIE["pass"];}//pegamos o cookie pass, gravado em gravar_login.php

if (isset($user) && isset($pass))//vamos ver se os dados est�o simultaneamente setados...
	{
	$sqlquery = "SELECT * FROM users WHERE user = '$user' AND pass = '$pass'";
	$resultado = mysql_query($sqlquery);
	//Esta consulta verifica se o conteudo dos cookies esta correto.
	//Se der 0, n�o coincide algo, e a entrada ser� proibida:
	if (mysql_num_rows($resultado) == 0) {$logado = false;}
	//Se der 1, est� certo. Se der mais de 1, � porque est� duplicado o login e a senha.
	//Tecnicamente, sendo absolutamente chato, � um erro, mas vamos aceitar mesmo assim.
	else {$logado = true;}
	//vamos aproveitar que estamos aqui e pegar os todos dados do usu�rio, e gravar na session.
	$dadosdousuario = mysql_fetch_array($resultado);
	$userid = $dadosdousuario['id'];
	$_SESSION['userid'] = $userid;

	}
else {$logado = false;}//se nem $user nem $pass estiverem setados, o seguran�a barra.
//De posse da booleana $logado, vamos seguir em frente. Dois blocos de condicionais, ent�o.
//O primeiro barra tudo e manda o vagabundo se logar.
//O segundo mostra a barrinha de usu�rio com as informa��es do acesso, atalhos e permite o uso das p�ginas /admin.
if ($logado == false) {
//include 'loginform.php';
	}

?>