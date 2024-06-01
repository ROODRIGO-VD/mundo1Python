print(("=-"*15), "Analisador de Triângulos", ("=-"*15))
a = float(input("1° Segmento: "))
b = float(input("2° Segmento: "))
c = float(input("3° Segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos podem formar um triângulo!")
    if a == b and a == c and b == a and b == c and c == a and c == b:
        print("Esse triângulo é EQUILÁTERO")
    elif
else:
    print("Os segmentos não podem formar um triângulo!")
