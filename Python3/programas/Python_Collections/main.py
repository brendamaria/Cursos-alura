
idades = [39, 30, 27, 18]
print(idades)

idades.append(15)
print(idades)

for idade in idades:
    print(idade)

idades.append(30)
print(idades)
idades.remove(30)
print(idades)

print(27 in idades)
print(33 in idades)

if 27 in idades:
    idades.remove(27)
print(idades)

'''idades.append([33, 40])
print(idades) '''

idades.extend([33, 40])
print(idades)

idades_ano_que_vem = [(idade+1) for idade in idades]
''' for idade in idades:
    idades_ano_que_vem.append(idade + 1)'''
print(idades_ano_que_vem)
