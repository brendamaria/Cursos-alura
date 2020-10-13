from collections import defaultdict
from collections import Counter


numeros_aleatorios = [92, 29, 21, 92, 12, 89]
mais_numeros_aleatorios = [54, 65, 12, 54, 29]


print(type(numeros_aleatorios))
set(numeros_aleatorios)
print(numeros_aleatorios)
print("\n------------criando copia---------------")

todos_numeros_aleatorios = numeros_aleatorios.copy()
todos_numeros_aleatorios.extend(mais_numeros_aleatorios)
print(todos_numeros_aleatorios)

print(set(todos_numeros_aleatorios))
print("\n------------teste de operações---------------")

teste = {32, 53, 18, 74}
segundo_teste = {53, 67, 32, 76}

print(teste | segundo_teste)
print(teste & segundo_teste)
print(teste - segundo_teste)
print(teste ^ segundo_teste)
print("\n------------teste de repetição---------------")
teste.add(53)
print(teste) #não adiciona itens repetidos
teste.add(43)
print(teste)

teste_congelado = frozenset(teste)
print(type(teste_congelado))
#teste_congelado.add(43)
print("\n------------texto---------------")
texto = "Mas quando falamos de conjuntos, falamos meio que não tem início e fim, não tem posição inicial e posição final"

print(texto)

meu_texto = texto.split() #usa o parametro padrao " ", quebra de texto
print(meu_texto)
print(set(meu_texto)) #todas as palavras sem repeticao

#dicionario
print("\n------------dicionario---------------")

texto_tratado = texto.lower()
apariocoes = {}

for palavra in texto_tratado.split(): #criando dicionario para palavras do texto
    ate_agora = apariocoes.get(palavra, 0)
    apariocoes[palavra] = ate_agora + 1

print(apariocoes)

print("\n------------dicionario default---------------")

apariocoes = defaultdict(int) ##caso não tenha retorna 0

for palavra in texto_tratado.split():
    apariocoes[palavra] += 1

print(apariocoes)

print("\n------------contador---------------")

print(Counter(texto_tratado))