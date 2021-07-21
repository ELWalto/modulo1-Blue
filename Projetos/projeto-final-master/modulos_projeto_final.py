from random import choice
import time 
class Relogio:
    def __init__(self):
        self.horas = 19
        self.minutos = 0 


    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

class Clima:
    def __init__(self,chuva,neve,furacao):
        self.chuva = chuva
        self.neve = neve
        self.furacao = furacao

class Pessoa:
    def __init__(self,altura,forca,satisfacao):
        self.altura = altura
        self.forca = forca
        self.satisfacao = satisfacao

class Cliente(Pessoa):
    alergias = [True,False]
    pedidoComida = ['Misto Quente','X-Salada','X-Tudo','X-Bacon']
    pedidoBebida = ['Suco','Fanta','Agua','Coca']
    recompensa = [10.00, 0]
    def __init__(self,altura,forca,satisfacao):
        super().__init__(altura,forca,satisfacao)
        self.alergia = choice(self.alergias)
        self.pedidoComida = choice(self.pedidoComida)
        self.pedidoBebida = choice(self.pedidoBebida)
        self.gorjetaCliente = choice(self.recompensa)
        
    def fazerPedido(self):
        print(f'Cliente : "Olá, eu gostaria de um {self.pedidoComida} e para beber um(a) {self.pedidoBebida}".')
    def reclamar():
        pass
    def brigar():
        pass
    def xingar():
        pass
    def pagar(self,valorLanche):
        return valorLanche    
    def gorjeta(self):
        return self.gorjetaCliente
    
    def elogiar():
        pass

class Dono(Pessoa):
    def __init__(self,altura,forca,satisfacao):
        super().__init__(altura,forca,satisfacao)        
        self.lista = ['mal dia', 'bom dia', 'desastrado']

    def fazerCompras():
        # Aguardando a classe Estabelecimento
        #                     - estoque
        #                     - saldo
        pass
    def pagagamentos():
        # Aguardando a classe Estabelecimento
        pagarAssistente = False;
        pagarContas = False;
        pass

class Assistente(Pessoa):
    def __init__(self,altura,forca,satisfacao,salario):
        super().__init__(altura,forca,satisfacao)  
    def receberSalario(self,valor):
        print('Você recebeu ' + valor + 'de' + 'gorjeta' if self.valor < 50 else 'salário.')

    def faltarTrabalho(self):
        print('Seu ajudante faltou.')

    def reclamar(self):
        print('Seu funcionário não está feliz e reclamou.')

class Cardapio: 
    def __init__(self):
        self.pratos = {'Misto Quente': ['Pão', 'Presunto', 'Queijo'], 'X-Salada': ['Pão', 'Hamburguer', 'Queijo', 'Salada'], 'X-Tudo': ['Pão', 'Hamburguer', 'Ovo', 'Queijo', 'Bacon', 'Salada'], 'X-Bacon': ['Pão', 'Hamburguer', 'Queijo','Bacon']}
        self.bebidas = ['Coca','Fanta','Suco','Agua']
        
class Estabelecimento:
    def __init__(self,nome):
        self.estoque = {'Pão': 10, 'Hamburguer': 10, 'Salada': 10, 'Queijo': 10, 'Presunto': 10, 'Ovos': 10, 'Bacon': 10, 'Carne': 10, 'Frango': 10}
        self.bebidas = {'Coca':10, 'Fanta':10, 'Suco': 10, 'Agua': 10}
        self.caixa = 800.00
        self.estoqueCheio = True
        self.estabelecimentoSujo = False
        self.nome = nome
    
    def entradaMercadorias(self):
        for i in self.estoque:
            self.estoque[i] = 10
        self.estoqueCheio = True
        self.saidaCaixa(150.00)
    def exibirEstoque(self):
        for c, v in self.estoque.items():
            print(f'{c} -> Quantidade: {v}') 

    def saidaEstoque(self,key):
        if self.estoque[key] > 0:
            self.estoque[key] -= 1
        else:
            print(f'Você não tem mais {key} em estoque.')
            self.estoqueCheio = False
            return False
        return True
    def entradaCaixa(self,valor):
        self.caixa += valor
        
    def saidaCaixa(self,valor):
        self.caixa -= valor

    def abrirEstabelecimento(self):
        print(f'Seu Estabelecimento {self.nome} foi aberto.')
    
    def fecharEstabelecimento(self):
        print(f'Seu Estabelecimento {self.nome} foi fechado.')

    def limparEstabelecimento(self):
        self.estabelecimentoSujo = False
        print(f'Seu Estabelecimento {self.nome} foi limpo.') 

# def EliminarItemPedido(ingrediente,pedido):
#     for i in range(len(pedido)):
#         if pedido[i] == ingrediente:
#             del pedido[i]
#             break
def EliminarItemPedido(ingrediente,pedido = []):
    if isinstance(pedido, list):
        for i in range(len(pedido)):
            if pedido[i] == ingrediente:
                del pedido[i]
                break    
class Recompensa:
    def __init__(self, fidelizacao, popularidade):
        self.fidelizacao = fidelizacao
        self.popularidade = popularidade

class Punicao:
    def __init__(self, xingamento , reclamacoes , perda_popularidade):
            #cliente não pagou pelo prato
            #sem renda / não consegue pagar as conta ) 
        self.xingamento = xingamento
        self.reclamacoes = reclamacoes
        self.perda_popularidade = perda_popularidade

    # faltando - metodo get atributo 
    # alterando
     

def mostrar_titulo_tela():
    from time import sleep


    titulo_frame1 = '''\033[1;31m 
  ____   ___   ____    ____  _   _    ____    ___    ____   ____   ____  _   _ 
 / ___) / _ \ |    \  / _  )| | | |  |    \  / _ \  / ___) / ___) / _  )| | | |
( (___ | |_| || | | |( (/ / | |_| |  | | | || |_| || |    | |    ( (/ / | |_| |
 \____) \___/ |_|_|_| \____) \____|  |_|_|_| \___/ |_|    |_|     \____) \____|
                                                                              
\033[m '''


    
    sleep(0.1)
    
    titulo_frame2 = '''\033[1;31,40m
  ____   ___   ____    ____  _   _    ____    ___    ____   ____   ____  _   _ 
 / ___) / _ \ |    \  / _  )| | | |  |    \  / _ \  / ___) / ___) / _  )| | | |
( (___ | |_| || | | |( (/ / | |_| |  | | | || |_| || |    | |    ( (/ / | |_| |
 \____) \___/ |_|_|_| \____) \____|  |_|_|_| \___/ |_|    |_|     \____) \____|
                                                                              
     \033[m '''
    import time, os 
    startTime = time.time()
    currentTime = time.time()
    counter = 0

    while(currentTime < startTime + 3.0):
        if counter % 2 == 0:
            print(titulo_frame1)
        else:
            print(titulo_frame2)
        counter += 1
        
        os.system('cls')               
        time.sleep(0.08)
        currentTime = time.time()
        
    print(startTime)
def game_over():
    titulo_game_over1 = '''\033[1;31m
   ___                                      ___                           
  / __|   __ _    _ __     ___      o O O  / _ \   __ __    ___      _ _  
 | (_ |  / _` |  | '  \   / -_)    o      | (_) |  \ V /   / -_)    | '_| 
  \___|  \__,_|  |_|_|_|  \___|   TS__[O]  \___/   _\_/_   \___|   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' \033[m
    
    '''

    print(titulo_game_over1)

if __name__ == '__main__':
    mostrar_titulo_tela()

    game_over() 