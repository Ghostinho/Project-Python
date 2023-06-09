import math
ct1 = float(input('Digite o valor do cateto oposto: '))
ct2 = float(input('Digite o valor do cateto adejacente: '))
hptn = math.hypot(ct1, ct2)
print(f'A medida de {ct1} somada com {ct2} equivale há {hptn}')
