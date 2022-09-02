from turtle import color, width
import matplotlib
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

### Monitor Stats
mon1_dem = (16, 9)
mon1_pos = (0, 0)

mon2_dem = (16, 9)
mon2_pos = (mon1_pos[0] + mon1_dem[0], mon1_pos[1])


### Set Up
fig, ax = plt.subplots()
patches = []

for i in range(360):
    plt.cla()

    ax.add_patch(Rectangle(mon1_pos, mon1_dem[0], mon1_dem[1], color="y", angle=i))
    ax.add_patch(Rectangle(mon2_pos, mon2_dem[0], mon2_dem[1], color="b", angle=-i))

    ### Plot
    plt.xlim(-3, 35)
    plt.ylim(-12, 21)

    plt.axis("off")
    plt.pause(0.001)

plt.show()