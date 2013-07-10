<?php
setcookie("user","",time()-3600);
setcookie("pass","",time()-3600);

echo "Você saiu do sistema.";
echo "<br/><a href='index.php'>Voltar para a página principal</a>";

?>