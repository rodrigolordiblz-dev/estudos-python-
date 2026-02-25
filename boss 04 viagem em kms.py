km = int(input('qu7antos kms voce vai viajar'))
'''if km <= 200:
    viagem = km * 0.50
else:
    viagem = km * 0.45
print('o valor da passagem sera de R$ {}'.format(viagem))'''
preço = km * 0.50 if km <= 200 else km *0.45
print('o valor da passagem sera de R$ {}'.format(preço))