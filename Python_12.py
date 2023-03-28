preço = float(input('Qual o preço do produto? R$ '))
produto = float(input('Digite o valor do desconto: '))
total = preço - (preço * produto / 100)
print(f'O produto que custa, {preço} no desconto de {produto:.0f} custa: R${total:.2f}')
