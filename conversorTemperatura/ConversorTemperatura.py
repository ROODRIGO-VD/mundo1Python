from time import sleep

def tc_tk():
    a = float(input("Digite sua temperatura em °C: "))
    form = a + 273
    print(f"A temperatura de {a}°C, corresponde a {form}°K !")


def tc_tf():
    a = float(input("Digite sua temperatura em °C: "))
    form = (a * 9 / 5) + 32
    print(f"A temperatura de {a}°C, corresponde a {form}°F !")


def main():
    while True:
        print("=" * 20)
        print("Conversor de Temperatura")
        print("=" * 20)
        print("Opções: ")
        print("[1] - Celsius para Kelvin")
        print("[2] - Celsius para Fahrenheit")
        print("[3] - Encerrar o Programa")
        opcao = int(input("Digite sua Opção: "))
        if opcao == 1:
            tc_tk()
            sleep(2)
        elif opcao == 2:
            tc_tf()
            sleep(2)
        elif opcao == 3:
            print("Fim do programa, volte sempre !!")
            break
        else:
            print("Opção Inválida, tente outra vez !!")
            sleep(2)
            main()
main()





