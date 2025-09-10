CREATE DATABASE login;
USE login;

CREATE TABLE pacientes (
    id int auto_increment primary key,
    nome varchar(150) not null,
    senha text not null,  
    email varchar(200) not null,
    
    
    criado_em timestamp default current_timestamp
)