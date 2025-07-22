from utils.config_driver import ChromeWebDriver
from utils.waits import Waits
from selenium.webdriver.common.keys import Keys
from traceback import format_exc
from time import sleep

class IndexPage:
    """Classe responsavel pela pagina index.
    """
    
    def __init__(self, driver:ChromeWebDriver):
        if not isinstance(driver, ChromeWebDriver):
            raise Exception("O tipo do driver não é valido pois não é um Webdriver chrome!")
        
        self.driver:ChromeWebDriver = driver
        self.waits:Waits = Waits(self.driver)
        
    def search_city(self, city:str = "Arealva") -> dict[bool, str, str, str]:
        """Metodo responsavel por pesquisar a cidade recebida no paramentro city

        Args:
            
            city (str, optional): Recebe o nome da cidade a ser pesquisada. Defaults to "Arealva".

        Returns:
            
            dict[bool, str, str, str]: {"error" bool, "type": str, "data" str, "exception": str}
        """
        
        try:
            try:
                self.driver.get("https://openweathermap.org/")
                
            except Exception: 
                return {
                        "error" : True,
                        "type" : "Erro ao carregar o site OpenWeatherMap tente novamente mais tarde!",
                        "data" : "",
                        "exception" : format_exc()
                        }
            
            input_search = self.waits.wait_clickable({"css_selector" : 'input[placeholder="Search city"]'}, time=5)
            input_search.send_keys(city)
            
            sleep(0.5)
            
            input_search.send_keys(Keys.ENTER)
            
            try:
                
                result_search = self.waits.wait_visibility({"css_selector" : 'ul[class="search-dropdown-menu"] li'}, time=5)
                result_search.click()
                    
            except Exception:
                return {
                        "error" : True,
                        "type" : f"A cidade: {city} não  foi encontrada!",
                        "data" : "",
                        "exception" : ""
                        }
            
            return {"error" : False, "type" : "", "data" : "", "exception" : ""}
        
        except Exception:
            return {
                    "error" : True,
                    "type" : "Erro inesperado ao pesquisar cidade, contate o ADM",
                    "data" : "",
                    "exception" : "" 
                    }