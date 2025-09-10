<?php
if($_SERVER["REQUEST_METHOD"]== "POST"){
    include "aulasegcox.php";
    $nome= $_POST["nome"];
    $email= $_POST["email"];
    $senha= $_POST["senha"];

    $sql_check="SELECT COUNT(*) FROM pacientes WHERE email = '$email'";
    $result_check =$coon->query($sql_check);
    $row=$result_check->fetch_assoc();
    $count=$row['COUNT(*)'];
    if ($count > 0){
        echo "Usuario já existe!";
    } else {
       echo "<h2>Cadrastrado com sucesso</h2>";
       echo"<b>Bem vindo</b> $nome <br>";
       
    }

    $sql = "INSERT INTO pacientes(nome,email,senha)VALUES('$nome','$email','$senha')";

}
?>