# Teste BTIME

Este é um teste para vaga de RPA da Btime

# Descrição

    1. *Descrição do Problema:*
    - Criar dois scripts em Python que automatizem a coleta de dados de um website de sua escolha
    (exemplo: cotação de ações, notícias, clima). O primeiro script deve utilizar técnicas de web scraping, e o
    segundo deve realizar a coleta de dados por meio de uma API pública relacionada ao mesmo tema.
    Em ambos os casos, os dados extraídos devem ser formatados e salvos em um arquivo CSV.

    2. *Requisitos Técnicos:*
    - *Script 1: Web Scraping*:
    - Utilizar Python e bibliotecas como Selenium, BeautifulSoup, ou Scrapy para realizar o web scraping.
    - O script deve ser capaz de lidar com bloqueios e outras restrições comuns do web scraping.
    - *Script 2: API*:
    - Utilizar Python para acessar uma API pública que forneça dados semelhantes aos obtidos no web scraping.
    - Implementar a requisição à API e formatar os dados recebidos de maneira semelhante ao script de web scraping.
    - O arquivo CSV final, gerado por ambos os scripts, deve estar bem estruturado e claro.

    3. *Critérios de Avaliação:*
    - *Qualidade do código:* legibilidade, uso de boas práticas, e comentários explicativos em ambos os scripts.
    - *Eficiência da solução:* quão bem os scripts resolvem o problema proposto.
    - *Robustez dos scripts:* tratamento de erros, exceções, e contingências para possíveis falhas tanto no
    scraping quanto na API.
    - *Documentação:* instruções claras sobre como executar ambos os scripts, com detalhes das dependências
    necessárias.

    4. *Entrega:*
    - Via Github, o candidato deverá fornecer os códigos-fonte dos dois scripts (web scraping e API), juntamente
    com os arquivos CSV gerados e qualquer documentação auxiliar.
    - Incluir um README com instruções para instalar as dependências e executar cada um dos scripts.

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
    . Apos criar sua chave de API você deve registrar ela no arquivo .env conforme o indicado no arquivo

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
