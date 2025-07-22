from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from traceback import format_exc


class Driver():
    """ Classe responsavel por gerenciar drivers selenium qual o robô irá utilizar!
    """
    
    def __init__(self):
        self.__driver:ChromeWebDriver
        
    def get_chrome_driver(self) -> ChromeWebDriver | dict[bool, str]:
        """Metodo que inicia um novo Chrome driver

        Returns:
            ChromeWebDriver | dict: {'error' : bool, 'type': str, 'exception' : str}
        """
        
        try:
            self.__service = ChromeService(executable_path=ChromeDriverManager().install())
            
            self.__options = ChromeOptions()
            
            self.__driver = ChromeWebDriver(service=self.__service, options=self.__options)
            
            self.__driver.maximize_window()
            
            return self.__driver
            
        except Exception:
            return {"error" : True, "type" : "Erro inesperado ao iniciar o nevegador Chrome",  "exception" : f"{format_exc()}"}