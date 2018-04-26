import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
plt.figure(figsize=(6,6))
#1英寸=2.54cm
x=np.linspace(0,100,1000)#deng jian ge shu zu
X=np.array([20.,40.,60.,80.,100.])#jiang yi ge lie biao zhuanhua wei shu zu
Y=np.array([4.35,7.55,10.40,13.80,16.80])

def f(p):# ding yi han shu
    k,b=p   #jie ju yu xie lv xiang tong          #对谁做拟合
    return(Y-(k*X+b))# X Y shuyu wai bu bian liang
r=leastsq(f,[1,0])# f shi ni he han shu  [1,0] shi chu shi can shu zhi
k,b=r[0]  #r0 shi ni he jie guo
print("k=",k,"b=",b)
plt.scatter(X,Y,s=100,alpha=1.0,marker='o',label=u'数据点')
y=k*x+b
ax=plt.gca()
ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
#设置坐标轴标签字体大小

plt.plot(x, y, color='r',linewidth=5, linestyle=":",markersize=20, label=u'拟合曲线')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel(u'安培/A')
plt.ylabel(u'伏特/V')

plt.xlim(0, x.max() * 1.1)
plt.ylim(0, y.max() * 1.1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')

plt.show()