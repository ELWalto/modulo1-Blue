num_notas100 = 0
num_notas50 = 0
num_notas10 = 0
num_notas5 = 0
num_notas1 = 0
auxiliar = 0
saque = float(input('informe o valor para saque "entre 10 e 600"'))
while saque < 10 or saque > 600:
    saque = float(input(' A quantidade informada não é permitida, informe um valor entre 10 e 600 '))
auxiliar = saque
num_notas100 = int(auxiliar//100)
auxiliar += -(num_notas100*100)

num_notas50 = int(auxiliar // 50)
auxiliar += -(num_notas50*50)

num_notas10 += int(auxiliar //10)
auxiliar += -(num_notas10*10)

num_notas5 += int(auxiliar //5)
auxiliar += -(num_notas5*5)

num_notas1 += int(auxiliar //1)
print(f'Para sacar a quantidade R${saque:.2f}  ')

if num_notas100 >0:
    print(f'a quantidade de nota(s) de 100 é (são):\n{num_notas100}')
if num_notas50 >0:
    print(f'a quantidade de nota(s) de 50 é(são):\n{num_notas50}')
if num_notas10 >0:
    print(f'a quantidade de nota(s) de 10 é(são):\n{num_notas10}')
if num_notas5 >0:
    print(f'a quantidade de nota(s) de 5 é(são):\n{num_notas5}')
if num_notas1 >0:
    print(f'a quantidade de nota(s) de 1 é(são) :\n{num_notas1}')


