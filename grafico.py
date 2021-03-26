import matplotlib.pyplot as plt

x = range(-10, 11)
y = []
for n in x:
    y.append(n** 2 + 4)

plt.grid()
plt.plot(x, y, linewidth = 2.0)
plt.show()