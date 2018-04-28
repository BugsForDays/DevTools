from math import pi, radians, degrees
from fractions import Fraction
from sys import stdin

if stdin.readline().strip() == 'deg-rad':
    lines = stdin.readlines()
    print('converting from deg to rad: ')
    for deg in lines:
        deg = deg.strip()
        deg = int(deg)
        conversion = Fraction(radians(deg)/pi).limit_denominator(10000000)
        print(str(deg) + ' ----> ' + str(conversion.numerator) + 'π/' + str(conversion.denominator))
else:
    lines = stdin.readlines()
    print('converting from rad to deg: ')
    for rad in lines:
        rad = rad.strip()
        conversion = rad.replace('pi', str(pi))
        print(str(rad) + ' ----> ' + str(degrees(eval(conversion))))
