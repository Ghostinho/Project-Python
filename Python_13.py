rs = float(input('Qual o salario de Fúncionario? R$'))
aumento = float(input('Qual a porcentagem de aumento: %'))
v = rs + (rs * aumento / 100)
print(f'Um fucionario ganhava {rs}R$ com um aumento de {aumento}% ele ganha agora \n{v:.2f}R$')
