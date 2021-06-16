




# 04 - Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a
# soma deles (o usuário vai dizer quantos números serão informados antes de começar)
soma = 0 #utilizo essa variavel como auxiliar para armazenar temporariamente os numeros para soma

quantidade_numeros = int(input('informe quantos numeros vc quer somar'))

for i in range (quantidade_numeros):# aqui o for é repetido quantas vezes o usuário informar
    soma = soma + int(input('informe outro numero')) #armazeno os números informados e efetuo a soma
print(soma)
