<?php
include "dbconnectmysql.php";
include "functions.php";
include "functions2.php";
include "cookielogado.php";
include "dblogado.php";


session_start();
if (isset ($_SESSION['itens'])) {$itens = $_SESSION['itens'];} else
	{
	$itens = array();
	$_SESSION['itens'] = $itens;
	}

if (isset ($_SESSION['flags'])) {$flags = $_SESSION['flags'];} else
	{
	$flags = array();
	$_SESSION['flags'] = $flags;
	}

if (isset ($_SESSION['options'])) {
		$options = $_SESSION['options'];
	} else
	{
		$options = array();
		$_SESSION['options'] = $options;
	}


?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<?php
include "sharefacebook.php";
?>

<title>Owned - Um Novo Jogador</title>

<script type="text/javascript" async="" src="./js/ga.js"></script>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3/jquery.min.js"></script>
<script type="text/javascript">

$(document).ready(function() {

	//Default Action
	$(".tab_content").hide(); //Hide all content
	$("ul.tabs li:first").addClass("active").show(); //Activate first tab
	$(".tab_content:first").show(); //Show first tab content

	//On Click Event
	$("ul.tabs li").click(function() {
		$("ul.tabs li").removeClass("active"); //Remove any "active" class
		$(this).addClass("active"); //Add "active" class to selected tab
		$(".tab_content").hide(); //Hide all tab content
		var activeTab = $(this).find("a").attr("href"); //Find the rel attribute value to identify the active tab + content
		$(activeTab).fadeIn(); //Fade in the active content
		return false;
	});

});
</script>

<link href="css/fbstyles.css" rel="stylesheet" type="text/css" />
<link href="css/tabs.css" rel="stylesheet" type="text/css" />

<style type="text/css">

body {
	background: url(./images/fundo_index.jpg) fixed no-repeat center;
	font-family: "Arial Black", Gadget, sans-serif;
	color: #CCC;
}
#Table_01 tr td strong {
	color: #000;
	font-family: Verdana, Geneva, sans-serif;
}
.fonte9 {
	font-size: 9px;
}
#Table_01 tr td .fonte9 {
	font-size: 10px;
}
#Table_01 tr td .fonte9 {
	font-size: 12px;
	font-family: "Lucida Console", Monaco, monospace;
}
#Table_01 tr td .fonte9 {
	font-family: "Arial Black", Gadget, sans-serif;
	text-align: right;
	color: #CCC;
}
.tahoma {
	font-family: Tahoma, Geneva, sans-serif;
}
.corrier {
	font-family: "Courier New", Courier, monospace;
}
.corrier {
	font-family: "Courier New", Courier, monospace;
}
#Table_01 tr td #form1 label .corrier {
	font-family: Arial, Helvetica, sans-serif;
	font-weight: bold;
	}




.sdc {
	color: #F00;
}
.black {
	color: #000;
	font-family: "Arial Black", Gadget, sans-serif;
}
.orange {
	color: #F90;
	font-family: "Arial Black", Gadget, sans-serif;
}
#Table_01 tr td table tr td p {
	font-weight: bold;
}
#Table_01 tr td table tr td p {
	font-weight: normal;
}
#Table_01 tr td table tr td p {
	font-family: Arial, Helvetica, sans-serif;
}
#Table_01 tr td table tr td p {
	color: #333;
	font-family: Arial, Helvetica, sans-serif;
}
#Table_01 tr td table tr td p b {
	color: #396CDF;
}

h3 {
	color: #57a1eb;
}


#Table_01 tr td .conteudo	{
height: 100%;
/* background:url("/images/imgmarcador.jpg") no-repeat; */
vertical-align:text-top;
}

</style>

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-27331837-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>


</head>

<body>
<table width="100%" border="0">
  <tr>
    <td width="12%">&nbsp;</td>
    <td width="81%">
    
    <table id="Table_01" width="924" height="1089" border="0" cellpadding="0" cellspacing="0" align="center">
      <tbody>
        <tr>
        
          <td rowspan="11"><img src="./images/ownedlayout_01.png" width="33" height="1089" alt="" /></td>
          <td><img src="./images/ownedlayout_02.jpg" width="1" height="45" alt="" /></td>
          <td colspan="4" align="right" background="./images/ownedlayout__03.jpg">
         
	  <?php include "loginform.php";?>
          
          </td>
          <td rowspan="11"><img src="./images/ownedlayout_04.png" width="31" height="1089" alt="" /></td>
          <td><img src="./images/spacer.gif" width="1" height="45" alt="" /></td>
        </tr>
        <tr>
          <td rowspan="7"><img src="./images/ownedlayout_05.jpg" width="1" height="259" alt="" /></td>
          <td rowspan="7"><a href="http://www.novojogador.com.br/index.php?action=game"><img src="./images/ownedlayout_06.jpg" width="476" height="259" alt="" /></a></td>
          <td><img src="./images/ownedlayout_07.jpg" width="178" height="70" alt="" /></td>
          <td><img src="./images/ownedlayout_08.jpg" alt="" width="178" height="70" border="0" usemap="#Map2Map" /></td>
          <td rowspan="6"><img src="./images/ownedlayout_09.jpg" width="26" height="258" alt="" />
          </td>
          <td><img src="./images/spacer.gif" width="1" height="70" alt="" />
          </td>
        </tr>
        
        <?php include "menu.php";?>
        
        
        <tr>
          <td rowspan="2"><img src="./images/ownedlayout_18.jpg" width="178" height="52" alt="" /></td>
          <td rowspan="2"><img src="./images/ownedlayout_19.jpg" width="178" height="52" alt="" /></td>
          <td><img src="./images/spacer.gif" width="1" height="51" alt="" /></td>
        </tr>
        <tr>
          <td><img src="./images/ownedlayout_20.jpg" width="26" height="1" alt="" /></td>
          <td><img src="./images/spacer.gif" width="1" height="1" alt="" /></td>
        </tr>
        <tr>
          <td style="vertical-align:top" colspan="5" background="./images/ownedlayout_21.jpg"><table width="100%" height="100%" border="0">
            <tbody>
              <tr></tr>
              <tr>
                <td height="0" width="10%">&nbsp;</td>
                <td class="conteudo">
                
       			<?php include "actions/principal.php";?>
                
                </td>                
                <td width="25%">&nbsp;</td>
              </tr>
            </tbody>
          </table></td>
          <td><img src="./images/spacer.gif" width="1" height="571" alt="" /></td>
        </tr>
        <tr>
          <td><img src="./images/ownedlayout_22.jpg" width="1" height="66" alt="" /></td>
          <td colspan="4"><img src="./images/ownedlayout_23.jpg" width="858" height="66" alt="" /></td>
          <td><img src="./images/spacer.gif" width="1" height="66" alt="" /></td>
        </tr>
        <tr>
          <td colspan="5"><img src="./images/ownedlayout_24.jpg" alt="" width="859" height="148" border="0" usemap="#MapMap" /></td>
          <td><img src="./images/spacer.gif" width="1" height="148" alt="" />
          </td>
        </tr>
      </tbody>
    </table>
    
      <map name="MapMap" id="MapMap">
        <area shape="rect" coords="140,15,224,35" href="http://www.novojogador.com.br/index.php?action=down" alt="Clique para baixar o Owned" />
        <area shape="rect" coords="140,41,223,60" href="http://www.novojogador.com.br/index.php?action=participe" alt="Clique para participar do Owned" />
        <area shape="rect" coords="250,13,347,36" href="http://www.novojogador.com.br/index.php?action=blog" alt="Acesse o blog do Owned" />
        <area shape="rect" coords="250,40,353,60" href="http://www.novojogador.com.br/index.php?action=creditos" alt="Veja quem fez o Owned" />
        <area shape="rect" coords="372,14,477,36" href="http://www.novojogador.com.br/index.php?action=recomendacoes" alt="Materiais recomendados pra quem gostou do Owned" />
        <area shape="rect" coords="372,39,433,61" href="http://www.novojogador.com.br/index.php?action=faq" alt="Possui alguma dúvida?" />
        <area shape="rect" coords="15,73,401,142" href="http://creativecommons.org/licenses/by-nc-sa/3.0/" />
      </map>
      <map name="Map2Map" id="Map2Map">
        <area shape="rect" coords="95,19,129,51" href="https://twitter.com/share?url=http://www.novojogador.com.br&amp;text=Estou%20jogando%20OWNED!%20-%20Um%20Novo%20Jogador,%20de%20Simone%20Campos!&amp;via=owned_jogador&amp;lang=pt" target="_blank" />
        <area shape="rect" coords="146,21,176,52" href="http://www.facebook.com/sharer.php?u=http://www.novojogador.com.br?f=facebook" target="_blank" alt="facebook" />
    </map></td>
    <td width="7%">&nbsp;</td>
  </tr>
</table>
<map name="Map" id="Map">
  <area shape="rect" coords="140,15,224,35" href="http://www.novojogador.com.br/index.php?action=down" alt="Clique para baixar o Owned">
  <area shape="rect" coords="140,41,223,60" href="http://www.novojogador.com.br/index.php?action=participe" alt="Clique para participar do Owned">
  <area shape="rect" coords="250,13,347,36" href="http://www.novojogador.com.br/index.php?action=blog" alt="Acesse o blog do Owned">
  <area shape="rect" coords="250,40,353,60" href="http://www.novojogador.com.br/index.php?action=creditos" alt="Veja quem fez o Owned">
  <area shape="rect" coords="372,14,477,36" href="http://www.novojogador.com.br/index.php?action=recomendacoes" alt="Materiais recomendados pra quem gostou do Owned">
  <area shape="rect" coords="372,39,433,61" href="http://www.novojogador.com.br/index.php?action=faq" alt="Possui alguma dúvida?">
  <area shape="rect" coords="15,73,401,142" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">
</map>

<map name="Map2" id="Map2">

  <area shape="rect" coords="95,19,129,51" href="https://twitter.com/share?url=http://www.novojogador.com.br&text=Estou%20jogando%20OWNED!%20-%20Um%20Novo%20Jogador,%20de%20Simone%20Campos!&via=owned_jogador&lang=pt" target="_blank">


<area shape="rect" coords="146,21,176,52" href="http://www.facebook.com/sharer.php?u=http://www.novojogador.com.br?f=facebook" target="_blank" alt="facebook">


</map>





</body></html>

<?php
@mysql_close();
?>
