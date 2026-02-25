a1 = float(input('Digite a reta de um triângulo: '))
a2 = float(input('Digite outra reta de um triângulo: '))
a3 = float(input('Digite mais uma reta de um triângulo: '))

if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
    print('Forma um triângulo!')

    if a1 == a2 == a3:
        print('Este é um triângulo equilátero.')
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print('Este é um triângulo isósceles.')
    else:
        print('Este é um triângulo escaleno.')
else:
    print('Não forma um triângulo.')
9