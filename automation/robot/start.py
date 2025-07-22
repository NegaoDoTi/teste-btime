from robot.pages.index import IndexPage
from traceback import format_exc
from utils.config_driver import Driver, ChromeWebDriver
import logging


class StartRobot:
    
    def __init__(self):
        self.driver:ChromeWebDriver
        self.index_page:IndexPage
        self.city_page:CityPage
        
    def start(self) -> None:
        try:
            self.driver = Driver().get_chrome_driver()
            if isinstance(self.driver, dict):
                logging.critical(self.driver["type"], self.driver["exception"])                
                return
            
        except Exception:
            return