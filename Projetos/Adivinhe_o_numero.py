import random

print("Jogo do Adivinhe o numero, digite números de 1 a 10"
      " até acertar o numero aleatório")
loop1 = True

while loop1:
    rnumero = random.choice(range(1, 11)) # 'rnumero' é um número randômico
    jogar = input("Quer jogar? S/N?:")
    loop = True
    if jogar == 'S' or jogar == 's':
        while loop:
            numero = int(input("Adivinhe o número de 1 a 10:"))
            if numero > 10 or numero < 1:
                print("Somente números de 1 a 10, por favor!")
            elif numero > rnumero:
                print("Menor!")
            elif numero < rnumero:
                print("Maior!")
            else:
                print("Você ganhou!")
                loop = False
    else:
        print("Ok, até logo!")
        loop1 = False