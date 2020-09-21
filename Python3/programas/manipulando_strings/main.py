from ExtratorArgumentoURL import ExtratorArgumentoURL

url ="https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"


cambio = ExtratorArgumentoURL(url)
moedaOrigem,moedaDestino = cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem, moedaDestino, valor)


