#lesson1（更新于4/5）
#标准开局，print的基本用法一例
print('hellow world')

#e.g.输入两个整数，并求和输出
a = int(input('a='))
b = int(input('b='))
sum = a+b
print('a+b=',sum)
#
print('%d + %d = %d'%(a,b,a+b))
#print的其他用法？"%d"是啥玩意？
#input的用法？为什么要加int()？不加会怎么样？

#e.g 求圆的面积
pi=3.1415926
r = int(input('r='))
s = pi*r*r
print('S=',s)
print(type(s))
#type的用处？float是什么鬼？有其他和"float"一类的名词嘛？

#e.g 1+2+....+100=？
a=0
for i in range(1,101):
    a = a + i
print('a=',a)
#"for xxx in range"是什么？此例应学会这一基本用法(其他for的方法再说= =)
#为什么要到101？为什么之后一行前有空格？
#以下是进阶练习
#1-2+3-4......+99-100=?
a = 0
for i in range(1,51):
    a = a+2*i-1
    a = a-2*i
print('a=',a)
#for循环是非常重要的东西~~~
#e.g 还是5050，换一种结构如何？
sum = 0
i = 1
while i<=100:
    sum = sum+i
    i+=1
print('sum=',sum)
#此例应学会"当"结构的基本用法，以及i+=1代表什么？

#e.g 输入一段字符串，以"#"结束，并统计"a"或"A"c出现的概率
#完全可以不用#，降低点难度
i=0
n=0
st = input('str is ')
while st[i]!='#':
    if (st[i]=='a') or (st[i]=='A'):
        n+=1
    i=i+1
print('P=',(100*n)/i,'%')
#逻辑运算与或非怎么写？字符串相关？
#不过，以上是一般做法，而我们可以用Python特色遍历字符串的方法解决(不以#结尾)
n = 0
for i in st:
    if (i=='a') or (i=='A'):
        n+=1
print('P=',(100*n)/len(st),'%')

#
