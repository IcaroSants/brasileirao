from src.extract import Extract
import pymongo 
client = pymongo.MongoClient("????")

banco = client["dbBrasileirao"]
colecao = banco["artilheiro"]

extract = Extract("https://www.espn.com.br/futebol/estatisticas/_/liga/BRA.1/vista/gols")

tbodies = extract.get_table("tbody",{"class":"Table__TBODY"})
    
registros = extract.get_register(tbodies[0])
registros_gols = extract.organize_information(["nome","clube","n_jogos","n_gols"],registros)

result = colecao.insert_many(registros_gols)

print("artilheiros inseridos:",result.inserted_ids)

colecao = banco["assistencia"]

registros = extract.get_register(tbodies[1])
registros_assistencia = extract.organize_information(["nome","clube","n_jogos","n_assistencias"],registros)

result = colecao.insert_many(registros_assistencia)

print("assistentes inseridos:",result.inserted_ids)
