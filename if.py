age = 3
print('your age is', age)
#它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
if age >= 18:#if不需要加括号
    print('adult')
    #可以继续，不需要加大括号 print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
