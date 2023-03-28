import math
cto = float(input('Digite o valor do cateto oposto: '))
ctad = float(input('Digite o valor do cateto adjacente: '))
hptn = math.pow(cto, 2) + math.pow(ctad, 2)
print(f'O valor da hipotenusa é {math.sqrt(hptn)}')
