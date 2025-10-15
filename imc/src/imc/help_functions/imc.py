from math import pow
from colorama import Fore, Back, Style

def calcula_imc(peso: float, altura:float)->float:
    return peso / pow(altura, 2)

def classifica_imc(imc:float)->str:
    response = ""

    if imc <= 18.5:
        response = Fore.LIGHTMAGENTA_EX + "Abaixo do peso"
    elif imc <= 24.9:
        response = Fore.GREEN + "Peso normal"
    elif imc <= 35:
        response = Fore.LIGHTRED_EX + "Acima do peso"
    else:
        response = Fore.RED + "Obesidade"

    return response+Style.RESET_ALL