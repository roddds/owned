	<?php
	//seleciona a imagem dependendo da action.

	$imagedown="images/ownedlayout_12.jpg";
	$imagecreditos="images/ownedlayout_13.jpg";
	$imageparticipe="images/ownedlayout_14.jpg";
	$imagerecomendacoes="images/ownedlayout_15.jpg";
	$imageblog="images/ownedlayout_16.jpg";
	$imagefaq="images/ownedlayout_17.jpg";

	if (isset($_GET['action'])) {$action=$_GET['action'];} else {$action="";}

	switch ($action){
		case "down":
			$imagedown="images/ownedlayout__12.jpg";
			break;
		case "creditos":
			$imagecreditos="images/ownedlayout__13.jpg";
			break;
		case "participe":
			$imageparticipe="images/ownedlayout__14.jpg";
			break;
		case "recomendacoes":
			$imagerecomendacoes="images/ownedlayout__15.jpg";
			break;
		case "blog":
			$imageblog="images/ownedlayout__16.jpg";
			break;
		case "faq":
			$imagefaq="images/ownedlayout__17.jpg";
			break;
	}




	?>

	<tr>
		<td>
			<a href="index.php?action=glossario"><img src="images/ownedlayout_10.jpg" width="178" height="34" alt=""></a></td>
		<td>
			<a href="index.php?action=comojogar"><img src="images/ownedlayout_11.jpg" width="178" height="34" alt=""></a></td>
		<td>
			<img src="images/spacer.gif" width="1" height="34" alt=""></td>
	</tr>
		<tr>
		<td><a href="index.php?action=down"><img src="<?php echo $imagedown;?>" width="178" height="35" alt=""></a></td>
		<td><a href="index.php?action=creditos"><img src="<?php echo $imagecreditos;?>" width="178" height="35" alt=""></a></td>
		<td>
			<img src="images/spacer.gif" width="1" height="35" alt=""></td>
	</tr>
	<tr>
		<td><a href="index.php?action=participe"><img src="<?php echo $imageparticipe;?>" width="178" height="35" alt=""></a></td>
		<td><a href="index.php?action=recomendacoes"><img src="<?php echo $imagerecomendacoes;?>" width="178" height="35" alt=""></a></td>
		<td>
			<img src="images/spacer.gif" width="1" height="35" alt=""></td>
	</tr>
	<tr>
		<td><a href="index.php?action=blog"><img src="<?php echo $imageblog;?>" width="178" height="33" alt=""></a></td>
		<td><a href="index.php?action=faq"><img src="<?php echo $imagefaq;?>" width="178" height="33" alt=""></a></td>
		<td>
			<img src="images/spacer.gif" width="1" height="33" alt=""></td>
	</tr>






