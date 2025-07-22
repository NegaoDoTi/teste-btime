from robot.pages.index import IndexPage
from robot.pages.city import CityPage
from traceback import format_exc
from utils.config_driver import Driver, ChromeWebDriver
from utils.generate_csv import generate_csv
import logging

class StartRobot:
    """Classe responsavel por organizar todos modulos do scraping
    """
    
    def __init__(self):
        self.driver:ChromeWebDriver
        self.index_page:IndexPage
        self.city_page:CityPage
        
    def start(self, city:str = "Arealva") -> None:
        """Metodo responsavel por colocar em ordem todas as etapas do webscraping
        """
        
        try:
            self.driver = Driver().get_chrome_driver()
            if isinstance(self.driver, dict):
                logging.critical(f"{self.driver['type']}, {self.driver['exception']}")                
                return
            
            self.index_page = IndexPage(self.driver)
            self.city_page = CityPage(self.driver)
            
            search_city = self.index_page.search_city()
            if search_city["error"]:
                logging.error(f"{search_city['type']}, {search_city['exception']}")
                return

            extract_data = self.city_page.get_city_data()
            if extract_data["error"]:
                logging.error(f'{extract_data["type"]}, {extract_data["exception"]}')
                return
            
            data = extract_data["data"]
            
            csv_file = generate_csv(data)
            
            print(f"Webscraping Finalizado com sucesso! Local do arquivo csv: {csv_file}")
                
            return
        
        except Exception:
            logging.critical(f"Erro inesperado na execução do webscraping: {format_exc()}")
            return