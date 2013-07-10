<?php
//este script tem funções coletadas da Internet.

//FUNÇÃO VERIFICAR EMAIL (http://www.criarweb.com/artigos/185.php)
function verificar_email($email){ 
   $mail_correcto = 0; 
   //verifico umas coisas 
   if ((strlen($email) >= 6) && (substr_count($email,"@") == 1) && (substr($email,0,1) != "@") && (substr($email,strlen($email)-1,1) != "@")){ 
      if ((!strstr($email,"'")) && (!strstr($email,"\"")) && (!strstr($email,"\\")) && (!strstr($email,"\$")) && (!strstr($email," "))) { 
         //vejo se tem caracter . 
         if (substr_count($email,".")>= 1){ 
            //obtenho a terminação do dominio 
            $term_dom = substr(strrchr ($email, '.'),1); 
            //verifico que a terminação do dominio seja correcta 
         if (strlen($term_dom)>1 && strlen($term_dom)<5 && (!strstr($term_dom,"@")) ){ 
            //verifico que o de antes do dominio seja correcto 
            $antes_dom = substr($email,0,strlen($email) - strlen($term_dom) - 1); 
            $caracter_ult = substr($antes_dom,strlen($antes_dom)-1,1); 
            if ($caracter_ult != "@" && $caracter_ult != "."){ 
               $mail_correcto = 1; 
            } 
         } 
      } 
   } 
} 

if ($mail_correcto) 
   return 1; 
else 
   return 0; 
} 


function alternative_file_get_contents($url){
 $header[] = $_SERVER["HTTP_ACCEPT"];
 $ch = curl_init();
 $timeout = 0;
 curl_setopt ($ch, CURLOPT_URL, "$url");
 curl_setopt ($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
 curl_setopt ($ch, CURLOPT_HTTPHEADER, $header);
 curl_setopt ($ch,  CURLOPT_FOLLOWLOCATION, true);
 curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
 curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
 $file_contents =  curl_exec($ch);
 curl_close($ch);
 return $file_contents;
}

function alternative_file($url){
 $header[] = $_SERVER["HTTP_ACCEPT"];
 $ch = curl_init();
 $timeout = 0;
 curl_setopt ($ch, CURLOPT_URL, "$url");
 curl_setopt ($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
 curl_setopt ($ch, CURLOPT_HTTPHEADER, $header);
 curl_setopt ($ch,  CURLOPT_FOLLOWLOCATION, true);
 curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
 curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
 $file_contents =  curl_exec($ch);
 curl_close($ch);
 $lines = array();
 $lines = explode("\n", $file_contents);
 return $lines;
}

?>