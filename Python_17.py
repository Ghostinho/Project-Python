import random
n1 = str(input('Digite o um nome: '))
n2 = str(input('Digite segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
x = random.sample(lista,k=len(lista))
print(f'Os alunos escolhido para apresentar a sala {x}')
