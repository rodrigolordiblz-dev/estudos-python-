num1 = int(input('Digite um número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

'''if num1 > num2 and num1 > num3:
    print('O número {} é o maior.'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O número {} é o maior.'.format(num2))
elif num3 > num1 and num3 > num2:
    print('O número {} é o maior.'.format(num3))
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
print('O maior número é {} e o menor número é {}.'.format(maior, menor))'''
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior= num3
print('o maior numero é o {} e o menor numero é o {}.'.format(maior, menor))
