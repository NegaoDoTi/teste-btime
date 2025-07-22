from pathlib import Path

def generate_csv(datas:dict[str, list]) -> str:
    """Metodo responsavel por gerar o arquivo CSV contendo dados da previsão do tempo da cidade

    Args:
        
        datas (dict[str, list]): {"name_city" : str, "data" : list[str]}
        
    Returns:
        
        str: Retorna o diretorio completo do arquivo CSV gerado.
        
    """
    
    default_dir = Path(Path(__file__).parent.parent)
    
    archive_full_path = Path(default_dir, f"previsao_{datas['name_city']}.csv")
    
    with open(str(archive_full_path), "w+") as csv_file:
        header = "Cidade; Dia 1; Dia 2; Dia 3; Dia 4; Dia 5; Dia 6; Dia 7; Dia 8\n"
        
        csv_file.write(header)
        
        line = f"{datas['name_city']} ;"

        for data in datas["data"]:
            
            line = line + f" {data} ;"
        
        line = line + "\n"
        
        csv_file.write(line)
        
        csv_file.close()
    
    return str(archive_full_path)
        