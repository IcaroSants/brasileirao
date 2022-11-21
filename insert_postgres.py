from src.extract import Extract
from src.connectPostgres import Connect


connect = Connect(host='????',database='????', user="????", password="????")
extract = Extract("https://www.espn.com.br/futebol/estatisticas/_/liga/BRA.1/vista/gols")

tbodies = extract.get_table("tbody",{"class":"Table__TBODY"})
    
registros = extract.get_register(tbodies[0])
registros_gols = extract.organize_information(["nome","clube","n_jogos","n_gols"],registros)

connect.faz_insercao("artilheiros",registros_gols)
print(connect.get_registers("artilheiros"))

registros = extract.get_register(tbodies[1])
registros_assistencia = extract.organize_information(["nome","clube","n_jogos","n_assistencias"],registros)

connect.faz_insercao("assistencia",registros_assistencia)

print(connect.get_registers("assistencia"))
   

    
    


