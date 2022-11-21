# Brasileirão 2022 
Esse projeto consiste em extrair dados dos gols e assistencias  do campeonato brasileiro de futebol do ano de 2022. Esses dados são extraidos do site de estatísticas da ESPN("https://www.espn.com.br/futebol/estatisticas/_/liga/BRA.1/vista/gols"). Após a etapa de coleta, esses dados foram salvo em 2 banco de dados diferentes: Postgresql e Mongodb.

## Arquivos
* **insert_postgres.py**: Arquivo que faz a extraçao dos dados e os salva no banco de dados postgres.
* **insert_mongo.py**: Arquivo que faz a extraçao dos dados e os salva MongoDB.
* **src/extract.py**: Nesse arquivo estão presentes as funções que fazem  a extraçao dos dado presente na tabela do site.
* **src/ConnectPostgres.py**: Nesse arquivo contem as funções para fazer a conexão e as inserções dos dados nas tabelas.
* **sql/table.sql**: Arquivo de script para a criação das tabelas no postgre.

## Execução

* Para inserir os dados no Postgresql, primeiramente é necessário executar o arquivo **table.sql**. Com a execução será criada a base de dados **brasileirao** e duas tabelas: artilheiros e assistencia.Depois, basta executar o arquivo **insert_postgres.py**, adicionando os parametro de conexão com o banco de dados que os dados serão inseridos no banco de dados.

* Para inserir os dados no MongDB, basta executar  o arquivo **insert_mongo.py**.Adicione os dados de conexao com o Mongodb. Com a execução, será criado a base de dados brasileirao e 2 coleções: artilheiros e assistencia. Os dados extraidos do site serão adicionados as suas respectivas coleções.   