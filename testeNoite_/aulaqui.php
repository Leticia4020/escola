<?php
if($_SERVER["REQUEST_METHOD"]== "POST"){
    $nome = $_POST["nome"];
    $numero = isset($_POST["hospede"]) ;
    $check_out = $_POST["check-out"];
    $check_in =  $_POST["check-in"];
    echo"<h2>Dados cadastrados</h2>";
    echo"Nome: " . $nome . "<br>";
    echo"Número de hóspede: " . $numero . "<br>";
    echo"Check-in : " . $check_in . "<br>";
    echo"Check-out: " . $check_out . "<br>";

}
if($check_out < $check_in){
    echo"Check-out menor que a data do Check-in";
}