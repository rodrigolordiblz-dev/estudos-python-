frase = input('digite uma frase: ').strip().upper()
print ('a letra A aparece {} na frase'.format (frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))



