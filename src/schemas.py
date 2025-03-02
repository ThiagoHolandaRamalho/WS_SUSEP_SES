import pandera as pa
import pandas as pd 
from pandera import DataFrameSchema
from pandera.typing import Series,DataFrame
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
        GRAID      Series[pd.Int64Dtype] : pa.Field(nullable= True,description="Identificador")
        GRANOME	   Series[str] : pa.Field(nullable= True,description="Nome do Grupamento de ramos")
        GRACODIGO  Series[pd.Int64Dtype] : pa.Field(nullable= True,description="Código do grupamento de ramos")


    """

    GRAID :Series[pd.Int64Dtype]	 = pa.Field(nullable= True,description="Identificador")
    GRANOME	:Series[str] = pa.Field(nullable= True,description="Nome do Grupamento de ramos")
    GRACODIGO : Series[pd.Int64Dtype] = pa.Field(nullable= True,description="Código do grupamento de ramos")

    class Config:
        coerce = True

class SchemaSesSeguros(pa.DataFrameModel):
    """
    Esquema de validação para o arquivo Ses_seguros.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.
    
    Attributes:
        damesano                             Series[pd.Int64Dtype]: Ano e mês da informação
        coenti                               Series[pd.Int64Dtype]: Código da Empresa
        cogrupo                              Series[pd.Int64Dtype]: Codigo do grupo
        coramo                               Series[pd.Int64Dtype]: Código do Ramo no FIP
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



    damesano                             :Series[pd.Int64Dtype] = pa.Field(nullable=True)
    coenti                               :Series[pd.Int64Dtype] = pa.Field(nullable=True)
    cogrupo                              :Series[pd.Int64Dtype] = pa.Field(nullable=True)
    coramo                               :Series[pd.Int64Dtype] = pa.Field(nullable=True)
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
        coenti       Series[pd.Int64Dtype]: Código da Empresa
        damesano     Series[pd.Int64Dtype]: Ano e mês da informação
        ramos        Series[pd.Int64Dtype]: Codigo do Ramo
        UF           Series[str]: Unidade Federativa
        premio_dir   Series[float]: Premios Diretos
        premio_ret   Series[float]: Premios Retidos
        sin_dir      Series[float]: Sinistros Diretos
        prem_ret_liq Series[float]: Premios Retidos
        gracodigo    Series[pd.Int64Dtype]: Código do grupamento de ramos
        salvados     Series[float]: Salvados de sinistros
        recuperacao  Series[float]: Recuperações 
    """
  
    coenti        :Series[pd.Int64Dtype]  = pa.Field(nullable=True)
    damesano      :Series[pd.Int64Dtype]  = pa.Field(nullable=True)
    ramos         :Series[pd.Int64Dtype]  = pa.Field(nullable=True)
    UF            :Series[str]   = pa.Field(nullable=True,description='Unidade Federativa do Risco')
    premio_dir    :Series[float] = pa.Field(nullable=True)
    premio_ret    :Series[float] = pa.Field(nullable=True)
    sin_dir       :Series[float] = pa.Field(nullable=True)
    prem_ret_liq  :Series[float] = pa.Field(nullable=True)
    gracodigo     :Series[pd.Int64Dtype] = pa.Field(nullable=True)
    salvados      :Series[float] = pa.Field(nullable=True)
    recuperacao   :Series[float] = pa.Field(nullable=True)

    class Config:
        coerce = True



class SchemaSesCampos(pa.DataFrameModel):
    ''' 
     Esquema de validação para o arquivo Ses_campos.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.

    Attributes:
        nuitem       Series[int]   : pa.Field(nullable=True,description ='Número do Campo')
        noitem       Series[str]   : pa.Field(nullable=True,description = 'Nome do Campo')
        nuquad       Series[str]   : pa.Field(nullable=True,description ='Quadro correspondente do FIP (22A, 22P,  23...)' )
        mercado      Series[str]   : pa.Field(nullable=True,description = 'Identificador do Mercado Supervisionado (C, P ou S) ')
        inivigencia  Series[pd.Int64Dtype] : pa. Field(nullable=True,description = 'Início de vigência do campo')
        fimvigencia  Series[pd.Int64Dtype] : pa.Field(nullable=True,description = 'Fim de vigência do campo')
    
    
    
    '''

    nuitem      : Series[int]   = pa.Field(nullable=True,description ='Número do Campo')
    noitem      : Series[str]   = pa.Field(nullable=True,description = 'Nome do Campo')
    nuquad      : Series[str]   = pa.Field(nullable=True,description ='Quadro correspondente do FIP (22A, 22P,  23...)' )
    mercado     : Series[str]   = pa.Field(nullable=True,description = 'Identificador do Mercado Supervisionado (C, P ou S) ')
    inivigencia : Series[pd.Int64Dtype] = pa. Field(nullable=True,description = 'Início de vigência do campo')
    fimvigencia : Series[pd.Int64Dtype] = pa.Field(nullable=True,description = 'Fim de vigência do campo')

    class Config:
        coerce = True


class SchemaSesBalanco(pa.DataFrameModel):
    ''' 
    Esquema de validação para o arquivo SES_Balanco.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.

    Attributes:
        coenti	 Series[pd.Int64Dtype]  : pa.Field(nullable=True,description='Código da Empresa')
        damesano Series[pd.Int64Dtype]  : pa.Field(nullable=True,description='Ano e mês da informação')	
        cmpid	 Series[pd.Int64Dtype]  : pa.Field(nullable=True,description='Codigo do campo ')
        valor	 Series[float]  : pa.Field(nullable=True,description='Valor')
        seq      Series[pd.Int64Dtype]  : pa.Field(nullable=True,description='Ordem do campo no Balanco')
        quadro   Series[str]    : pa.Field(nullable=True,description='Quadro a qual pertence o campo')
     
    '''
    coenti	 :Series[pd.Int64Dtype]  = pa.Field(nullable=True,description='Código da Empresa')
    damesano :Series[pd.Int64Dtype]  = pa.Field(nullable=True,description='Ano e mês da informação')	
    cmpid	 :Series[pd.Int64Dtype]  = pa.Field(nullable=True,description='Codigo do campo ')
    valor	 :Series[float]  = pa.Field(nullable=True,description='Valor')
    seq      :Series[pd.Int64Dtype]  = pa.Field(nullable=True,description='Ordem do campo no Balanco')
    quadro   :Series[str]    = pa.Field(nullable=True,description='Quadro a qual pertence o campo')

    class Config:
        coerce = True

class SchemaSesDadosCap(pa.DataFrameModel):
    ''' 
    Esquema de validação para o arquivo SES_Balanco.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.

    Attributes:
        coenti	        Series[pd.Int64Dtype] : pa.Field(nullable=True,description='Ano e mês da informação')
        damesano	    Series[pd.Int64Dtype] : pa.Field(nullable=True,description='Código da Empresa')
        codModal	    Series[pd.Int64Dtype] : pa.Field(nullable=True,description='Código da modalidade')
        modalidade	    Series[str]   : pa.Field(nullable=True,description='Descrição da modalidade (Tradicional, Compra-Programada, Popular, Incentivo, Antes Circ 365 e Não Adequado, Filantropia Premiável, Instrumento de Garantia)')
        receitasCap	    Series[float] : pa.Field(nullable=True,description='Total de receitas')
        valorResg	    Series[float] : pa.Field(nullable=True,description='Total de resgates')
        sorteiosPagos   Series[float] : pa.Field(nullable=True,description='Total de sorteios pagos')
    '''
    coenti              : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='Ano e mês da informação')
    damesano            : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='Código da Empresa')
    codModal            : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='Código da modalidade')
    modalidade          : Series[str]   = pa.Field(nullable=True,description='Descrição da modalidade (Tradicional, Compra-Programada, Popular, Incentivo, Antes Circ 365 e Não Adequado, Filantropia Premiável, Instrumento de Garantia)')
    receitasCap	        : Series[float] = pa.Field(nullable=True,description='Total de receitas')
    valorResg           : Series[float] = pa.Field(nullable=True,description='Total de resgates')
    sorteiosPagos       : Series[float] = pa.Field(nullable=True,description='Total de sorteios pagos')


    class Config:
        coerce = True


class SchemaSesCapUf(pa.DataFrameModel):
    '''
    Esquema de validação para o arquivo ses_cap_uf.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.

    Attributes:
        COENTI       Series[pd.Int64Dtype] : pa.Field(nullable=True,description='Código da Empresa')
        DAMESANO     Series[pd.Int64Dtype] : pa.Field(nullable=True,description='Ano e mês da informação')
        UF           Series[str]   : pa.Field(nullable=True,description='Unidade Federativa')
        PREMIO       Series[float] : pa.Field(nullable=True,description='Prêmios (R$)')
        RESGPAGO     Series[float] : pa.Field(nullable=True,description='Resgates Pagos (R$)')
        SORTPAGO     Series[float] : pa.Field(nullable=True,description='Sorteios Pagos (R$)')
        NUMPARTIC    Series[float] : pa.Field(nullable=True,description='Média de Participantes no Período')
        RESGATANTES  Series[float] : pa.Field(nullable=True,description='Resgatantes')
        SORTEIOS     Series[float] : pa.Field(nullable=True,description='Sorteios')
    
    '''
    COENTI         : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='Código da Empresa')
    DAMESANO       : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='Ano e mês da informação')
    UF             : Series[str] = pa.Field(nullable=True,description='Unidade Federativa')
    PREMIO         : Series[float] = pa.Field(nullable=True,description='Prêmios (R$)')
    RESGPAGO       : Series[float] = pa.Field(nullable=True,description='Resgates Pagos (R$)')
    SORTPAGO       : Series[float] = pa.Field(nullable=True,description='Sorteios Pagos (R$)')
    NUMPARTIC      : Series[float] = pa.Field(nullable=True,description='Média de Participantes no Período')
    RESGATANTES    : Series[float] = pa.Field(nullable=True,description='Resgatantes')
    SORTEIOS       : Series[float] = pa.Field(nullable=True,description='Sorteios')

    class Config:
        coerce = True


class SchemaSesValoresMovRamos(pa.DataFrameModel):
    '''
    Esquema de validação para o arquivo SES_ValoresMovRamos.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.

    Attributes:
        coenti       Series[pd.Int64Dtype] :
        damesano     Series[pd.Int64Dtype] :
        cmpid        Series[pd.Int64Dtype] :
        ramcodigo    Series[pd.Int64Dtype] :
        gracodigo    Series[pd.Int64Dtype] :
        valor        Series[float] :
        seq          Series[pd.Int64Dtype] :
        quadro       Series[pd.Int64Dtype] :



    '''


    coenti      : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='')
    damesano    : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='')
    cmpid       : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='')
    ramcodigo   : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='')
    gracodigo   : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='')
    valor       : Series[float] = pa.Field(nullable=True,description='')
    seq         : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='')
    quadro      : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='')


    class Config:
        coerce = True


class SchemaSesValoresResMovMovGrupos(pa.DataFrameModel):
    '''
    Esquema de validação para o arquivo ses_valoresresmovgrupos.csv

    Esta classe valida os dados do arquivo, garantindo a consistência 
    dos tipos e a conformidade com as regras definidas.

    **Resseguros**: Prêmios Ganhos  e Sinistros Retidos (Utilizar em conjunto com a tabela  ses_campos associando o CMPID - SES_VALORESRESMOVGRUPOS   com o NUITEM - SES_campos)

    Attributes:
        COENTI     Series[pd.Int64Dtype] :Código da Empresa
        DAMESANO   Series[pd.Int64Dtype] :Ano e mês da informação'
        CMPID      Series[pd.Int64Dtype] :codigo do campo na tabela ses_campos
        GRACODIGO  Series[pd.Int64Dtype] :Código do grupamento de ramos
        VALOR      Series[float] :Valor
        ID         Series[pd.Int64Dtype] :Identificador


    '''
    COENTI      : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='Código da Empresa')
    DAMESANO    : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='Ano e mês da informação')
    CMPID       : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='codigo do campo na tabela ses_campos')
    GRACODIGO   : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='Código do grupamento de ramos')
    VALOR       : Series[float] = pa.Field(nullable=True,description='Valor ')
    ID          : Series[pd.Int64Dtype] = pa.Field(nullable=True,description='Identificador')

    class Config:
        coerce = True 