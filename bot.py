import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Bot:
    # Pega caminho atual do projeto
    path = os.getcwd()

    def __init__(self):
        # inicia o driver com todas as opções necessárias
        self.chrome = self.path + '/chromedriver'
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('start-maximized')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('lang=pt-br')

        self.driver = webdriver.Chrome(executable_path=self.chrome, chrome_options=chrome_options)

    def inicia(self, contato):
        # Abre o whatsapp e espera 20 segundos até começar a procurar os elementos do DOM
        # Após isso, ele busca na barra de pesquisa o nome do contato e clica na conversa

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)

        self.caixa_pesquisa = self.driver.find_element_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")
        self.caixa_pesquisa.send_keys(contato)
        time.sleep(2)

        self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(contato))
        self.contato.click()
        time.sleep(2)

    def envia_mensagem(self, texto):
        # Envia a mensagem para o contato aberto
        
        self.caixa_mensagem = self.driver.find_element_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text'][@data-tab='1']")
        self.caixa_mensagem.send_keys(texto)
        time.sleep(0.5)

        self.botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
        self.botao_enviar.click()
        time.sleep(0.5)