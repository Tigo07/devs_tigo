# import da classe principal
from ibgeparser.microdados import Microdados
# import dos enums para facilitar as buscas
from ibgeparser.enums import Anos, Estados, Modalidades

if __name__ == "__main__":
    # usando os unums
    ano = Anos.DEZ  

    estados = [ Estados.RIO_DE_JANEIRO]
    modalidades = [Modalidades.DOMICILIOS]
    
    # instanciando a classe
    ibgeparser = Microdados()
    # obeter dados
    ibgeparser.obter_dados_ibge(ano, estados, modalidades)