num = int(input("Digite um número: "))
n = str(num)

if len(n) == 1:
        print(f"Unidade = {n[0]}")
elif len(n) == 2:
        print(f"Unidade: {n[1]}\nDezena: {n[0]}")
elif len(n) == 3:
        print(f"Unidade: {n[2]}\nDezena: {n[1]}\nCentena: {n[0]}")
elif len(n) == 4:
        print(f"Unidade: {n[3]}\nDezena: {n[2]}\nCentena: {n[1]}\nMilhar: {n[0]} ")
else:
        print("Valor fora de 0 a 9999")
