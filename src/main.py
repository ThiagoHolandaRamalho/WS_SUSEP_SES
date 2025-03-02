import os
from funcoes import *


PATH_BASE = r"C:\Users\thiag\Documents\BASE_SUSEP_TESTE_22"
PATH_PASTA_ARQUIVOS = os.path.join(PATH_BASE,"Download_arquivo")
PATH_PASTA_ARQUIVOS_CSV = os.path.join(PATH_BASE,"Arquivos_CSV")
QDE_MAX_SEGUNDOS_DOWNLOAD = 600 

iniciar_logs(PATH_BASE)

check_download = buscar_arquivo_na_susep(path=PATH_PASTA_ARQUIVOS,
                        qde_max_segundos_download=QDE_MAX_SEGUNDOS_DOWNLOAD)

check_zip = descompactar_zip(path_origem=PATH_PASTA_ARQUIVOS,check_sucesso=check_download)

check_validacao = validar_schemas_obrigatorios(PATH_PASTA_ARQUIVOS,check_zip)

mover_arquivos(PATH_PASTA_ARQUIVOS,PATH_PASTA_ARQUIVOS_CSV,check_validacao)