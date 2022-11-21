CREATE DATABASE brasileirao;

CREATE SCHEMA dados;

CREATE SEQUENCE dados.idartilheiro;
CREATE TABLE artilheiros (
    id_jogador INT DEFAULT NEXTVAL('dados.idartilheiro'::regclass) PRIMARY KEY,
    nome VARCHAR(100),
    clube VARCHAR(50),
    n_jogos INT,
    n_gols INT  
);

CREATE SEQUENCE dados.idassistente;
CREATE TABLE assistencia(
    id_jogador INT DEFAULT NEXTVAL('dados.idassistente'::regclass) PRIMARY KEY,
    nome VARCHAR(100),
    clube VARCHAR(50),
    n_jogos INT,
    n_assistencias INT  
);