#str是不变对象，而list是可变对象
a = 'abc'
print(a)
a = 'Abc'
print(a)
print(a.replace('b', 'B'))
print(a)
#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
#相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
b = [1,2,3]
c = {4, 5, 6}
print(max(-1,0,1))
print(max(b))
print(max(c))