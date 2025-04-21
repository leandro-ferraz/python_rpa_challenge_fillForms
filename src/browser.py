from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement #import just for ilustrate a specific typehint (find method)

from config import Config

class Browser:
    def __init__(self):    
        def genererate_options():
            options = Options()

            prefs = {
                "download.prompt_for_download": False,
                "download.default_directory": Config.DOWNLOAD_DIR,
                "safebrowsing.enabled": True
            }
        
            options.add_experimental_option("prefs", prefs)


            """
            options.add_argument('--headless=new')  # Nova sintaxe do modo headless
            """
            options.add_argument('--no-sandbox') # Desativa o mecanismo de sandbox do Chrome, + performance e - segurança
            options.add_argument('--disable-dev-shm-usage') #Evita problemas de memória compartilhada em ambientes com recursos limitados
            options.add_argument('--disable-gpu')  # Necessário em alguns sistemas Windows
            
            return options

        path = ChromeDriverManager().install()
        print(path)
        self.driver = webdriver.Chrome(
                        service=Service(path),
                        options=genererate_options()
                     )

        self.driver.implicitly_wait(10)
        
    def go_to(self, url: str):
        self.driver.get(url)

    def find(self, by, value) -> WebElement:
        return self.driver.find_element(by, value)
        
    def find_all(self, by, value) -> list[WebElement]:
        return self.driver.find_elements(by, value)
    
    def quit(self):
        self.driver.quit()
    
    


        