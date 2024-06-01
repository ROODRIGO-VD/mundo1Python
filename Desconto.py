produto = float(input("Qual é o preço do produto? R$"))

desconto = produto * 0.05
total = produto - desconto

print(f"O preço original do produto era R${produto:.2f}, na promoção com desconto de 5% o produto custará R${total:.2f}")