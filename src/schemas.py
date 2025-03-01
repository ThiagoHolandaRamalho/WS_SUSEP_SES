import pandera as pa
from pandera import DataFrameSchema
from pandera.typing import Series,DataFrame,Int64
import pandas as pd


class SchemaSesCias(pa.DataFrameModel):
    """
    Esquema de validação para o arquivo Ses_cias.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.
    
    Attributes:
        Coenti Series[str] : pa.Field(nullable= True,description="Código da seguradora") 
        Noenti Series[str] : pa.Field(nullable= True, description= "Nome da seguradora")
    """

    Coenti : Series[str] = pa.Field(nullable= True,description="Código da seguradora") 
    Noenti : Series[str] = pa.Field(nullable= True, description= "Nome da seguradora")

    class Config:
        coerce = True

class SchemaSesRamos(pa.DataFrameModel):
    """
    Esquema de validação para o arquivo Ses_ramos.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.
    
    Attributes:
        coramo  Series[str] :pa.Field(nullable= True,description="Código do ramo")
        noramo  Series[str] :pa.Field(nullable= True, description= "Nome dramo")


    """
    coramo : Series[str] = pa.Field(nullable= True,description="Código do ramo")
    noramo : Series[str] = pa.Field(nullable= True, description= "Nome dramo")

    class Config:
        coerce = True

class SchemaSesGrupoRamo(pa.DataFrameModel):
    """
    Esquema de validação para o arquivo ses_gruposramos.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.
    
    Attributes:
        GRAID      Series[str] : pa.Field(nullable= True,description="Identificador")
        GRANOME	   Series[str] : pa.Field(nullable= True,description="Nome do Grupamento de ramos")
        GRACODIGO  Series[str] : pa.Field(nullable= True,description="Código do grupamento de ramos")


    """

    GRAID :Series[str]	 = pa.Field(nullable= True,description="Identificador")
    GRANOME	:Series[str] = pa.Field(nullable= True,description="Nome do Grupamento de ramos")
    GRACODIGO : Series[str] = pa.Field(nullable= True,description="Código do grupamento de ramos")

class SchemaSesSeguros(pa.DataFrameModel):
    """
    Esquema de validação para o arquivo Ses_seguros.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.
    
    Attributes:
        damesano                             Series[Int64]: Ano e mês da informação
        coenti                               Series[Int64]: Código da Empresa
        cogrupo                              Series[Int64]: Codigo do grupo
        coramo                               Series[Int64]: Código do Ramo no FIP
        premio_direto                        Series[float]: Prêmio Direto (R$)
        premio_de_seguros                    Series[float]: Prêmio Seguros (R$)
        premio_retido                        Series[float]: Prêmio Retido (R$)
        premio_ganho                         Series[float]: Prêmio Ganho (R$)
        sinistro_direto                      Series[float]: Sinistro de Seguros (R$)
        sinistro_retido                      Series[float]: Sinistro Retido (R$)
        desp_com                             Series[float]: Despesa Comercial (R$)
        premio_emitido2                      Series[float]:
        premio_emitido_cap                   Series[float]:
        despesa_resseguros                   Series[float]:
        sinistro_ocorrido                    Series[float]:
        receita_resseguro                    Series[float]:
        sinistros_ocorridos_cap              Series[float]:
        recuperacao_sinistros_ocorridos_cap  Series[float]:
        rvne                                 Series[float]:
        conveniodpvat                        Series[float]:
        consorciosefundos                    Series[float]:
    """



    damesano                             :Series[Int64] = pa.Field(nullable=True)
    coenti                               :Series[Int64] = pa.Field(nullable=True)
    cogrupo                              :Series[Int64] = pa.Field(nullable=True)
    coramo                               :Series[Int64] = pa.Field(nullable=True)
    premio_direto                        :Series[float] = pa.Field(nullable=True)
    premio_de_seguros                    :Series[float] = pa.Field(nullable=True)
    premio_retido                        :Series[float] = pa.Field(nullable=True)
    premio_ganho                         :Series[float] = pa.Field(nullable=True)
    sinistro_direto                      :Series[float] = pa.Field(nullable=True)
    sinistro_retido                      :Series[float] = pa.Field(nullable=True)
    desp_com                             :Series[float] = pa.Field(nullable=True)
    premio_emitido2                      :Series[float] = pa.Field(nullable=True)
    premio_emitido_cap                   :Series[float] = pa.Field(nullable=True)
    despesa_resseguros                   :Series[float] = pa.Field(nullable=True)
    sinistro_ocorrido                    :Series[float] = pa.Field(nullable=True)
    receita_resseguro                    :Series[float] = pa.Field(nullable=True)
    sinistros_ocorridos_cap              :Series[float] = pa.Field(nullable=True)
    recuperacao_sinistros_ocorridos_cap  :Series[float] = pa.Field(nullable=True)
    rvne                                 :Series[float] = pa.Field(nullable=True)
    conveniodpvat                        :Series[float] = pa.Field(nullable=True)
    consorciosefundos                    :Series[float] = pa.Field(nullable=True)

    class Config:
        coerce = True

class SesUf2(pa.DataFrameModel):
    """
    Esquema de validação para o arquivo SES_UF2.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.

    Attributes: 
        coenti       Series[Int64]: Código da Empresa
        damesano     Series[Int64]: Ano e mês da informação
        ramos        Series[Int64]: Codigo do Ramo
        UF           Series[str]: Unidade Federativa
        premio_dir   Series[float]: Premios Diretos
        premio_ret   Series[float]: Premios Retidos
        sin_dir      Series[float]: Sinistros Diretos
        prem_ret_liq Series[float]: Premios Retidos
        gracodigo    Series[Int64]: Código do grupamento de ramos
        salvados     Series[float]: Salvados de sinistros
        recuperacao  Series[float]: Recuperações 
    """
  
    coenti        :Series[Int64]  = pa.Field(nullable=True)
    damesano      :Series[Int64]  = pa.Field(nullable=True)
    ramos         :Series[Int64]  = pa.Field(nullable=True)
    UF            :Series[str]   = pa.Field(nullable=True,description='Unidade Federativa do Risco')
    premio_dir    :Series[float] = pa.Field(nullable=True)
    premio_ret    :Series[float] = pa.Field(nullable=True)
    sin_dir       :Series[float] = pa.Field(nullable=True)
    prem_ret_liq  :Series[float] = pa.Field(nullable=True)
    gracodigo     :Series[Int64] = pa.Field(nullable=True)
    salvados      :Series[float] = pa.Field(nullable=True)
    recuperacao   :Series[float] = pa.Field(nullable=True)