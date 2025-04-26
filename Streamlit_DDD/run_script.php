<?php
// Simple PHP code to run a Python script
$output = shell_exec("python3 app.py");
echo $output;
?>