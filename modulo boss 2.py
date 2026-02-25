import math

num = float(input('comprimento do cateto oposto: '))
num2 = float(input('comprimento do cateto adjacente: '))
resultado = (num**2 + num2**2) **(1/2)
print('o comprimento do cateto oposto é {}, e do cateto adjacente é {} e o comprimento da hipotenusa é {:.2f}'.format (num, num2, resultado))

#ou pode ser tambem assim:
#import math
#num = float(input('comprimento do cateto oposto: '))
#num2 = float(input('comprimento do cateto adjacente: '))
#hipotenusa = math.hypot(num,num2)
#('o comprimento do cateto oposto é {}, e do cateto adjacente é {} e o comprimento da hipotenusa é {:.2f}'.format (num, num2, hipotenusa))

