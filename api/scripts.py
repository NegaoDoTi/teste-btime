from requests import get
from config.config import API_KEY
from datetime import datetime

def get_lat_lon(city:str = "Arealva") -> dict[float, float]:
    """Metodo responsavel por buscar a latitude e longitude da cidade

    Args:
        
        city (str, optional): Recebe nome da cidade a ser pesquisada. Defaults to "Arealva".

    Raises:
        
        Exception: Caso status code seja diferente de 200 e 201
        Exception: Caso a cidade passada por parametro não seja encontrada

    Returns:
        
        dict[float, float]: {"lat" : float, "lon" : float}
    """
    
        
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&Limit=1&appid={API_KEY}"
    
    header = {
        "Content-Type" : "application/json"
    }
    
    
    response = get(url,headers=header, verify=False)
    
    if response.status_code != 200 and response.status_code != 201:
        raise Exception(f"Error ao consultar api de Geolocalização, status code: {response.status_code}")
        
    raw_data = response.json()
    
    if len(raw_data) == 0:
        raise Exception(f"Cidade: {city} não encontrada!")

    data = {
        "lat" : raw_data[0]["lat"],
        "lon" : raw_data[0]["lon"]
    }
    
    return data

def get_city_forecast_data(lat:float, lon:float, city:str = "Arealva") -> dict:
    """Metodo responsavel por buscar dados meteorologicos da cidade no momento atual

    Args:
        
        lat (float): latitude da cidade
        lon (float): longitude da cidade
        city (str, optional): Nome da cidade aonde dados sejam buscados na API. Defaults to "Arealva".

    Raises:
        
        Exception: Caso o status code da consulta seja diferente de 200 e 201

    Returns:
        
        dict: dicionario contendo todos os dados relevantes da custa
    """
    
    now_date = datetime.now().strftime("%d/%m/%Y : %H:%M:%S")
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=pt_br&units=metric&appid={API_KEY}"
    
    header = {
        "Content-Type" : "application/json"
    }
    
    response = get(url, headers=header, verify=False)
    
    if response.status_code != 200 and response.status_code != 201:
        raise Exception(f"Erro ao consultar API de previsão do tempo status code: {response.status_code}")
    
    raw_data = response.json()
    
    data = {
        "cidade" : city,
        "data_hora" : now_date,
        "latitude" : str(lat),
        "longitude": str(lon),
        "ceu" : raw_data["weather"][0]["description"],
        "temperatura" : f'{raw_data["main"]["temp"]}ºC',
        "temperatura_min" : f'{raw_data["main"]["temp_min"]}ºC',
        "temperatura_max" : f'{raw_data["main"]["temp_max"]}ºC',
        "humidade_ar" : f'{raw_data["main"]["humidity"]}%',
        "velocidade_vento" : f'{raw_data["wind"]["speed"]} Metros/Segundos'
    }
    
    return data