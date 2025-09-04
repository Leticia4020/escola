<?php
$nomes = array("Ana","Adriano","Marcio","Claudio","José","Maria",);
$nomes = ["Roberto", "Carlos", "João" ];
$pessoa = [
    "nome"=> "Leticia",
    "idade"=> "20",
    "cidade"=> "Santa luzia",
];
echo $pessoa["nome"];

$usuaríos = [
    ["nome" => "Ana", "idade" => 20],
    ["nome"=> "Carlos", "idade"=> 25],
    ["nome"=> "Roberto", "idade"=> 50],
];
 echo $usuaríos[1]["nome"];
 echo $usuaríos[1]["idade"];

 $lista=[];
?>
<br><br>
<?php
 $cidade = ["Lagoa","lua","mar","ceu","areia","praia"];
 echo $cidade[0];
 echo $cidade[5];
 
?>
<?php
$numero=[10,20,30,40,50];
$soma=array_sum($numero);
$quantidade=count($numero);
$media=$quantidade / $soma;
echo "A media é " . $media ." A soma é " . $soma;

?>
<br><br>
<?php
$numeros=[7,3,9,1,12];
$max=max($numeros);
$min=min($numeros);
echo "maior é " . $max ." menor e" . $min;

?>
<?php
$aluna = [
    "nome"=>"eticia",
    "idade" =>33,
    "curso"=> "php",
];
echo " o aluno " . $aluna["nome"] . " tem " . $aluna["idade"] ." anos e estuda ". $aluna["curso"];

?>