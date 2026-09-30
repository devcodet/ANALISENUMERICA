from globals import VALOR_PARA_DIGITO, DIGITO_PARA_VALOR, PRECISAO, EPS
from Utils import separateNumber
import decimal

def DecimalParaBase(number: str, base_atual: int) -> str:
    """
    Converte a parte inteira de um número decimal (base 10) para uma base especificada.
    
    Args:
        number (str): O número decimal a ser convertido.
        base_atual (int): A base para a qual o número será convertido.
        
    Returns:
        str: O número convertido na base especificada.
    """

