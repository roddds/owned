<?php

if (isset($_POST["user"])) {$userc = $_POST["user"];}
if (isset($_POST["email"])) {$emailc = $_POST["email"];}
if (isset($_POST["pass1"])) {$pass1c = $_POST["pass1"];}
if (isset($_POST["pass2"])) {$pass2c = $_POST["pass2"];}

$erros=0;

//verificar se existe tudo

if ($userc != "") {}
else {
	echo "<p>Erro: Voc&ecirc; n&atilde;o escolheu um nome de usu&aacute;rio v&aacute;lido.</p>";
	$erros=1;
}

if (($emailc != "") && (verificar_email($emailc)==1)) {
}
else {
	echo "<p>Erro: Voc&ecirc; n&atilde;o escolheu um e-mail v&aacute;lido.</p>";
	$erros=1;
}

if ($pass1c != "") {
}
else {
	echo "<p>Erro: Voc&ecirc; n&atilde;o escolheu um a senha v&aacute;lida.</p>";
	$erros=1;
}

if ($pass2c = $pass1c) {
}
else {
	echo "<p>Erro: Voc&ecirc; n&atilde;o confirmou a senha corretamente.</p>";
	$erros=1;
}


//OK, se nenhum erro pipocou, gravando o cadastro então.

if ($erros==0){

$query = "INSERT INTO `users` (`user`, `pass`, `email`) VALUES ('$userc', '$pass1c', '$emailc')";
$resultado = mysql_query($query) or die(mysql_error());
if ($resultado) {
	echo "<p>Usu&aacute;rio cadastrado com sucesso!</p>";
} 



}

?>