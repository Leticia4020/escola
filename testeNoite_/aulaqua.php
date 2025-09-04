<?php
if($_SERVER["REQUEST_METHOD"]== "POST"){
   include "aulasexcox.php";
   $nome=  $_POST["nome"];
   $idade= $_POST["idade"] ;
   $sexo=  $_POST["sexo"];
   $data_nascimento=  $_POST["Data_de_Nascimento"];
   $cpf=  $_POST["CPF"];
   $telefone=  $_POST["Telefone"];
   $endereco=  $_POST["Endereco"];
   $sintomas=  $_POST["sintomas"];
   $inicio_sintomas=  $_POST["inicio_sintomas"];
   $doencas=  $_POST["doencas"];
   $medicamentos=  $_POST["medicamentos"];
   $alergias=  $_POST["alergias"];
  $pressao=  $_POST["pressao"];
   $temperatura=  $_POST["temperatura"];
   $cardiaca=  $_POST["cardiaca"];
   $saturacao=  $_POST["saturacao"];
   $observacao=  $_POST["observacao"];
   $sql = "INSERT INTO pacientes(nome,idade,sexo,data_nascimento,
   cpf,telefone,endereco,sintomas,inicio_sintomas,
   doencas,medicamentos,alergias,pressao,temperatura,
   cardiaca,saturacao,observacoes)VALUES('$nome','$idade','$sexo','$data_nascimento',
   '$cpf','$telefone','$endereco','$sintomas','$inicio_sintomas',
   '$doencas','$medicamentos','$alergias','$pressao','$temperatura',
   '$cardiaca','$saturacao','$observacao')";
    
}
?>
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paciente Cadrastrado</title>
</head>
<body>
    <div class = "container">
<?php
if($coon ->query($sql) == TRUE){
echo "<h2>Paciente Cadrastrado com sucesso</h2>";
echo "<div class='paciente'></div>";
echo"<b> Nome:</b> $nome <br>";
    echo"<b>Idade: </b> $idade <br>";
    echo"<b>Sexo : </b> $sexo <br>";
    echo"<b>Data de Nascimento: </b> $data_nascimento <br>";
    echo"<b>CPF: </b> $cpf <br>";
    echo"<b>Telefone: </b> $telefone <br>";
    echo"<b>Endereço: </b> $endereco <br>";
    echo"<b>Sintomas : </b> $sintomas <br>";
    echo"<b>Inicio dos sintomas: </b> $inicio_sintomas <br>";
    echo"<b>Doenças: </b> $doencas <br>";
    echo"<b>Medicamentos: </b> $medicamentos <br>";
    echo"<b>Alergias: </b> $alergias <br>";
    echo"<b>Pressão : </b> $pressao <br>";
    echo"<b>Temperatura: </b> $temperatura <br>";
    echo"<b>Cardiaca : </b> $cardiaca <br>";
    echo"<b>Saturação: </b> $saturacao <br>";
    echo"<b>Observação: </b> $observacao <br>";






}else{
echo"<p> Erro ao cadastrar Paciente" .
$coon->error . "</p>";
}
$coon->close();
?>
    </div>
</body>
</html>