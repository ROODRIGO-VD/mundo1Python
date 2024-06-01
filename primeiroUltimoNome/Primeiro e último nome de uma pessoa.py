nome = input("Digite seu Nome Completo: ").strip()
split = nome.split()

print(f"Seu primeiro nome é {split[0]}\n Seu ultimo nome é {split[len(split)-1]}")