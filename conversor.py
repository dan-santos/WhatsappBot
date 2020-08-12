class Conversor:
    def __init__(self, txt_file):
        # É iniciado com o nome do arquivo que ele vai converter

        self.txt_file = txt_file

    def converter(self):
        # Acessa o arquivo passado no construtor do objeto e retorna uma lista com as linhas do documento

        f = open(self.txt_file, 'r', encoding='utf-8', errors='ignore')
        lista = f.readlines()
        f.close()
        return self.limpar_lista(lista)

    def limpar_lista(self, lista):
        # Aqui ele faz a limpeza de linhas que não queremos enviar para o contato

        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        lista_limpa = list()
        lista_limpa.append(lista[2][:-1])
        for linha in lista[3:]:
            if linha != '\n' and linha[0] not in numeros:
                lista_limpa.append(linha[:-1])
        return lista_limpa
