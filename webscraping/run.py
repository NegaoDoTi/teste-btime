import logging
from robot.start import StartRobot

logging.basicConfig(filename="webscraping.log", level=logging.INFO, format='%(asctime)s | [%(levelname)s]: %(message)s')

def run():
    """Metodos responsavel por iniciar o webscraping, aqui seria possivel criar uma logica
        para iniciar multiplas instancias para extrair dados de diversas cidades diferentes
    """
    
    robot = StartRobot()
    
    robot.start()
    
if __name__ == "__main__":
    run()