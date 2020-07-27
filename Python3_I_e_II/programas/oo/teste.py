def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("saldo {}".format(conta["saldo"]))

def ola():
    print("ola mundo")

if __name__ == '__main__':
    print("iniciando")
    ola()
