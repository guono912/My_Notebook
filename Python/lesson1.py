#hellow world(#表示注释，类似于//)
print('hellow world')
#>>>hellow world
'''
多行注释为三个引号，类似于Pascal的‘{}’
另外python每句结尾不需要分号，相对的，对缩进的标准有病态般的追求2333\
'''
############################################
a='world'
print('hellow ',a)
#>>>hellow world
#可见python中print的用法和Pascal的write类似，不过有Pascal没有的\n之类的操作
print('hellow\nworld')
'''
hellow
world
'''
#实现上面的还可以
print('''hellow
         world''')
#并且可以把函数直接放到print中（Pascal没试过）
print('1+1=',1+1)
############################################
#作用和read一样然而差远了的input
input()  #=>>readln
#xxx(被赋值)=input('提示语')
name = input('your name is?/n')
#默认输入为字符串
a = input('a=')
#>>>3
type(a)
#<type 'str'>
a = int(input('a='))  #此时输入为整形，类似的操作有float等
