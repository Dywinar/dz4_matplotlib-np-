import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
X = np.random.normal(0, 1, 3000)
Y = np.random.normal(3, 4, 3000)
plt.scatter(X,Y,c='red', s=50, alpha=0.5, label='Заданные точки', marker='+')
# я правильно понял что в домашке ошибка и вместо maker надо было marker
plt.legend()
plt.grid()
plt.xlabel('X')
plt.ylabel("Y")
plt.show()
