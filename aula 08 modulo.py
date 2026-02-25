import math
num = int(input("Digite um numero: "))
raiz = math.sqrt(num)
print('a raiz de {} é igual a {:.2f}'.format(num, raiz))
print('a raiz de {} é igual a {:.2f}'.format(num, math.ceil(raiz)))
print('a raiz de {} é igual a {:.2f}'.format(num, math.floor(raiz)))
