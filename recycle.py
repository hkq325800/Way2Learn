names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum=0
arr=[1,2,3,4,5,6,7,8,9,10]
for x in arr:
    sum+=x
print(sum)

sum=0
for x in range(101):
    sum += x
print(sum)

sum=0
n=0
while n<101:
    sum+=n
    n+=1
print(sum)

# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']

#while
n=0
while n<3:
    print('Hello, %s' % L[n])
    n += 1

#for
for str in L:
    print('Hello, %s' % str)
