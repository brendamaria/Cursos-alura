from Conta import Conta

conta_guilherme = Conta(32)
conta_guilherme.deposita(100)

conta_daniela = Conta(43)
conta_daniela.deposita(200)

print(conta_guilherme.saldo())
print(conta_daniela.saldo())

conta_guilherme + 20

print(conta_guilherme.saldo())

conta_paulo = Conta(65)
conta_paulo.deposita(300)

conta = [conta_guilherme, conta_daniela, conta_paulo]

print(conta_guilherme)
print(conta_paulo)
print(conta_daniela)

print(conta_guilherme < conta_paulo)
print(conta_daniela < conta_guilherme)

print(conta_guilherme == conta_guilherme)

print(conta_paulo <= conta_daniela)
print(conta_guilherme <= conta_guilherme)
