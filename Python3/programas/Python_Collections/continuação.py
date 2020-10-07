numeros_aleatorios = [92, 29, 21, 92, 12, 89]
mais_numeros_aleatorios = [54, 65, 12, 54, 29]


print(type(numeros_aleatorios))
set(numeros_aleatorios)
print(numeros_aleatorios)
print("---------------------------")

todos_numeros_aleatorios = numeros_aleatorios.copy()
todos_numeros_aleatorios.extend(mais_numeros_aleatorios)
print(todos_numeros_aleatorios)

print(set(todos_numeros_aleatorios))
print("---------------------------")

teste = {32, 53, 18, 74}
segundo_teste = {53, 67, 32, 76}

print(teste | segundo_teste)
print(teste & segundo_teste)
print(teste - segundo_teste)
print(teste ^ segundo_teste)
print("---------------------------")
teste.add(53)
print(teste) #não adiciona itens repetidos
teste.add(43)
print(teste)

teste_congelado = frozenset(teste)
print(type(teste_congelado))
#teste_congelado.add(43)
print("---------------------------")
texto = "Mas quando falamos de conjuntos, falamos meio que não tem início e fim, não tem posição inicial e posição final"

print(texto)

meu_texto = texto.split() #usa o parametro padrao " "
print(meu_texto)

print(set(meu_texto)) #todas as palavras sem repeticao


