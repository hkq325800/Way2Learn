def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

#有多个有默认参数的参数时赋值要带上'参数=xxx'
enroll('Bob', 'M', city='Tianjin')

def add_end(L):
	L=[]
    L.append('END')
    return L

add_end()
add_end()
print(add_end())

