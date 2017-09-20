def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

#有多个有默认参数的参数时赋值要带上'参数=xxx'
enroll('Bob', 'M', city='Tianjin')
#默认参数必须指向不变对象
def add_end(L=[]):
	L.append('END')
	return L

add_end()
add_end()
print(add_end())

def add_end_new(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

add_end_new()
add_end_new()
print(add_end_new())

#可变参数 可传入0个或任意个参数
#原函数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#1*1+2*2+3*3
print(calc([1,2,3]))

#新函数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3))

#关键字参数允许你传入0个或任意个含参数名的参数，
#这些关键字参数在函数内部自动组装为一个dict
#用来解决必填项和可选项
def person(name, age, **other):
    print('name:', name, 'age:', age, 'other:', other)
person('Michael', 30, )
person('Bob', 24, gender="M", job='engineer') 
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 28, **extra)   