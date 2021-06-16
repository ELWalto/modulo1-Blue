#PROJETO DETETIVE

pergunta_1 = (str(input("Você telefonou para a vítima? Digite SIM ou NÃO \n").upper()))
pergunta_2 = (str(input("Você esteve no local do crime? Digite SIM ou NÃO \n").upper()))
pergunta_3 = (str(input("Você mora perto da vítima? Digite SIM ou NÃO \n").upper()))
pergunta_4 = (str(input("Você devia para a vítima? Digite SIM ou NÃO \n").upper()))
pergunta_5 = (str(input("Você já trabalhou com a vítima? Digite SIM ou NÃO \n").upper()))

contador = 0

if pergunta_1 == "SIM":  # aqui testo todas as perguntas e quando a resposta for 'sim' adiciono 1 a variável "contador"
  contador = contador + 1
if pergunta_2 == "SIM":
  contador = contador + 1
if pergunta_3 == "SIM":
  contador = contador + 1
if pergunta_4 == "SIM":
  contador = contador + 1
if pergunta_5 == "SIM":
  contador = contador + 1

if contador == 2:
  print(f"O número de respostas sSIM foram {contador}, portanto você é considerado(a) SUSPEITO(a)" )
elif contador == 3 or contador == 4 :
  print(f"O número de respostas SIM foram {contador}, portanto você é considerado(a) CÚMPLICE")
elif contador == 5:
  print(f"O número de respostas SIM foram {contador}, portanto você é considerado(a) ASSASSINO(A)" )
else:
  print("você é INOCENTE")