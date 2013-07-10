<?php

if (isset ($_GET['action'])) {$action = $_GET['action'];} else {$action = "newgame";}

include_once "actions/$action.php";

?>