import numpy as np
import matplotlib.pyplot as plt

mean = 0
std_dev = 3


x = np.linspace(-10, 10, 400)  


pdf = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

plt.figure(figsize=(8, 6))
plt.plot(x, pdf, label=f'Mean={mean}, Std Dev={std_dev}')
plt.title('Gaussian Distribution')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()


plt.savefig('gaussian.png')

plt.show()



