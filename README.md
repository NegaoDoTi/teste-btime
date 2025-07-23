# Teste BTIME

Este é um teste para vaga de RPA da Btime

# Requisitos

    Tenha instalado em sua maquina Python 3.10

# Instalação da bibliotecas:

    . Abra o terminal ou CMD dentro da pasta raiz

    . Execute os seguintes comandos:
        .1º:
            . python3 -m pip install pipenv
            . python3 -m pip pipenv shell (ira criar subterminal apenas para dependencias da projeto)

        .2º:
            .Ja dentro do sub terminal do pipenv execute o seguintes comandos:
                .   pipenv install

    . Você criar um conta no OpenWeatherMap e criar um chave de API
    . Apos criar sua chave de API você deve registrar ela no arquivo .env conforme o indicado   no arquivo

# Como executar webscraping:

    . Abra o terminal ou CMD dentro da pasta raiz

    . Se necessario execute novamente o comando caso não esteja dentro do sub terminal pipenv:
        . python3 -m pipenv shell

    . pipenv run python /webscraping/run.py

# Como executar o script de consumo da API:

    . Abra o terminal ou CMD dentro da pasta raiz

    . Se necessario execute novamente o comando caso não esteja dentro do sub terminal pipenv:
        . python3 -m pipenv shell

    . pipenv run python /api/run.py
