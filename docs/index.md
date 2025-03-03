# Documentação do projeto
## Fonte de dados : Susep(Ses)  


Sistema de extração e validação dos arquivos fornecidos pela Susep.

- Efuetua webscraping na página da susep com o objetivo de efetuar o download da base estatística mensal
- Valida o Schema dos arquivos que serão utilizados no DataViz
- Gravação de logs com a biblioteca Loguru  


## Ferramentas utilizadas

![image](home/assets/poetry.png)
![image](home/assets/pandas.png)
![image](home/assets/selenium.png)
![image](home/assets/python.png)
![image](home/assets/pandera.png)
![image](home/assets/powerbi.png)
![image](home/assets/susep_black.png)


## Comandos / Instruções 

Efetua a instalação das bibliotecas necessárias  
<pre><code>poetry install --no-root </code></pre>


`PATH_BASE no arquivo src.main.py` - Informa onde os arquivos serão salvos

## Fluxo de trabalho da automação

```mermaid

flowchart TD
    A[Iniciar Selenium] --> B[Encontrar link para download];
    B --> C{Link existe?};
    C -- Não --> Z[Fim];
    C -- Sim --> D[Efetuar download];
    D --> E{Download concluído com sucesso?};
    E -- Não --> Z;
    E -- Sim --> F[Descompactar o arquivo];
    F --> G[Validar os Schemas dos arquivos CSV];
    G --> H{Schemas dentro do contrato de dados?};
    H -- Não --> Z;
    H -- Sim --> I[Mover Arquivos para pasta Arquivos CSV]
    I --> Z[Fim]
    

```
