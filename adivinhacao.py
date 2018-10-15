import random


def jogar():
    print("********************")
    print("Jogo de adivinhação!")
    print("********************")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000
    total_tentativas = 0

    print("Numero secreto {}".format(numero_secreto))
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        print("Pontos: {}".format(pontos))
        chute = int(input("Digite o seu número entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if (acertou):
            print("Você acetou, parabéns você fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("O numero secreto é menor")
            else:
                print("O numero secreto é maior")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("********************")
    print("****Fim do jogo*****")
    print("********************")


if (__name__ == "__main__"):
    jogar()
