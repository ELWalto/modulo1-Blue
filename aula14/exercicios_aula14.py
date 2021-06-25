# Exercícios

# 1.	Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

# def somar(num1,num2,num3): # definindo uma função
#     '''
#     pede dois numeros para o usuario e printa o resultado da soma dos dois # aqui defino o help para saber o que a funcao faz
#     '''
#     soma = num1 + num2 + num3
#     print(f'a soma dos numeros {num1} , {num2} e {num3} é {soma} ')
# a = 10
# b = 20
# c = 30
# somar(a,b,c)


# 2.	 Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

# def positiva (numero):
#     if numero > 0:
#         return 'P'
#     elif numero < 0:
#         return 'N'
#     else:
#         return 0
# n = int(input(' Informe um número: '))
# print(positiva(n))


# 3.	 Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

# def somaImposto (taxaImposto , custo):
#     taxaImposto = custo * taxaImposto/100
#     preco_venda = custo + taxaImposto
#     return preco_venda
# valorProduto = float(input(' Digite o valor do produto: ').replace(',','.'))
# valorTaxa = float(input(' Digite o valor da taxa: ').replace(',','.'))
# print(f'O preço de venda será : {somaImposto(valorTaxa,valorProduto)} ')



# 4.	Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

# def salario (valorhora,qthoras):
#     if qthoras <= 40:
#         salario = valorhora*qthoras
    
#     else:
#         horaextra = qthoras-40 
#         valorhoraextra = valorhora + valorhora *1.5/100
#         salario = valorhora * 40 + valorhoraextra * horaextra

#     return salario
# horas = int(input('Informe a quantidade de horas trabalhadas :'))
# cascalho = float(input(' Informe o valor da hora trabalhada :'))
# print(salario (cascalho ,horas))


    

         






# 5.	Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

# def imc():
#     a = 1.68**2
#     b = 75 
#     return round(b/a,2) # Round arredonda a quantidade de casas depois da virgula

# print(imc())


# 6.	Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).
# Nota	Conceito
# >=9.0	A
# >=8.0	B
# >=7.0	C
# >=6.0	D
# > 4.0 E 
# <=4.0	F

# def nota (a):
#     if a >= 9:
#         return "NOTA'A'"
#     elif a >= 8:
#         return "NOTA'B"
#     elif a >= 7:
#         return "NOTA'C'"
#     elif a >= 6:
#         return "NOTA'D'"
#     elif a > 4:
#         return "NOTA'E'"
#     else:
#         return "NOTA 'F'"
# boletim = float(input('Informe o valor da sua nota: ').replace(',','.'))

# print(nota(boletim))


# 7.	Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

# def comparacao(a,b):
#     if a == b:
#         return 'Iguais'
#     lista = [a,b]
#     menor = min(lista)
#     return menor 
# num1 = int(input('Informe o primeiro valor: '))
# num2 = int(input('Informe o segundo valor '))
# print(comparacao(num1,num2))






# DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.

def data_valida(data):
    try:
        # faz o split e transforma em números
        dia, mes, ano = map(int, data.split('/'))

        # mes ou ano inválido, retorna False
        if mes < 1 or mes > 12 or ano <= 0:
            return False

        # verifica qual o último dia do mês
        if mes in (1, 3, 5, 7, 8, 10, 12):
            ultimo_dia = 31
        elif mes == 2:
            if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
                ultimo_dia = 29
            else:
                ultimo_dia = 28
        else:
            ultimo_dia = 30

        # verifica se o dia é válido
        if dia < 1 or dia > ultimo_dia:
            return False

        return True
    except ValueError:
        return False

meses = {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",12:"Dezembro"}

data = input('Informe uma data DD/MM/AAAA ')
if data_valida(data) == True: 
    dia,mes,ano = data.split('/')
    print ('Data: %s de %s de %s' % (dia, meses[int(mes)], ano))
else:
    print('DATA INVÁLIDA')

