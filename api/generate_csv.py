from pathlib import Path

def generate_csv(datas:dict[str]) -> str:
    """Metodo responsavel por gerar o arquivo CSV contendo dados da 
        previsão do tempo da cidade no momento atual da execução do script

    Args:
        
        datas (dict[str ...]): 
        
        {
            "cidade" : str
            "data_hora" : str
            "latitude" : str
            "longitude": str
            "ceu" : str
            "temperatura" : str
            "temperatura_min" : str
            "temperatura_max" : str
            "humidade_ar" : str
            "velocidade_vento" : str
        }

    Returns:
        
        str: Retorna o caminho completo do arquivo csv gerado
        
    """
    
    default_dir = Path(Path(__file__).parent)
    
    archive_full_path = Path(default_dir, f"previsao_{datas['cidade']}.csv")
    
    with open(str(archive_full_path), "w+") as csv_file:

        line = ""
        header = ""
        
        for key in datas:
            header = header + f"{key};" 
            line = line + f'{datas[key]};'
        
        header = header + "\n"
        line = line + "\n"
        
        csv_file.write(header)
        csv_file.write(line)
        
        return str(archive_full_path)
        
        
    
    