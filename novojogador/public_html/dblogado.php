<?php
//este código, que carrega no início dá página, recebe o login e grava o cookie do login (action gravarlogin)
//também desloga o caboclo (action logoff).

if (isset($_GET['action'])){

if ($_GET['action']=="gravarlogin") {

	if (isset($_POST["user"])) {
		$user = $_POST["user"];
	}//recebe o form;
	if (isset($_POST["pass"])) {
		$pass = $_POST["pass"];
	}//recebe o form;
	if (isset($_SESSION["parg"])) {
		$parg = $_SESSION["parg"];}

	if (isset($user) && isset($pass))//vamos ver se os dois estão simultaneamente setados...
	{
		$sqlquery = "SELECT * FROM users WHERE user = '$user' AND pass = '$pass'";
		$resultado = mysql_query($sqlquery) or die("não conecta na base de dados");
		//Esta consulta verifica se o conteudo da form esta correto.
		//Se der 0, não coincide algo, e a o usuário não fica logado:

		if (mysql_num_rows($resultado) == 0) {
			$logado = false;
		}
		//Se der 1, está certo. Se der mais de 1, é porque está duplicado o login e a senha na base.
		//Tecnicamente é um erro, mas como ninguém morre vamos aceitar mesmo assim.
		else {$logado = true;
		$dadosuser=mysql_fetch_array($resultado);
		$userid=$dadosuser['id'];
		}
	}
	else {$logado = false;
	}//se nem $user nem $pass estiverem setados, o segurança barra.
	//Esta consulta verifica se os dados do form estão corretos.
	//Se der 0, não coincide algo, e a entrada será proibida.

	if ($logado == true){
		setcookie ("user", $user); //grava o cookie com o login
		setcookie ("pass", $pass); //grava o cookie com a senha
	}
	$_GET['action']="game";
	$_SESSION['userid'] = $userid;
}

if ($_GET['action']=="logoff") {


	setcookie("user","",time()-3600);
	setcookie("pass","",time()-3600);
	$logado = false;
	$_GET['action']="game";
}
}



?>