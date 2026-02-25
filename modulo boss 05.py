import random

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)  # Embaralha a lista
print('A ordem de apresentação será')
print(lista)
