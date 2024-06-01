velocidade = int(input("Qual era sua velocidade: "))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f"Você estava a {velocidade}Km/h, numa via de 80 Km/h, e foi multado em {multa}R$")
else:
    print(f"Você está dentro do limite da via")