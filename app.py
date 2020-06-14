from selenium import webdriver
from selenium.webdriver.common.by import by 
from selemium.webdriver.ui import WebDriverWait 
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located


class Email:
    def __init__(self,driver):
        self.driver = driver
        self.NOME = (By,ID.'')
        self.MAIL = (By,ID.'')
        self.MSG = (By,ID.'')
        self.DEST = (By.CSS_SELECTOR, '')
        self.BTN = (By.CSS_SELECTOR, '')
        

    def find(self, *locator , time=30)
        return WebDriverWait(driver,timeout).until(visibility_of_all_elements_located(*locator))

    def login (self, user, password):
        self.find(self.NOME).send_keys(user)
        self.find(self.MAIL).send_keys(password)
        self.find(self.BTN).click
    
    def destinatario(self,destino):
        self.find(DEST).send_keys(destino)


    def msg (self, mensagem ):
        self.find(self.MSG).send_keys(mensagem)

    def sair (self):
        self.driver.quit() 
    
    
    def acessar(self,site):
        self.driver.get()


driver = webdriver.Chrome()
test = Email(driver)
test.acessar()
test.login()
test.destinatario()
test.msg()
test.sair()