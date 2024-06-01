distancia = float(input("Qual a distância da sua viagem: "))

if distancia <= 200:
    calcu = distancia * 0.50
    print(f"Você percorreu {distancia}Km, portanto pagará na passagem {calcu:.2f}R$ ")
else:
    calcu = distancia * 0.45
    print(f"Você percorreu {distancia}Km, portando pagará na passagem {calcu:.2f}R$")