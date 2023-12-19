import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
data = np.random.normal(16, 2, 1000)
plt.hist(data, color='r', alpha=0.5)
plt.show()
#По большей мере исходя из событий, 250+ человек всегда по большей части пробегают за +-16, а за 22,8-12 секунды пробегают от 0 до 50
