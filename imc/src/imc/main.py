#Crie uma aplicação que calcula o imc do usuário. Vc precisa perguntar o nome, a altura e o peso.
#Classifique o imc nestas categorias <18.5(abaixo do peso), <24.9(Peso normal), <35(Acima do peso), < (Obesidade)

#def func(arg1, arg2):
#    return arg1 + arg2
from math import pow
from help_functions import imc

nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc_person = imc.calcula_imc(peso, altura)
imc_type_person = imc.classifica_imc(imc_person)

print("Agora vamos calcular o imc da sua mãe")
nome_mother = input("Digite nome da sua mãe: ")
altura = float(input("Digite a altura da sua mãe: "))
peso = float(input("Digite o peso da sua mãe: "))
imc_mother = imc.calcula_imc(peso, altura)
imc_type_mother = imc.classifica_imc(imc_mother)
#print(f"Seu imc é de: {imc:.2fLeo}")

print("{} seu imc é de: {:.2f}".format(nome, imc_person))
print("Categoria do imc: {}".format(imc_type_person))
print("{} o imc da sua mãe é de: {:.2f}".format(nome_mother, imc_mother))
print("Categoria do imc: {}".format(imc_type_mother))
