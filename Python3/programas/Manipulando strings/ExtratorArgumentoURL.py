class ExtratorArgumentoURL:
    def __init__(self, url):
        if self.stringValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida")

    @staticmethod
    def stringValida(url):
        if url:
            return True
        else:
            return False

    def verificaMoedaOrigem(self, buscaMoedaOrigem):
        self.url = self.url.replace("moedadestino", "real", 1)
        inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
        finalSubstringMoedaOrigem = self.url.find("&")
        return self.url[inicioSubstringMoedaOrigem:finalSubstringMoedaOrigem]

    def retornaMoedas(self):
        buscaMoedaOrigem = "moedaorigem"
        buscaMoedaDestino = "moedadestino"

        inicioMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
        finalMoedaOrigem = self.url.find("&")
        moedaOrigem = self.url[inicioMoedaOrigem:finalMoedaOrigem]

        if moedaOrigem == "moedadestino":
            self.verificaMoedaOrigem(buscaMoedaOrigem)
            inicioMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
            finalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[inicioMoedaOrigem:finalMoedaOrigem]

        inicioMoedaDestino = self.encontraIndiceInicioSubstring(buscaMoedaDestino)
        finalMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[inicioMoedaDestino:finalMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicioSubstring(self, moedaOuValor):
        return self.url.find(moedaOuValor) + len(moedaOuValor) + 1

    def retornaValor(self):
        buscaValor = "Valor".lower()
        inicioSubstringValor = self.encontraIndiceInicioSubstring(buscaValor)
        valor = self.url[inicioSubstringValor:]
        return valor

    def __str__(self):
        moedaOrigem, moedaDestino = self.retornaMoedas()
#        representacaoString2 = "Valor: " + self.retornaValor() + " " + moedaOrigem + " " moedaDestino
        representacaoString = "\nValor: {}\nMoeda Origem: {}\nMoeda Destino: {} \n".format(self.retornaValor(), moedaOrigem, moedaDestino)
        return representacaoString

    def __len__(self):
        return len(self.url)

    def __eq__(self, compara):
        return self.url == compara.url


