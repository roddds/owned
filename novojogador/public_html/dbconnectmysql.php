<?
header('Content-Type:text/html; charset=UTF-8');

ini_set('default_charset','UTF-8'); // Para o charset das páginas e


$mdbusuario='simonecamp_1';
$mdbsenha='livrojogo';
//$mdbservidor='localhost';
$mdbservidor='dbmy0031.whservidor.com';
$mdbbase='simonecamp_1';
@mysql_connect($mdbservidor,$mdbusuario,$mdbsenha) or die('Problema na Conexão com o Banco de Dados Mysql');
@mysql_select_db($mdbbase) or die('Problema na Conexão com o Banco de Dados ' . $mdbbase);

mysql_set_charset('utf8'); // para a conexão com o MySQL

mysql_query("SET NAMES 'utf8'");
mysql_query('SET character_set_connection=utf8');
mysql_query('SET character_set_client=utf8');
mysql_query('SET character_set_results=utf8');
?>