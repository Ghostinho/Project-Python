nc = str(input('Digite o seu nome completo: ')).strip()
print(f'Letras Maiusculas {nc.upper()}')
print(f'Letras Minusculas {nc.lower()}')
print(f'Letras Capitalizadas {nc.capitalize()}')
print(f'Letras Tituladas {nc.title()}')
print(f'Quantidade de letras {len(nc) - nc.count(" ")}')
sp = nc.split()
print(f'Quantidade de letras do primeiro nome {len(sp[0])}')
