import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5*np.pi, 1000)
x = t * np.cos(t)
y = t * np.sin(t)

plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Параметрическая кривая')
plt.show()