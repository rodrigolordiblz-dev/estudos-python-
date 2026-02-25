import random
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)
print('O aluno sorteado foi: {}'.format(sorteado))
