from os import fsdecode
import modulos_projeto_final as mod

hora = mod.Relogio()
foodTruck = mod.Estabelecimento('Comeu Morreu')
mod.mostrar_titulo_tela()
# introdução do jogo
gameOver = False
dia = 1
estabelecimentoAberto = False

while not gameOver:
    if not estabelecimentoAberto:
        escolha = '-1'
        while escolha not in '01234':
            if dia == 5 or dia == 35:
                contas = 500
                print(f'Você pagou suas contas no valor de R$: {contas:.02} reais....')
                foodTruck.saidaCaixa(contas)
                print(f'Ficou com um caixa de R$: {foodTruck.caixa:.2f} reais.')
            print(f'Esse é seu {dia}º dia.')
            print(f'Você é dono do Food Truck \033[1;31m{foodTruck.nome}\033[m.')
            print(f'Agora são {hora.horas}:{hora.minutos:02d}Hs.')
            print('Seu estabelecimento está ' + ('Sujo.' if foodTruck.estabelecimentoSujo else 'Limpo.'))
            # print(f'Você tem em caixa R${foodTruck.caixa:.2f}')
            print('Seu estoque ' + ('está cheio.' if foodTruck.estoqueCheio else 'foi consumido.'))
            print('O que você gostaria de fazer?\n')
            # escolha = input('[1] Abrir food truck.\n[2] Ver estoque.\n[3] Sair do jogo.\n')
            print('[1] Abrir food truck.')
            print('[2] Ver estoque.')
            if foodTruck.estabelecimentoSujo: print('[3] Limpar Estabelecimento.')
            if not foodTruck.estoqueCheio: print('[4] Repor estoque.')
            print('[0] Sair do Jogo')
            escolha = input()
            if escolha == '1':
                print()
                foodTruck.abrirEstabelecimento()
                estabelecimentoAberto = True
                print()
            elif escolha == '2':
                print('Estoque:')
                foodTruck.exibirEstoque()
                hora.avancaTempo(5)
                print()
            elif escolha == '3':
                foodTruck.limparEstabelecimento()
                print()
                continue
            elif escolha == '4':
                foodTruck.entradaMercadorias()
                continue
            elif escolha == '0':
                gameOver = True
                break
            else:
                print('Escolha inválida. Escolha opções de 1 a 3.')
        cliente1 = 0 # contador número clientes
    if estabelecimentoAberto:
        cliente1 += 1
        print(f'Você recebeu seu {cliente1}º pedido.')
        cliente = mod.Cliente(1.70,'forte',True)
        cliente.fazerPedido()
        print('Você precisa preparar o pedido. Escolha os ingredientes:')
        ingredientes = '0'
        cardapio = mod.Cardapio() # Pegar o pedido no cardápio
        pedido = cardapio.pratos[cliente.pedidoComida]
        itensEmEstoque = True
        while '1234567' not in ingredientes: #aqui so invertendo que ficava no loop
            print()
            ingredientes = input('[1] Pegar salada.\n[2] Pegar queijo.\n[3] Pegar presunto.\n[4] Pegar ovo.\n[5] Pegar bacon.\n[6] Pegar pão.\n[7] Pegar hamburguer.\n') #aqui näo tinha como colocar as bebidas, onde colocar as opções das bebidas?
            if ingredientes == '1':
                if not foodTruck.saidaEstoque('Salada'):
                    itensEmEstoque = False
                    break
                print('adicionando os ingredientes....')
                mod.time.sleep(2)
                if 'Salada' not in pedido:
                    print('Ops Ingrediente errado, você desperdiçou tempo e ingrediente.')
                    hora.avancaTempo(5)
                else:
                    print('Ingrediente correto. Defina o próximo passo.')
                    mod.EliminarItemPedido('Salada',pedido)
                    
            elif ingredientes == '2':
                print('adicionando os ingredientes....')
                mod.time.sleep(2)
                if not foodTruck.saidaEstoque('Queijo'):
                    itensEmEstoque = False
                    break
                if 'Queijo' not in pedido:
                    print('Ops Ingrediente errado, você desperdiçou tempo e ingrediente.')
                    hora.avancaTempo(5)
                else:
                    print('Ingrediente correto. Defina o próximo passo.')               
                    mod.EliminarItemPedido('Queijo',pedido)
                    
                    
            elif ingredientes == '3':
                print('adicionando os ingredientes....')
                mod.time.sleep(2)
                if not foodTruck.saidaEstoque('Presunto'):
                    itensEmEstoque = False
                    break
                if 'Presunto' not in pedido:
                    print('Ops Ingrediente errado, você desperdiçou tempo e ingrediente.')
                    hora.avancaTempo(5)
                else:
                    print('Ingrediente correto. Defina o próximo passo.')               
                    mod.EliminarItemPedido('Presunto',pedido)
                    
            elif ingredientes == '4':
                print('adicionando os ingredientes....')
                mod.time.sleep(2)
                if not foodTruck.saidaEstoque('Ovos'):
                    itensEmEstoque = False
                    break
                if 'Ovo' not in pedido:
                    print('Ops Ingrediente errado, você desperdiçou tempo e ingrediente.')
                    hora.avancaTempo(5)
                else:
                    print('Ingrediente correto. Defina o próximo passo.')
                    mod.EliminarItemPedido('Ovo',pedido)
                    
            elif ingredientes == '5':
                print('adicionando os ingredientes....')
                mod.time.sleep(2)
                if not foodTruck.saidaEstoque('Bacon'):
                    itensEmEstoque = False
                    break
                if 'Bacon' not in pedido:
                    print('Ops Ingrediente errado, você desperdiçou tempo e ingrediente.')
                    hora.avancaTempo(5)
                else:
                    print('Ingrediente correto. Defina o próximo passo.')              
                    mod.EliminarItemPedido('Bacon',pedido)
                    
            elif ingredientes == '6':
                print('adicionando os ingredientes....')
                mod.time.sleep(2)
                if not foodTruck.saidaEstoque('Pão'):
                    itensEmEstoque = False
                    break
                if 'Pão' not in pedido:
                    print('Ops Ingrediente errado, você desperdiçou tempo e ingrediente.')
                    hora.avancaTempo(5)
                else:
                    print('Ingrediente correto. Defina o próximo passo.')              
                    mod.EliminarItemPedido('Pão',pedido)
                    
            elif ingredientes == '7':
                print('adicionando os ingredientes....')
                mod.time.sleep(2)
                if not foodTruck.saidaEstoque('Hamburguer'):
                    itensEmEstoque = False
                    break
                if 'Hamburguer' not in pedido:
                    print('Ops Ingrediente errado, você desperdiçou tempo e ingrediente.')
                    hora.avancaTempo(5)
                else:
                    print('Ingrediente correto. Defina o próximo passo.')               
                    mod.EliminarItemPedido('Hamburguer',pedido)
            else:
                print('Escolha inválida. Escolha opções de 1 a 7.') 
            if pedido == []:
                print('\nPedido entregue.\n')
                hora.avancaTempo(30)
                if hora.horas < 24:
                    print(f'Agora são {hora.horas}:{hora.minutos:02d}Hs.')
                if cliente.pedidoComida == 'X-Tudo':
                    valorLanche = 30
                elif cliente.pedidoComida == 'Misto Quente':
                    valorLanche = 10
                elif cliente.pedidoComida == 'X-Salada':
                    valorLanche = 20
                elif cliente.pedidoComida == 'X-Bacon':
                    valorLanche = 25
                foodTruck.entradaCaixa(cliente.gorjeta() + cliente.pagar(valorLanche))  # Verificar depois  a iteração 
                print(f'Você recebeu R$: {cliente.pagar(valorLanche):.02f} reais pelo {cliente.pedidoComida}.')
                if cliente.gorjeta() > 0:
                    print(f'Você recebeu R$: {cliente.gorjeta()} reais de gorjeta. ')
                print(f'Você ficou com um caixa de R$: {foodTruck.caixa:.02f} reais.')
                break
        if hora.horas >= 24:
            print(f'Já passou das 00:00Hs e você fechou seu estabelecimento...')
            print('Tenha um bom descanso...')
            foodTruck.fecharEstabelecimento()
            foodTruck.estabelecimentoSujo = True
            hora.horas = 19
            hora.minutos = 0
            mod.time.sleep(5)
            dia += 1
            estabelecimentoAberto = False            
        if not itensEmEstoque:
            print('Você não conseguirá entregar o pedido, pois faltam ingredientes.')
        opcoes = '0'
        while opcoes not in '234' and estabelecimentoAberto:
            opcoes = input('\nO que gostaria fazer?\n[1] Fazer Compras para reabastecer o estoque.\n[2] Fechar food truck.\n[3] Aguardar próximo cliente.\n[4] Sair do Jogo.\n')            
            if opcoes == '1':
                if not foodTruck.estoqueCheio:
                    foodTruck.entradaMercadorias()
                    print('Indo as compras....')
                    mod.time.sleep(5)
                    print('Pronto, compras feitas.')
                    print('Estoque: ')
                    foodTruck.exibirEstoque()
                else:
                    print('Você está com o um bom estoque, não precisa fazer compras.')
            elif opcoes == '2':
                foodTruck.fecharEstabelecimento()
                foodTruck.estabelecimentoSujo = True
                print('Tenha um bom descanso...\n')
                hora.horas = 19
                hora.minutos = 0
                mod.time.sleep(5)
                dia += 1
                estabelecimentoAberto = False
            elif opcoes == '4':
                estabelecimentoAberto = False
                gameOver = True
                break
            elif opcoes == '3':
                print('Aguardando o próximo cliente...')
                mod.time.sleep(5)
            else:
                print('Opção inválida... Escolha de 1 a 4.')
else:
    mod.game_over()