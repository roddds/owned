<?php
//página de teste de exibição.


//pega o jogo do POST
if (isset($_SESSION['game'])) {
} else {$_SESSION['game']=(int)1;
}
if (isset($_POST['game'])) {
	$game=(int)$_POST['game'];
} else {$game=$_SESSION['game'];}


//pega o parágrafo do POST
if (isset($_POST['parg'])) {$parg=$_POST['parg'];}
else {
	if (isset($_SESSION['parg'])) {$parg=$_SESSION['parg'];}
	else {$parg=(int)1;}
	}
$_SESSION['parg']=$parg;


//pega o disclaimer do POST
if (isset($_SESSION['disclaimer'])) {
	$disclaimer=$_SESSION['disclaimer'];
} else {$_SESSION['disclaimer']=false;
}

if (isset($_POST['disclaimer'])) {
	$disclaimer=$_POST['disclaimer'];
} else {$disclaimer=$_SESSION['disclaimer'];
}

$_SESSION['disclaimer']=$disclaimer;


if ($disclaimer==false){
include "actions/newgame.php";
}

else {

echo "<ul class='tabs'>";
echo "    <li><a href='#tab1'>Hist&oacute;ria</a></li>";
echo "<li><a href='#tab2'>Invent&aacute;rio</a></li>";
echo "   <li><a href='#tab3'>Menu</a></li>";
echo "</ul>";


echo "<div class='tab_container' style='font-size: 12px;'>";
echo "    <div id='tab1' class='tab_content'>";

include "actions/historia.php";

echo "    </div>";
echo "    <div id='tab2' class='tab_content'>";

include "actions/inventario.php";

echo "    </div>";
echo "    <div id='tab3' class='tab_content'>";
include "actions/system.php";
echo "    </div>";

echo "</div>";

}



