<?php

if (isset($_SESSION['parg'])){$parg=$_SESSION['parg'];} else {$parg=1;}
if (isset($logado)){} else {$logado=false;}

if ($logado==false){
	echo "
	<form id='form1' name='form1' method='post' action='index.php?action=gravarlogin'>
		<label for='login'><strong class='fonte9'>LOGIN:</strong><strong class='corrier'> </strong></label>
		<input name='user' type='text' id='user' size='12' />
		<span class='sdc'><strong class='fonte9'>SENHA:</strong></span><strong class='fonte9'>
		<input name='pass' type='password' id='pass' size='12' maxlength='8' />
		<input name='submit' type='submit' value='OK' id='submit' />
	<a href='index.php?action=cadastrar' style='text-decoration: none'><span class='black'>....</span><span class='orange'>Cadastrar</span> <span class='black'>....</span></a>
	<a href='index.php?action=esqueci' style='text-decoration: none'><span class='black'>....</span><span class='orange' font-size='8px'>Esqueci minha senha!</span> <span class='black'>....</span></strong></a>
	</form>
	";}

	if ($logado==true){
		echo "
			<span class='sdc'><strong class='fonte9'>Ol&aacute;, $user!  </strong></span><strong class='fonte9'>
			<a href='index.php?action=logoff' style='text-decoration: none'><span class='black'>....</span><span class='orange'>Sair</span> <span class='black'>....</span></strong></a>
		";
	}

