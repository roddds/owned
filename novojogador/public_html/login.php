<?php
require_once "dbconnectmysql.php"; //carrega o arquivo de configuração do banco de dados

if (isset($_COOKIE["user"])) {$user = $_COOKIE["user"];}//pegamos o cookie user, gravado em gravar_login.php
if (isset($_COOKIE["pass"])) {$pass = $_COOKIE["pass"];}//pegamos o cookie pass, gravado em gravar_login.php

if (isset($user) && isset($pass))//vamos ver se os dados estão simultaneamente setados...
	{
	$sqlquery = "SELECT * FROM users WHERE user = '$user' AND pass = '$pass'";
	$resultado = mysql_query($sqlquery); 
	//Esta consulta verifica se o conteudo dos cookies esta correto.
	//Se der 0, não coincide algo, e a entrada será proibida:
	if (mysql_num_rows($resultado) == 0) {$logado = false;}
	//Se der 1, está certo. Se der mais de 1, é porque está duplicado o login e a senha.
	//Tecnicamente é um erro, mas vamos aceitar mesmo assim.
	else {$logado = true;}
	//vamos aproveitar que estamos aqui e pegar os todos dados do usuário.
	$dadosdousuario = mysql_fetch_array($resultado);
	$user = $dadosdousuario['user'];
	$admin = $dadosdousuario['admin'];
	
	}
else {$logado = false;}//se nem $user nem $pass estiverem setados, o segurança barra.
//De posse da booleana $logado, vamos seguir em frente. Dois blocos de condicionais, então.
//O primeiro barra tudo e manda o vagabundo se logar.
//O segundo mostra a barrinha de usuário com as informações do acesso, atalhos e permite o uso das páginas /admin.
if ($logado == false) {
include 'loginform.php';
	}

if ($logado == true) {
echo "Bem vindo $user. <br/><a href='sair.php'>Sair</a>";	}
?>