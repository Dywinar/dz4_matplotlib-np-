import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
def f(x):
  return x**(1/2)/(x-5)
X = np.linspace(1,10,300)
Y = f(X)
plt.plot(X,Y, color='green', dashes=[2,1], alpha=0.5, label='Вот такая моя функция')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Функция')
plt.grid()
plt.show()
