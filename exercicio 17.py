from math import hypot
co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente'))
#hi = (ca ** 2 + co ** 2) ** (1/2)
#print(' a hipotenusa é {:.2f}'.format(hi))
print(' a hipotenusa é {}'.format(hypot(co, ca)))



