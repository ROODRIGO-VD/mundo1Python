#Analise de dados

#frase.find() - Mostra a posição do que voce procura

#len(frase) - Mostra o comprimento da frase


frase = str("Me chamo Rodrigo Vidal e Albuquerque Cruz")
len(frase)
print(f"Na frase '{frase}', há {len(frase)} letras.  ")

#frase.count("Colocar a letra ou número para ele contar na frase") - Conta quantas letras ou números especificos há em uma frase.

print(f"Na frase '{frase}', há {frase.count('o')} letras 'O' ")

# Existe a palavra "Rodrigo" dentro da frase|  = if "Rodrigo" in frase:   | ou print("Rodrigo" in frase) - retorna True ou False

if "Rodrigo" in frase:
    print("Sim")
else:
    print("Não")

#Transformação de dados

#frase.replace("x","y") - Substitui o X por Y

a = frase.replace("Rodrigo", "Xereca")
print(a)

#frase.upper() - Deixa em maiusculo

b = frase.upper()
print(b)

#frase.lower() - Deixa em minusculo

c = frase.lower()
print(c)

#frase.capitalize() - Joga todos caracteres para MINUSCULO e deixa apenas o primeiro em MAIUSCULO

d = frase.capitalize()
print(d)

#frase.tittle() - Transforma cada letra após o ESPAÇO em MAIUSCULA, incluindo a PRIMEIRA LETRA

e = frase.title()
print(e)

#frase.strip() - Remove todos os espaços inuteis, tanto no inicio quanto no final da frase
#frase.rstrip() - Remove todos os espaços inuteis da direita
#frase.lstrip() - Remove todos os espaços inuteis da esquerda

#"-".join(variavel)

frase2 = ("Rodrigovidalalbuquerquecruz")
f = " ".join(frase2)
print(f)
