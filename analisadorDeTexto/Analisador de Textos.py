from time import sleep

nome = input("Digite seu nome completo: ")
print("Analisando seu nome...")
sleep(1)

def main():
    maiusculo = nome.upper()
    minusculo = nome.lower()
    letras = len(nome.replace(' ', ''))
    first = nome.find(' ')
    separa = nome.split()
    print(f"Seu nome em maiúsculas é {maiusculo}\n Seu nome em minúsculas é {minusculo}\n Seu nome ao todo possui {letras}\n"
          f" Seu primeiro é {separa[0]} e ele possuí {first} letras ")


main()