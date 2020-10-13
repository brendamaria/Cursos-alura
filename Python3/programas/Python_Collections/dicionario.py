

apariocoes = {"guilherme" : 1, "cachorro" : 2, "nome" : 2, "vindo" : 1}

teste = "cachorro" in apariocoes
segundoTeste = "carlos" in apariocoes
naoTem = apariocoes.get("xpto", 0) #caso não tenha retorna 0

print(teste)
print(segundoTeste)
print(naoTem)


for elemento in apariocoes:
    print(elemento)

for elemento in apariocoes.values():
    print(elemento)

for elemento in apariocoes.items():
    print(elemento)

apariocoes["carlos"] = 3
print(apariocoes)

apariocoes["carlos"] = 5
print(apariocoes)

del apariocoes["carlos"]
print(apariocoes)



