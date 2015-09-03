#数字
x=99
t = ( bin(x), x.bit_length() )
print(t)
print( (bin(256), (256).bit_length()) )
print( len(bin(256))- 2 )

#其他的内置数学工具
print("其他的内置数学工具")
import math
m=math.pi,math.e
print("math.pi,math.e",m)
print("math.sin(2*math.pi/180):",math.sin(2*math.pi/180))
print("math.sqrt(144):",math.sqrt(144),"  math.sqrt(2):",math.sqrt(2))
print("pow(2,4):",pow(2,4),"   2**4:",2**4)
print("abs(-42.0):",abs(-42.0),"  sum((1,2,3,4)):", sum((1,2,3,4)))
print("min(3,1,2,4):",min(3,1,2,4),"   max(3,1,2,4):",max(3,1,2,4))
print("math.floor(2.567):", math.floor(2.567), " math.floor(-2.567):", math.floor(-2.567))
print("math.trunc(2.567):", math.trunc(2.567), " math.trunc(-2.567):", math.trunc(-2.567))
print("int(2.567):", int(2.567), " int(-2.567):", int(-2.567))
print("round(2.567):", round(2.567), " round(2.467):", round(2.467), " round(2.567,2):", round(2.567,2))
print("'%.1f' % 2.567:", '%.1f' % 2.567, "'{0:.2f}'.format(2.567):", '{0:.2f}'.format(2.567))
print("(1/3):", 1/3, "round(1/3,2):", round(1/3,2), " ('%.2f' % (1/3)):", ('%.2f' % (1/3)))
print("math.sqrt(144):", math.sqrt(144))
print("144 ** 0.5:", 144**0.5)
print("pow(144,0.5)",pow(144,0.5))

import random
print("random.random():", random.random())
print("random.random():", random.random())
print("random.randint(1,10):", random.randint(1,10))
print("random.randint(1,10):", random.randint(1,10))

import decimal
print("decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.')-decimal.Decimal('0.3'):", decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1')-decimal.Decimal('0.3'))

print("decimal.Decimal(1)/decimal.Decimal(7):", decimal.Decimal(1)/decimal.Decimal(7))
decimal.getcontext().prec=4  #设置小数精确到4
print("decimal.Decimal(1)/decimal.Decimal(7):", decimal.Decimal(1)/decimal.Decimal(7))
print("1999+1.33:", 1999+1.33)
decimal.getcontext().prec=2
print("decimal.Decimal(str(1999+1.33)):", decimal.Decimal(str(1999+1.33)))

with decimal.localcontext() as ctx:
	ctx = 2
	print("decimal.Decimal('1.00')/decimal.Decimal('3.00')",decimal.Decimal('1.00')/decimal.Decimal('3.00')

from fractions import Fraction
x=Fraction(1,3)
y=Fraction(4,6)
print("x+y:", x+y)
print("x-y:", x-y)
print("x*y:", x*y)
print("x/y:", x/y)

print("集合")
x=set('abcde')
y=set('bdxyz')
print("x:", x)
print("y:", y)
print("'e' in x")
print("x-y:", x-y)
print("x|y:", x|y)
print("x&y:", x&y)
print("x^y:", x^y)
print("x>y,x<y:", x>y,x<y)
z= x.intersection(y)  # x&y
print("z:", z)
z.add('spam')
print("z.add('spam')", z)
z.update(set(['x','y']))
print("z.update(set['x','y']):",z)
z.remove('b')
print("z.remove('b'):", z)



input()