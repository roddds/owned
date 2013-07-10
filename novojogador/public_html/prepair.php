<?php
if (isset($_GET['param'])) {
	$param = explode("/",$_GET['param']);
	$classe = $param[0] . "Controller";
	if ((isset($param[1])) && ($param[1] != ""))
	{
		$metodo = $param[1];
	}
	else
	{$metodo = "Index";
	}

	$controlador = new $classe();
	$controlador->$metodo();
}

else {
	$classe = "IndexController";
	$metodo = "Index";

}
?>