frase = input("Digite uma frase: ").strip().upper()

contagem = frase.count("A")
primeira = frase.find("A")+1
ultima = frase.rfind("A")+1

print(f" A letra 'A' aparece {contagem}\n A primeira letra 'A' aparece na posição {primeira}\n A ultima letra 'A'"
      f"aparece na posição {ultima}")

