import math
num = float(input('digite o valor do ângulo: '))
seno = math.sin(math.radians(num))
coseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))
print('o valor do seno {:.2f}'.format(seno))
print('o valor do coseno {:.2f}'.format(coseno))
print('o valor do tangente {:.2f}'.format(tangente))
