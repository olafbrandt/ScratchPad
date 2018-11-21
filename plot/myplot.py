import matplotlib.pyplot as plt
import numpy as np
import time

x = np.arange(0.0, 360.0, 0.1)

y1 = np.sin(x * (2.0 * np.pi / 360.0))
y2 = np.cos(x * (2.0 * np.pi / 360.0))
if True:
    y3 = np.tan(x * (2.0 * np.pi / 360.0))
    y3[900] = np.nan
    y3[2700] = np.nan

#plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

fig, ax = plt.subplots(figsize=(12, 10))

line_width = 3
ax.plot(x, y1, label="sine", lw=line_width)
ax.plot(x, y2, label="cosine", lw=line_width)
ax.plot(x, y3, label="tangent", color="red", lw=line_width)

plt.xlabel('degrees')
plt.xticks(np.arange(0, 361, 45))

plt.ylim((-3,3))

plt.title('Trigonometry')

plt.grid()
plt.legend()

if False:
    plt.show()
else:
    plt.show(block=False)
    input()

plt.close()