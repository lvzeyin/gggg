# import numpy as np
# from scipy import interpolate
# import pylab as pl
# x = np.linspace(0, 10, 11)
# y = np.sin(x)
# xnew = np.linspace(0, 10, 101)
# pl.plot(x,y,'ro')
# for kind in ['nearest', 'zero', 'slinear', 'quadratic']:
# 	f = interpolate.interp1d(x,y,kind=kind)
# 	ynew = f(xnew)
# 	pl.plot(xnew, ynew, label=str(kind))
#
# pl.legend(loc='lower right')
# pl.show()

import numpy as np
import pylab as pl
from scipy import interpolate

x = np.linspace(0, 2*np.pi+np.pi/4, 10)
y = np.sin(x)

x_new = np.linspace(0, 2*np.pi+np.pi/4, 100)
f_linear = interpolate.interp1d(x, y)
tck = interpolate.splrep(x, y)
y_bspline = interpolate.splev(x_new, tck)

pl.plot(x, y, "o", label="原始数据")
pl.plot(x_new, f_linear(x_new), label="线性插值")
pl.plot(x_new, y_bspline, label="B-spline插值")
pl.legend()
pl.show()

