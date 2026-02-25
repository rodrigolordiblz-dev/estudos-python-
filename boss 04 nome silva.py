nome = str(input('qual é o seu nome completo?')).strip().upper()
#print ('seu nome tem Silva?', 'SILVA' in nome)
print('seu nome tem silva? {}'.format('silva' in nome.lower()))