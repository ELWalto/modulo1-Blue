# #1 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmfF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print(f'Sexo registrado com sucesso {sexo}') 

    




# 2 - Escreva um programa que pede a senha uma senha ao usuário, e só sai do loop quando digitarem
# corretamente a senha. A senha é “Blue123”
# 2b - Exiba quantas vezes o usuário errou a digitação.
senha = 'Blue123'
entrada = " "
cont = 0
while senha != entrada:
    entrada = input('informe a senha correta')
    cont+=1
    if entrada == senha:
        print('acesso liberado')
print(f'O numero de tentativas incorretas foi {cont}')

# 3 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No
# final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

idade18 = 0
homens = 0
mulher20 = 0
totcadastrados = 0
while True:
    idade = int(input('informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('informe o sexo: [M/F] ')).upper()
    if idade >= 18:
        idade18 += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    if sexo == 'M':
        homens += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).upper()
    if r == 'N':
        break
totcadastrados = homens + mulher20 + idade18
print(f'O total de cadastros foi {totcadastrados} ')
print(f'O total de cadastrados com mais de 18 anos foi {idade18}')
print(f'O total de homens cadstrados foi {homens}')
print(f'O total de mulheres  cadastradas com menos de 20 anos foi {mulher20}')
print('Fim')



# DESAFIO:
# 4 - Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar
# adivinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram
# necessários para vencer.
from random import randint
n = int(input('Digite um número de 0 a 10: '))
comp = randint(0, 10)
while n != comp:
    print('ERROOOOU. Tente novamente.')
    n = int(input('Digite um número de 0 a 10: '))
if n == comp:
    print(f'VOCÊ ACERTOOOOU. O computador pensou em {comp}')