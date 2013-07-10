<?php
if (isset($_GET['action'])) {$action = $_GET['action'];} else {$action = "principal";}

include "actions/$action.php";

?>

