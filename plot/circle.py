import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots(figsize=(5, 5))
plt.subplots_adjust(left=0.25, bottom=0.25)

circle = plt.Circle(xy=(0,0), radius=1, fill=True, facecolor='#FFD0D0', edgecolor='r', lw=2)
ax.add_patch(circle)

theta_deg = 30
theta_rad = np.deg2rad(theta_deg)

verts = [[0, 0], [np.cos(theta_rad), 0], [np.cos(theta_rad), np.sin(theta_rad)]]
triangle = plt.Polygon(verts, facecolor='0.9', edgecolor='0.5', lw=2, joinstyle='round')

ax.add_patch(triangle)

incr = 0.25
plt.xticks(np.arange(-1.0, 1.0 + 0.01, incr))
plt.yticks(np.arange(-1.0, 1.0 + 0.01, incr))
plt.xlim(-1.0 - incr/2, 1.0 + incr/2)
plt.ylim(-1.0 - incr/2, 1.0 + incr/2)

plt.grid()
ax.set_aspect(1.0)

axcolor = 'lightgoldenrodyellow'
axang = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

sang = Slider(axang, 'Angle', 0, 360, valinit=theta_deg)

def update(val):
    global triangle

    theta_deg = np.around(sang.val)
    if (np.abs(theta_deg - sang.val) > 0.00001):
       # print ('{} --> {}'.format(sang.val, theta_deg))
       sang.set_val(theta_deg)
    theta_rad = np.deg2rad(theta_deg)
    verts = [[0, 0], [np.cos(theta_rad), 0], [np.cos(theta_rad), np.sin(theta_rad)]]
    triangle.remove()
    triangle = plt.Polygon(verts, facecolor='0.9', edgecolor='0.5', lw=2, joinstyle='round')
    ax.add_patch(triangle)
    fig.canvas.draw_idle()

sang.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sang.reset()

button.on_clicked(reset)

if True:
    plt.show()
else:
    plt.show(block=False)
    input()

plt.close()