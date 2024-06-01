import random

adivinhe = int(input("Escolha um número de 0 a 5: "))
numero = random.randint(0, 5)

if adivinhe < 0 or adivinhe > 5:
    print("Número fora do intervalo estabelecido, escolha um entre 0 e 5 !")
elif adivinhe == numero:
    print(f"Parabéns, você acertou !!")
else:
    print(f"Você errou, o número escolhido pela máquina foi o {numero}, tente novamente!")
