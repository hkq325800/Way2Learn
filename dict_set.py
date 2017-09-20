#dict的key初始化时已固定，只减不增，key存在时可重新赋值
d = {'Michael' : 95, 'Bob' : 75, 'Tracy' : 85}
#print(d['Michael'])

#判断关键字是否在dict中
#print('hkq' in d)

#也可以通过d.get方式获取，不存在时可以返回None也可以指定default
#通过d.pop方式删除数据，但是删除后对应的key也删除了
d.pop('Bob')
#print(d.get('Bob', 0))
#print(len(d))

#set 可以看成数学意义上的无序和无重复元素的集合，因此两个set可以做数学意义上的交集并集操作
#要创建一个set，需要提供一个list作为输入集合
s1 = set([2, 3])

for a in s1:
	if a==4:
		print('true')
		s1.remove(4)
	else:
		print('false')
#重复元素在set中自动被过滤
s2 = set([1, 1, 2, 2, 3, 3, 5])
#s.remove(4)
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s2 - s1)

#print(len(s))