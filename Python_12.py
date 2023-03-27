preço = float(input('Qual o preço do produto? R$ '))
d = float(input('Digite o valor do desconto: '))
total = preço - (preço * d / 100)
print(f'O produto que custa, {preço} no desconto de {d:.0f} custa: R${total:.2f}')
