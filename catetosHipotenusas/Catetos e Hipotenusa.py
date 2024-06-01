import math as m

# COM MÓDULO
def main():
    a = int(input("Digite o comprimento do cateto oposto em CM: "))
    b = int(input("Digite o comprimento do cateto adjacente em CM: "))
    hipot = m.hypot(a, b)
    print(f"A hipotenusa vai medir {hipot}cm ")

#SEM MÓDULO
def main2():
    a = float(input("Digite o comprimento do cateto oposto em CM: "))
    b = float(input("Digite o comprimento do cateto adjacente em CM: "))
    hip = (a ** 2 + b ** 2) ** (1/2)
    print(f"A hipotenusa vai medir {hip}cm ")


main() or main2()


#pedir comprimento cateto oposto
#pedir comprimento cateto adjacente
#retornar hipotenusa
