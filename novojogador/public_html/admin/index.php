
<?php
include "../dbconnectmysql.php";
include "../functions.php";
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Owned - Um Novo Jogador</title>
<link href="../css/fbstyles.css" rel="stylesheet" type="text/css" />
</head>

<body>

<?php 
Echo "Página de Administração.";

Echo "<br/>";

Echo "Você deseja...";

criabotao("Editar ou Criar Jogos", "edita.php", "games", "all");

Echo "<br/>";

criabotao("Editar ou Criar Parágrafos", "edita.php", "pargs", "all");

Echo "<br/>";

criabotao("Editar ou Criar Itens", "edita.php", "items", "all");

Echo "<br/>";

criabotao("Editar ou Criar Flags", "edita.php", "flags", "all");

Echo "<br/>";

criabotao("Gerenciar Eventos", "edita.php", "events", "all");

Echo "<br/>";

criabotao("Gerenciar Usuários", "edita.php", "jogos", "all");

Echo "<br/>";



?>

</body>
</html>

