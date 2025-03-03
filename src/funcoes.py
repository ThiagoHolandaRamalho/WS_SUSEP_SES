import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import date
import sys
from datetime import datetime , timedelta, date
import time
from datetime import date
from dateutil.relativedelta import relativedelta
from pathlib import Path
from glob import glob 
import shutil
import zipfile
import pandas as pd
import schemas

from loguru import logger






def iniciar_logs(path:Path)-> None:
    """
    Objetivo da função: Inicia uma Seção do logger
    
    Args:
        path (Path): Caminho onde iremos criar os arquivos .log

    """

    logger.add(os.path.join(path,'LOGS_EXTRACAO_SUSEP.log'),level='INFO')
    logger.add(os.path.join(path,'LOGS_EXTRACAO_SUSEP_ERROS.log'),level='ERROR')



def criar_pasta(path:Path) -> None:
    """
    Objetivo da função: Apagar e recriar a pasta recebida no argumento Path
    
    Args:
        path (Path): Path onde a pasta será criada

    
    """

    try:
        shutil.rmtree(path,ignore_errors=True)
    except:
        ...

    os.makedirs(path,exist_ok=True)



def buscar_arquivo_na_susep(path:Path ,qde_max_segundos_download:int = 600) -> bool:
    """
    Objetivo da função: Acessa o site da Susep e realiza o download da base em formato `.zip`.

    Args:
        path (Path): Caminho onde o arquivo baixado será salvo.
        qde_max_segundos_download (int): Tempo máximo em segundos que o sistema aguardará 
                                        para concluir o download. Se o limite for atingido, 
                                        o processo será abortado.

    Returns:
        bool: Retorna `True` se o download for concluído com sucesso, caso contrário, 
            retorna `False`.
    """

    logger.info('Iniciando processo de Busca na Susep')
    check_download = False
    qde_max_segundos = qde_max_segundos_download
    criar_pasta(path)
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        options.add_argument("--headless")

        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico,options=options)
    except Exception as e:
         logger.error(f'Erro na inicialização do selenium : {e}')
         return check_download
         
    driver.get(r'https://www2.susep.gov.br/menuestatistica/ses/principal.aspx')

    time.sleep(5)

    id = driver.find_element(By.ID,'GEEST')
    if id: 
        try:
            tag_a = id.find_element(By.TAG_NAME,'a')
            link = tag_a.get_attribute('href')
        except Exception as e:
            logger.error(f'Obtendo link do download {e}')
    
        if link:
            driver.get(link)
            logger.info('Efetuando download do Zip')
        
        else: 
            logger.error('Link não encontrado')
            print('link não encontrado')
            driver.close()
            return

    else: 
        logger.error('Id do botão não localizado')
        print('Id do botão não localizado')
        driver.close()
        return
        
    time.sleep(5)
    segundos = 0
    
    while True:
        if segundos % 10 == 0:
                print('Efetuando Download')
        
        segundos += 1
        if segundos > qde_max_segundos: 
            logger.error('Excedeu o tempo limite de download')
            print('Excedeu o tempo limite de download')
            driver.close()
            return check_download
        
        arquivo = glob(os.path.join(path,'*.crdownload'))
        if arquivo:
            time.sleep(1)
            continue
        break
    
    print('Download Concluído')
    logger.info('Download Concluído')
    driver.close()
    check_download = True
    return check_download



def descompactar_zip(path_origem,check_sucesso:bool = False) -> bool:
    """
    Objetivo da função: Verifica a existência de arquivos `.zip` e realiza a descompactação.

    Args:
        path_origem (Path): Caminho onde os arquivos `.zip` serão procurados.
        check_sucesso (int): Retorno da função `buscar_arquivo_na_susep()`. Se a função 
                            for bem-sucedida, o valor será `True`, permitindo a 
                            descompactação.

    Returns:
        bool: Retorna `True` se a descompactação for concluída com sucesso, caso contrário, 
            retorna `False`.
    """

    
    try:
        if check_sucesso:
            arquivos_csv =  glob(os.path.join(path_origem,'*.csv'))
            for arq in arquivos_csv:
                os.remove(arq)

        time.sleep(5)
        if check_sucesso:
            arquivos = glob(os.path.join(path_origem,'*.zip'))

            for arquivo in arquivos:
                if arquivo.endswith('.zip'):
                    caminho_completo = os.path.join(path_origem, arquivo)

                    with zipfile.ZipFile(caminho_completo, 'r') as zip_ref:
                        zip_ref.extractall(path_origem)
        check_zip =True
        logger.info('Descompactação efetuada')
    except Exception as e:
        check_zip = False
        logger.error(f'Erro na Descompactação {e}')
    return check_zip




def validar_schemas_obrigatorios(path:Path,check_sucesso_zip:bool = False):
    """
    Objetivo da função: Realiza a validação da estrutura dos arquivos CSV.

    Args:
        path_origem (Path): Caminho onde os arquivos `.csv` serão procurados.
        check_sucesso_zip (int): Retorno da função `descompactar_zip()`. Se a função 
                                for bem-sucedida, o valor será `True`, permitindo 
                                a continuidade da validação.

    Returns:
        bool: Retorna `True` se a validação for concluída com sucesso, caso contrário, 
            retorna `False`.
    """


    check_validacao = True
    encoding_utilizado = 'ISO-8859-1'
    separador = ';'
    decimal = ','
    lazy = False

    if check_sucesso_zip:

        try:
            print('Ses_cias')
            schemas.SchemaSesCias.validate(pd.read_csv(os.path.join(path,"Ses_cias.csv"),encoding=encoding_utilizado,sep=separador),lazy=  lazy)
            print('Ses_ramos')
            schemas.SchemaSesRamos.validate(pd.read_csv(os.path.join(path,"Ses_ramos.csv"),encoding=encoding_utilizado,sep=separador),lazy=  lazy)
            print('ses_gruposramos')
            schemas.SchemaSesGrupoRamo(pd.read_csv(os.path.join(path,"ses_gruposramos.csv"),encoding=encoding_utilizado,sep=separador),lazy=  lazy)
            print('Ses_seguros')
            schemas.SchemaSesSeguros.validate(pd.read_csv(os.path.join(path,"Ses_seguros.csv"),encoding=encoding_utilizado,sep=separador,decimal=decimal),lazy=  lazy)
            print('SES_UF2')
            schemas.SesUf2.validate(pd.read_csv(os.path.join(path,"SES_UF2.csv"),encoding=encoding_utilizado,sep=separador,decimal=decimal),lazy=  lazy)
            print('Ses_campos')
            schemas.SchemaSesCampos.validate(pd.read_csv(os.path.join(path,"Ses_campos.csv"),encoding=encoding_utilizado,sep=separador),lazy=  lazy)
            print('SES_Balanco')
            schemas.SchemaSesBalanco.validate(pd.read_csv(os.path.join(path,"SES_Balanco.csv"),encoding=encoding_utilizado,sep=separador,decimal=decimal),lazy=  lazy)
            print('Ses_Dados_Cap')
            schemas.SchemaSesDadosCap.validate(pd.read_csv(os.path.join(path,"Ses_Dados_Cap.csv"),encoding=encoding_utilizado,sep=separador,decimal=decimal),lazy=  lazy)
            print('ses_cap_uf')
            schemas.SchemaSesCapUf.validate(pd.read_csv(os.path.join(path,"ses_cap_uf.csv"),encoding=encoding_utilizado,sep=separador,decimal=decimal),lazy=  lazy)
            print('SES_ValoresMovRamos')
            schemas.SchemaSesValoresMovRamos.validate(pd.read_csv(os.path.join(path,"SES_ValoresMovRamos.csv"),encoding=encoding_utilizado,sep=separador,decimal=decimal),lazy=  lazy)
            print('ses_valoresresmovgrupos')
            schemas.SchemaSesValoresResMovMovGrupos.validate(pd.read_csv(os.path.join(path,"ses_valoresresmovgrupos.csv"),encoding = encoding_utilizado, sep = separador , decimal=decimal ) ,lazy =  lazy)

            print('Sucesso na validação')
            logger.info(f'Schemas validados com sucesso')
            return check_validacao
        except Exception as e:
            check_validacao = False
            logger.error(f'Erro na validação dos Schemas {e}')
            return  check_validacao
        

def mover_arquivos(path_origem,path_destino,check_validacao):
    if check_validacao:
        try:
            criar_pasta(path_destino)
            arquivos =  glob(os.path.join(path_origem,'*.csv'))
            for arq in arquivos:
                shutil.copy(arq,path_destino)
            logger.info('Arquivos copiados com sucesso')
            print('processo finalizado')
        except Exception as e :
            logger.error(f'Erro ao copiar os arquivos {e}')
    else:
        print('Não movemos os arquivos pois obtivemos erro na etapa de validação')
        logger.info('Não movemos os arquivos pois obtivemos erro na etapa de validação')