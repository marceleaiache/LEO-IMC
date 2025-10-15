#Crie uma aplicação que calcula o imc do usuário. Vc precisa perguntar o nome, a altura e o peso.
#Classifique o imc nestas categorias <18.5(abaixo do peso), <24.9(Peso normal), <35(Acima do peso), < (Obesidade)

#def func(arg1, arg2):
#    return arg1 + arg2
import math
import math as matematica
from math import pow
from colorama import Fore, Back, Style


def imc(peso: float, altura:float)->float:
    return peso / pow(altura, 2)

def imc_type(imc:float)->str:
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


nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc_person = imc(peso, altura)
imc_type_person = imc_type(imc_person)


print("Agora vamos calcular o imc da sua mãe")
nome_mother = input("Digite nome da sua mãe: ")
altura = float(input("Digite a altura da sua mãe: "))
peso = float(input("Digite o peso da sua mãe: "))
imc_mother = imc(peso, altura)
imc_type_mother = imc_type(imc_mother)
#print(f"Seu imc é de: {imc:.2fLeo}")

print("{} seu imc é de: {:.2f}".format(nome, imc_person))
print("Categoria do imc: {}".format(imc_type_person))
print("{} o imc da sua mãe é de: {:.2f}".format(nome_mother, imc_mother))
print("Categoria do imc: {}".format(imc_type_mother))
