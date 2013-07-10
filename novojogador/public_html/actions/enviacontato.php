<?php
//pegar os dados do post
if (isset($_POST['mensagem']))
	{$mensagem=$_POST['mensagem'];
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



$to = "'Douglas Donin' <douglasdnn@gmail.com>";
$subject = "[Contato OWNED!] $assunto";

$message = wordwrap($mensagem);

$headers = "From: $remetente <$email>" . "\n";
$headers .= 'MIME-Version: 1.0' . "\n";
$headers .= 'Content-type: text/html; charset=utf-8' . "\r\n";

if (mail($to, $assunto, $mensagem, $headers)) {
  echo 'mail() Success!' . "<br />\n";
}
else {
  echo 'mail() Failure!' . "<br />\n";
}





?>
