#dict,list之类的其他内容
#list
a = ['a','b','d','d','d']
a.append('e')
print(a)
a.insert(2,'c')
print(a)
b = a.pop(4)
print(a)
print(b)
del a[3]
print(a)
a.append('e')
a.remove('e')
print(a)

#dict