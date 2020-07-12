def jogar():
    print("********************************")
    print("Bem vindo ao jofo de adivinhção!")
    print("********************************")

<<<<<<< HEAD
    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
=======
    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)
>>>>>>> 3d577246b6cf313925d70dfbc8dfe1d395e97721

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
<<<<<<< HEAD
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)


=======
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
>>>>>>> 3d577246b6cf313925d70dfbc8dfe1d395e97721
    print("Fim de jogo")


if (__name__ == "__main__"):
    jogar()
