import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.math.pi,np.math.pi, 50)
y = np.sin(x)
plt.stem(x, y)
plt.show()
