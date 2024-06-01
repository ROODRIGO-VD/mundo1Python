def main():
    dias = int(input("Por quantos dias você alugou o veículo? "))
    km = float(input("Quantos KM você percorreu com o veículo? "))
    total = (km * 0.15) + (dias * 60)
    print(f"Você rodou por {km}Km e alugou o veículo por {dias} dias, logo pagará no total R${total:.2f}.")
main()