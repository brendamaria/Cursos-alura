numeros_aleatorios = [92, 29, 21, 92, 12, 89]
mais_numeros_aleatorios = [54, 65, 12, 54, 29]


print(type(numeros_aleatorios))
set(numeros_aleatorios)
print(numeros_aleatorios)

todos_numeros_aleatorios = numeros_aleatorios.copy()
todos_numeros_aleatorios.extend(mais_numeros_aleatorios)
print(todos_numeros_aleatorios)

print(set(todos_numeros_aleatorios))

teste = {32, 53, 18, 74}
segundo_teste = {53, 67, 32, 76}

print(teste | segundo_teste)

print(teste & segundo_teste)

print(teste - segundo_teste)

print(teste ^ segundo_teste)