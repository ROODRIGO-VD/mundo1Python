import math

def main():
    ang = float(input("Digite o ângulo que você deseja: "))
    sen = math.sin(math.radians(ang))
    cos = math.cos(math.radians(ang))
    tan = math.tan(math.radians(ang))
    print(f"O ângulo de {ang} tem o SENO de {sen:.2f}\n O ângulo de {ang} tem o COSSENO de {cos:.2f}\n O ângulo de {ang} tem a TANGENTE de {tan:.2f}")


main()