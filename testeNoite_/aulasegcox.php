<?php
$host="localhost";
$user= "root";
$pass= "aluno";
$databse= "login";

$coon = new mysqli($host,$user,$pass,$databse);
if ($coon->connect_error){
    http_response_code(500);
    echo json_encode(["erro" => "falha na conecção"],json_uninescaped_unicode);
exit();
}  
?>