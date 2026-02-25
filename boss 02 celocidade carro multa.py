import random
velo = random.randint(50,100)
print('a velocidade do carro foi de {}'.format (velo))
if velo > 80:
    print('voce ultrapassou a velocidade maxima de 80km/h')
    print('MULTADO')
    multa = (velo - 80) * 7
    print('a multa sera de R$ {:.2f}'.format(multa))
print('voce é um bom motorista')