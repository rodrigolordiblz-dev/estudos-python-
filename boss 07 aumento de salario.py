salario = float(input('Qual o seu salário? '))

if salario >= 1250:
    novo_salario = salario + (salario * 10 / 100)
    print('Você recebeu um aumento de 10%.')
else:
    novo_salario = salario + (salario * 15 / 100)
    print('Você recebeu um aumento de 15%.')

print('Com o aumento, seu salário passa a ser R$ {:.2f}'.format(novo_salario))


'''programa guanabara 

salário = float(input( 'qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print( 'quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.' .format(salário, novo))'''
