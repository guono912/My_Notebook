import matplotlib.pyplot as plt
from sklearn import svm, datasets, metrics
from sklearn.model_selection import train_test_split
import numpy as np

#load data
data_digits = datasets.load_digits()
x = data_digits.images
y = data_digits.target
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)
train_x1 = train_x.reshape(len(train_x), -1) #源数据为2维numpy数组，需进行降维处理
test_x1 = test_x.reshape(len(test_y), -1) 

'''
scour=[]
xxx=[]
# 交叉验证gamma参数最优值（跑了快1分钟。。。决定是0.001比较好
i = 0.00001
while i<=0.005:
    xxx.append(i)
    svmm=svm.SVC(gamma=i)
    svmm.fit(train_x1, train_y)
    scour.append(svmm.score(test_x1,test_y))
    i += 0.0001
scour=np.array(scour)
xxx=np.array(xxx)
plt.plot(xxx, scour)
plt.show()
'''

#training
classifier = svm.SVC(gamma=0.001)
classifier.fit(train_x1, train_y)

#看下结果，并打印测试集前12个的预测值真实值对比
predictions = classifier.predict(test_x1)
for i in range(0,12):
    plt.subplot(3, 4, i + 1)
    plt.axis('off')
    plt.imshow(test_x[i], cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('pre:%d tar:%d' % (predictions[i],test_y[i]))
plt.show()

# 一开始觉得这种案例原理会比较复杂
# 后来写下来发现本质上仍然只是一个分类问题
# 尤其是降维那一步，简直暴露本质
# 只是参数变成了64个像素点。。。。。
# 不过毕竟我还只是一个只会调包调参的渣渣。
# 具体还是以后真正掌握这个算法再说
# 凑个50行~