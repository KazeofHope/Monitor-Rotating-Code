from turtle import color, width
import matplotlib
from matplotlib import animation
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

import numpy as np

### Monitor Stats
mon1_dem = (16, 9)
mon1_pos = (0, 0)

mon2_dem = (16, 9)
mon2_pos = (mon1_pos[0] + mon1_dem[0], mon1_pos[1])

rot_around1 = (0 - mon1_dem[0]/2, 0)
rot_around2 = (0 + mon2_dem[0], 0)

# Center = [-8, 0]
point_of_rotation1 = np.array([0 - mon1_dem[0], 0 -mon1_dem[1]/2])
# Center = [8, 0]
point_of_rotation2 = np.array([mon2_dem[0]/2 - mon1_dem[0], mon2_dem[1]/2])


color1 = "#02a9f7"
color2 = "#89d6fb"

### Set Up
fig, ax = plt.subplots()
patches = []

rot = 361

for deg in range(0, rot):
    plt.cla()

    rec1 = Rectangle(point_of_rotation1, mon1_dem[0], mon1_dem[1], color="y", transform=Affine2D().rotate_deg_around(*(rot_around1[0], rot_around1[1]), deg)+ax.transData)
    rec2 = Rectangle(-point_of_rotation2, mon2_dem[0], mon2_dem[1], color="b", transform=Affine2D().rotate_deg_around(*(rot_around2[0],rot_around2[1]), deg)+ax.transData)

    ax.add_patch(rec1)
    ax.add_patch(rec2)

    plt.plot([rot_around1[0]], [rot_around1[1]], marker="o")
    plt.plot([rot_around2[0]], [rot_around2[1]], marker="o")

    ### Plot
    # plt.xlim(-3, 35)
    # plt.ylim(-12, 21)

    plt.axis("scaled")
    # plt.axis("off")
    plt.pause(0.0001)

plt.show()
plt.close()