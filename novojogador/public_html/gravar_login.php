<?php 
include "functions.php";
include "dbconnectmysql.php"; //inclui o arquivo de configura��es
if (isset($_POST["user"])) {$user = $_POST["user"];}//recebe o form;
if (isset($_POST["pass"])) {$pass = $_POST["pass"];}//recebe o form;

if (isset($user) && isset($pass))//vamos ver se os dois est�o simultaneamente setados...
	{
	$sqlquery = "SELECT * FROM users WHERE user = '$user' AND pass = '$pass'";
	$resultado = mysql_query($sqlquery) or die("n�o conecta na base de dados");
	//Esta consulta verifica se o conteudo da form esta correto.
	//Se der 0, n�o coincide algo, e a o usu�rio n�o fica logado:
	if (mysql_num_rows($resultado) == 0) {$logado = false;}
	//Se der 1, est� certo. Se der mais de 1, � porque est� duplicado o login e a senha na base.
	//Tecnicamente � um erro, mas como ningu�m morre vamos aceitar mesmo assim.
	else {$logado = true;}
	}
else {$logado = false;}//se nem $user nem $pass estiverem setados, o seguran�a barra.
//Esta consulta verifica se os dados do form est�o corretos.
//Se der 0, n�o coincide algo, e a entrada ser� proibida.

if ($logado == true){
  setcookie ("user", $user); //grava o cookie com o login
  setcookie ("pass", $pass); //grava o cookie com a senha
  echo "Usu�rio logado. <br/><a href='index.php'>Voltar para a p�gina principal</a>"; //se a senha digitada est� correta, mostra essa mensagem
} 
else {
  echo "Matr�cula ou senha inv�lidos"; //se a senha est� incorreta mostra essa mensagem
  }
?>
