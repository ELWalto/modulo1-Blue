# Projeto 03 – Simulador de Votação
# Crie um programa que simule um sistema de votação, ele deve receber votos 
# até que o usuário diga que não tem mais ninguém para votar, esse programa 
# precisa ter duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como 
# parâmetro o ano de nascimento de uma pessoa que será digitado pelo usuário, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
# OPCIONAL e OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que 
# virá da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, 
# caso o contrário a 2° função deve validar o número que a pessoa escolheu, ela 
# pode escolher de 1 a 5 (crie 3 candidatos para a votação):
# 1, 2 ou 3 - Votos para os respectivos candidatos
# 4- Voto Nulo
# 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# Qual candidato venceu a votação.
# Obs: O projeto deve ser feito individualmente e entregue até o final da aula 17



from datetime import date
data = date.today().year

contador_nulo = 0
contador_branco = 0
candidatos = [{"codigo": '1', "Nome": "Batman", "votos": 0},
                {"codigo": '2', "Nome": "Mulher Maravilha", "votos": 0},      
                {"codigo": '3', "Nome": "Thor", "votos": 0}]### Dicionario criado com código para cada candidato ja declarando que voto é 0

def autoriza_voto(ano):### funçao que recebe o ano de nascimento de um usuário p/ validar se pode votar ou não
    idade =  data - ano
    if idade < 16:
        print(f" Com {idade} anos, você \033[1;31;40m NÃO pode votar!\033[m")
        return 0
    if 16 <= idade < 18 or idade > 70:
        print(f" Com {idade} anos o voto é   \033[1;31;40m OPCIONAL!\033[m")
        return 1
    if  idade >16 and idade <= 70:
        print(f" Com {idade} anos o voto é   \033[1;31;40m OBRIGATORIO!\033[m")
        return 2

def tela():
    print(f'Digite um número:') ### Função que exibe as opções de voto pegando o codigo e nome do candidato no dicionario criado
    for i in candidatos:
        print (f'[{i["codigo"]}] - {i["Nome"]}')
    print('[4] - Voto NULO')    
    print('[5] - Voto em BRANCO')
    voto = input("Digite o número do seu voto : ")
    return voto

def votacao(autoriza, voto): # Função que valida o voto digitado pelo usuário  

    if autoriza > 0 :
        global contador_nulo
        global contador_branco
        if voto.strip()[0].isnumeric():
            if voto == '5':
                contador_branco += 1
            elif int(voto) <= len(candidatos):
                candidatos[int(voto) - 1]["votos"] += 1
            else:
                contador_nulo += 1
        else:
            contador_nulo += 1
    if autoriza == 0 :
        print(" Com esta idade você \033[4;31;40m NÃO pode votar!\033[m")

def apuracao(): # Função criada para a apuração  os votos
    numero_votos = 0
    print( f" \033[4;31;40m Resultado \033[m ")
    votos_total = 0
    for i in range(len(candidatos)):
        print(f"{candidatos[i]['Nome']} votos: {candidatos[i]['votos']}")
        numero_votos += candidatos[i]['votos']
        if candidatos[i]['votos'] > votos_total:
            votos_total = candidatos[i]['votos']
     
    vencedores = []
    for i in candidatos:
        if i["votos"] == votos_total:
            vencedores.append(i)

    print(f"Votos Brancos {contador_branco}")

    print(f"Votos Nulos {contador_nulo}")
    
    print(f'{100 * contador_branco / (numero_votos + contador_branco + contador_nulo):.1f}% de votos Brancos')
    
    print(f'{100 * contador_nulo / (numero_votos + contador_branco + contador_nulo):.1f}% de votos Nulos')
    
    print(f'Total de votos: {numero_votos + contador_branco + contador_nulo}')
    
    print(f'Total de votos válidos: {numero_votos}')
    
    if len(vencedores) > 1:
        print(f'Houve empate entre os candidatos:')
        for i in vencedores:
            print(i["Nome"])
        print(f'Cada um deles obtiveram {100 * vencedores[0]["votos"] / numero_votos:.1f}% dos votos válidos.')
    elif len(vencedores) <= 1:
        print(f'O(A) cadidato(a) {vencedores[0]["Nome"]} venceu a eleição com {100 * vencedores[0]["votos"] / numero_votos:.1f}% dos votos válidos.')

    

print (f'-=-=-= \033[1;31;40m ELEICOES {data}   \033[m -=-=-=- ')
while True:
    ano_nasc= int(input("Digite o ano de nascimento do eleitor:"))
    autoriza = autoriza_voto(ano_nasc)
    voto = tela().strip() 
    votacao(autoriza, voto)
    resp = input("Votar novamente ??? (Sim/Não) ").upper()[0]
    if resp == 'S':
        pass
    elif resp == 'N':
            break
    else:
        print("OPÇÃO INVÁLIDA!")
    
apuracao()