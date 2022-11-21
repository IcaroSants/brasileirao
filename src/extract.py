from bs4 import BeautifulSoup
from urllib.request import urlopen

class Extract(object):
    def __init__(self,url):
        self.url = url

    
    def get_page(self):
        html = urlopen(self.url)
        bs = BeautifulSoup(html, "html.parser")
        return bs
    
    def get_table(self,tags,filter):
        return self.get_page().find_all(tags,filter)
    
    def get_register(self,tags):
        registros = []
        for tag in tags.children:
            dados = []
            for content in tag.contents:
                dados.append(content.text)
            dados.pop(0)
            registros.append(dados)
        return registros

    
    def organize_information(self, header, register):
        dados = []
        for registro in register:
            info = {}
            for index, cab in zip(range(len(registro)),header):
                if registro[index].isdigit():
                    info[cab] = int(registro[index])
                else:
                    info[cab] = registro[index]
            dados.append(info)
        return dados
    
    
