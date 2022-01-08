from ExtratorArgumentoURL import ExtratorArgumentoURL

url ="https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150"


cambio = ExtratorArgumentoURL(url)
comparacao = ExtratorArgumentoURL(url)
moedaOrigem,moedaDestino = cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem, moedaDestino, valor)

print(url.startswith("https"))

print(url.endswith("150"))

print(cambio)
print(len(cambio))


print(id(cambio))
print(id(comparacao))

print(cambio == comparacao)