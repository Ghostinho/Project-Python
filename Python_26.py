frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Quantas vezes aparece a letra "A": {frase.count("A")}')
print(f'Qual a primeira posiçao da letra "A": {frase.find("A")+1}')
print(f'Qual a ultima posiçao da letra "A": {frase.rfind("A")+1}')
