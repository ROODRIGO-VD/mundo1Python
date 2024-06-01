salario = float(input("Digite seu salário: R$"))

if salario <= 1250:
    aumento = salario * 1.15
else:
    aumento = salario * 1.1
print(f"Seu antigo salário era R${salario:.2f}, com o aumento foi para R${aumento:.2f}")