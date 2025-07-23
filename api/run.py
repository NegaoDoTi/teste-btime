from scripts import get_city_forecast_data, get_lat_lon
from generate_csv import generate_csv
from traceback import format_exc
import logging

logging.basicConfig(filename="script_api.log", level=logging.INFO, format='%(asctime)s | [%(levelname)s]: %(message)s')

def run(city:str = "Arealva") -> None:
    """Metodos responsavel por executar na ordem correta os 
        scripts para realizar a busca na api e gerar o arquivo csv

    Args:
        
        city (str, optional): Nome da cidade aonde quer se buscar os dados. Defaults to "Arealva".
    """
    
    try:
        lat_lon = get_lat_lon()
    
        data = get_city_forecast_data(lat_lon["lat"], lat_lon["lon"])
    
        csv_file = generate_csv(data)
    
        print(f"Script de previsão do tempo finalizado com sucesso local do arquivo csv: {csv_file}")

        return

    except Exception:
        logging.critical(format_exc())
        
        return

if __name__ == "__main__":
    run()