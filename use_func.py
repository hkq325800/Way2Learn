#Built-in Functions https://docs.python.org/3/library/functions.html
#abs()	dict()	help()	min()	setattr()
#all()	dir()	hex()	next()	slice()
#any()	divmod()	id()	object()	sorted()
#ascii()	enumerate()	input()	oct()	staticmethod()
#bin()	eval()	int()	open()	str()
#bool()	exec()	isinstance()	ord()	sum()
#bytearray()	filter()	issubclass()	pow()	super()
#bytes()	float()	iter()	print()	tuple()
#callable()	format()	len()	property()	type()
#chr()	frozenset()	list()	range()	vars()
#classmethod()	getattr()	locals()	repr()	zip()
#compile()	globals()	map()	reversed()	__import__()
#complex()	hasattr()	max()	round()	 
#delattr()	hash()	memoryview()	set()	 

#数据类型转换
int('123')
str(123)
float('12.34')
bool(1)
bool('')

# -*- coding: utf-8 -*-

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
#函数必须def在调用之前
print(my_abs(-2))

def my(x):
	if x>0:
		x = -5
	else:
		x = 5
	print(x)
#y的值不改变 说明函数内不影响函数外
y=66
my(y)
print(y)

#设置了默认参数n=2
#必选参数在前，默认参数在后
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s