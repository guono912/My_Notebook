'''
math模块简介
因为我们肯定会经常和它打交道，嗯
本节车速较快（毕竟函数什么名字都知道（打了多少年交到了废话
请站稳扶好
首先当然是
'''
import math

# 1 数字操作（混几个不在math里的）
a = math.ceil(4.3) #向上取整，本例返回5
b = math.floor(4.8)  #向下取整，本例返回4
c = round(4.8)  #四舍五入，返回5
d, e = math.modf(4.3) #返回整数和小数部分，e = 4.0, d = 0.299999999999
abs(-3)   #>>>3，绝对值，适用于integer，float，complex（取模长）
math.trunc(4.33)  #其实和floor没区别了
math.fabs(-3.3) #>>>3.3,同上，仅适用于integer和float，但仍然建议处理float使用这个
math.copysign(a,b) #使a与b同号（a随着b）

# 2 e相关（返回值为float
math.e  #>>>2.718.....（背不下来了）
math.e == math.exp(1)  #>>>True  返回e^x的值
math.expm1(0) == 0     #>>>True  返回e^x-1的值

# 3 对数相关（返回值均为float
math.log(8)  #返回ln8
math.log(8,2)  #返回(ln8/ln2)(本质)（由换底公式逆用可知返回值等于以2为底8的对数
math.log10(100) #以10为底
math.log2(8)  #以2为底
math.log1p(0)  #返回ln(1+x)

# 4 三角函数相关
f = math.pi  #3.141592653589793 
math.sin(f)  #sinx,弧度
math.cos(f)
math.tan(f)
math.asin(1)  #arcsin,返回弧度，下同
math.acos(1)
math.atan(1)
math.hypot(3,4)  #返回5
math.degrees(math.pi)   #弧度转角度（float
math.radians(180)   #上一行逆运算
math.sinh(0)   #sh x
math.cosh(0)   #ch x
math.tanh(0)   #th x
math.asinh(f)  #反双曲函数
math.acosh(f)
math.atanh(f)

# 5 其他
math.gcd(36,15)  #最大公约数
math.sqrt(9)  #根号9
math.fmod(9,2)   #同float(9 % 2)
math.factorial(4)  #4!
