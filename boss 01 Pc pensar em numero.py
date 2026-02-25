from random import randint
from time import sleep
num = randint(0,5)
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5 tente advinhar...')
print('-=-' * 20)
num2= int(input('em qual numero eu pensei?'))
print('PROCESSANDO... ')
sleep(2)
if num2 == num:
    print('voce acertou')
else:
    print('GANHEI! eu pensei no numero  {} e não no numero {}'.format(num, num2))
