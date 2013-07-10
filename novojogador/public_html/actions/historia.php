<?php

//TEXTO

mostraparagrafo($game, $parg);
echo "<br/>";

mostraopcao($game, $parg, 1);
echo "<br/>";

mostraopcao($game, $parg, 2);
echo "<br/>";

mostraopcao($game, $parg, 3);
echo "<br/>";

mostraopcao($game, $parg, 4);
echo "<br/>";

mostraopcao($game, $parg, 5);
echo "<br/>";

mostraparagrafo2($game, $parg);
echo "<br/>";

atualizaitens();
atualizaflags();
$_SESSION['parg']=$parg;


?>