from utils.config_driver import ChromeWebDriver
from selenium.webdriver.common.by import By
from utils.waits import Waits
from traceback import format_exc

class CityPage:
    """Classe responsavel pela pagina de cidade.
    """
    
    def __init__(self, driver:ChromeWebDriver):
        if not isinstance(driver, ChromeWebDriver):
            raise Exception("O tipo do driver não é valido pois não é um Webdriver chrome!")
        
        self.driver:ChromeWebDriver = driver
        self.waits:Waits = Waits(self.driver)
        
    def get_city_data(self, city:str = "Arealva") -> dict[bool, str, dict, str]:
        """Metodo responsavel por extrair dados da cidade passa pelo parametro city

        Args:
            
            city (str, optional): Recebe o nome da cidade a ser pesquisada. Defaults to "Arealva".

        Returns:
            
            dict[bool, str, dict]: {"error" bool, "type": str, "data" dict, "exception": str}
        """
        
        try:
            
            data = []
            
            lines_li = self.waits.wait_visibility_all({"css_selector" : 'ul[class="day-list"] li'})
            
            for line in lines_li:
                day_month = line.find_element(By.CSS_SELECTOR, 'ul[class="day-list"] li span:nth-child(1)').text
                
                temperature = line.find_elements(By.CSS_SELECTOR, 'ul[class="day-list"] li span:nth-child(2)')[0].text
                
                description_sky = line.find_element(By.CSS_SELECTOR, 'ul[class="day-list"] li span[class="sub"]').text
                
                data.append(
                    f"{day_month} | {temperature} | {description_sky}"
                )
                
            data_city = {
                "name_city" : city,
                "data" : data
            }
            
            return {
                    "error" : False,
                    "type" : "",
                    "data" : data_city,
                    "exception" : ""
                    }
            
        except Exception:
            
            return {
                    "error" : True,
                    "type" : f"Erro inesperado ao extrair dados da cidade: {city}",
                    "data" : [],
                    "exception" : f"{format_exc()}"
                    }