# Projeto 02 – Jogo Jokenpô
# Utilizando os conceitos aprendidos até estruturas de repetição, crie um
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha
# de quantidade de rodadas, se não finalize o programa.

from random import randint
from time import sleep
var = 0
itens = ['PEDRA','PAPEL', 'TESOURA']
escolha_usuario = 0
escolha_com = randint(0,2)
contador_jogador = 0
contador_computador = 0
contador_empate = 0
jogar_novamente = ' '

print('-='*20, 'JOKENPÔ','-='*20)
quantidade_rodadas = int(input('melhor de quantas rodadas ??? : '))
while jogar_novamente !='N':
    while var != quantidade_rodadas:
        print('-='*20, 'JOKENPÔ','-='*20)
        escolha_usuario = int(input(' Vai jogar o que ?? Digite [0] PEDRA [1] PAPEL [2] Tesoura '))
        print('JO')
        sleep(1)
        print('Ken')
        sleep(1)
        print('PÔ !!!')
        print('='*30)
        if escolha_com == 0:
            if escolha_usuario == 0:
                print('Empate !!!')
                contador_empate += 1
            elif escolha_usuario == 1:
                print('Você venceu !!! ')
                print('='*30)     
                contador_jogador += 1
            elif escolha_usuario == 2:
                print('O PC venceu !!!')
                print('='*30)     
                contador_computador += 1 
            else:
                print('Jogada inválida !!!')   
        elif escolha_com == 1:
            if escolha_usuario == 0:
                print('O PC ganhou !!!')
                print('='*30)     
                contador_computador += 1
            elif escolha_usuario == 1:
                print('Empate !!! ')
                print('='*30)     
                contador_empate += 1
            elif escolha_usuario == 2:
                print('você Ganhou !!!')
                print('='*30)     
                contador_jogador += 1
            else:
                print('Jogada inválida !!!')
        elif escolha_com == 2:
            if escolha_usuario == 0:
                print('Você ganhou !!!')
                print('='*30)     
                contador_jogador += 1
            elif escolha_usuario == 1:
                print('O PC ganhou !!!')
                print('='*30)     
                contador_computador += 1
            elif escolha_usuario == 2:
                print('Empate !!!')
                print('='*30)     
                contador_empate += 1
            else:
                print('Jogada inválida !!!')
        
        print(f'Voce jogou {itens[escolha_usuario]}')
        print(f'O PC jogou {itens[escolha_com]}')
        print('='*30)     
        var += 1
    print(f'Você venceu {contador_jogador} vez(es) !!!')
    print(f'O PC venceu {contador_computador} vez(es) !!!')
    print(f'Tivemos {contador_empate} empate(s)')
    if contador_computador < contador_jogador:
        print('Você é o Grande Campeão !!!')
    elif contador_computador > contador_jogador:
        print('O PC é o Grande Campeão!!!')
    else:
        print('Deu empate')
    print('=='*30)
    jogar_novamente = str(input('Deseja jogar novamente [S/N] ')).upper()
    if jogar_novamente == 'S':
        var = 0
    else:
        print('Ficou com medinho??? hahaha')
print('GAME OVER !!!')