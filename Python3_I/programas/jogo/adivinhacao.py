def jogar():

    import random

    print("********************************")
    print("Bem vindo ao jofo de adivinhção!")
    print("********************************")

    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("1-Fácil 2-Médio 3-Difícil: ")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100:")
        print("Você digitou, ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!!")
            continue

        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute
        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior que o número secreto!")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto,pontos))
            elif(menor):
                print("O seu chute foi menor que o número secreto!")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()