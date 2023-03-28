from random import choice
n1 = str(input('Digite o primerio nome: '))
n2 = str(input('Digte segundo nome: '))
n3 = str(input('Digite o terceiro: '))
lista = [n1, n2, n3]
x = choice(lista)
print(f'O aluno sorteado foi {x}')
