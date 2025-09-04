CREATE DATABASE triagem;
USE triagem;

CREATE TABLE pacientes (
    id int auto_increment primary key,
    nome varchar(150) not null,
    idade int not null,
    sexo varchar(10),
    data_nascimento date not null,
    cpf varchar(20) not null,
    telefone varchar(20) not null,
    endereco varchar(200) not null,
    sintomas text not null,
    inicio_sintomas date not null,
    doencas text not null,
    medicamentos text not null,
    alergias text not null,
    pressao varchar(200) not null,
    temperatura varchar(200) not null,
    cardiaca varchar(200) not null,
    saturacao varchar(200) not null,
    observacoes text not null,
    
    
    criado_em timestamp default current_timestamp
)