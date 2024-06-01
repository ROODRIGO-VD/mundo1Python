import random


def main():
    name1 = str(input("Nome do 1° aluno: "))
    name2 = str(input("Nome do 2° aluno: "))
    name3 = str(input("Nome do 3° aluno: "))
    name4 = str(input("Nome do 4° aluno: "))
    lista = [name1, name2, name3, name4]
    random.shuffle(lista)
    print(lista)


main()