import math
from pickle import FALSE, TRUE
from tkinter.dialog import DIALOG_ICON
import matplotlib
from matplotlib import animation
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
import numpy as np

### Monitor 
mon1_dem = (16, 9)
mon2_dem = (16, 9)

## The values we need from the triangle within the rectangles
diag_dia1 = math.sqrt(mon1_dem[0]**2 + mon1_dem[1]**2)
diag_dia2 = math.sqrt(mon2_dem[0]**2 + mon2_dem[1]**2)

# [hori_rad, diag_rad, vert_rad]
rad_array1 = [mon1_dem[0] / 2, diag_dia1 / 2, mon1_dem[1] / 2]
rad_array2 = [mon2_dem[0] / 2, diag_dia2 / 2, mon2_dem[1] / 2]

# angle_arr1 = [arcsin(9 / 18.35755), arccos(16 / 18.35755)]
angle_arr1 = [
    math.degrees(math.asin((mon1_dem[1]) / (diag_dia1))),
    math.degrees(math.asin((mon1_dem[0]) / (diag_dia1)))
    ]
angle_arr2 = [
    math.degrees(math.asin((mon2_dem[0]) / (diag_dia1))),
    math.degrees(math.asin((mon2_dem[1]) / (diag_dia2)))
    ]

# Check to Equal 90 : ~29 + ~61
# print(f"Angle[0]: {angle_arr1[0]}")
# print(f"Angle[1]: {angle_arr1[1]}")

# print(f"Sum of Angle Array1: {sum(angle_arr1)}")
# print(f"Sum of Angle Array2: {sum(angle_arr2)}")

### Plot Set Up
fig, ax = plt.subplots()

# Aesthetic
color1 = "#02a9f7"
color2 = "#89d6fb"

### Rotation Set Up
deg = 91

offset1 = 0
offset2 = 0

increment1 = 0
increment2 = 0

mon1_clkwise = FALSE
mon1_clkwise = TRUE

for i in range(0, deg):
    # Clear for Animation
    plt.cla()

    if (i <= angle_arr1[0]):
        increment1 = (diag_dia1 - mon1_dem[0]) / angle_arr1[0]
    elif (i > angle_arr1[0]):
        increment1 = ((mon1_dem[1] - diag_dia1) / angle_arr1[1])

    offset1 = offset1 + increment1

    if (i <= angle_arr2[0]):
        increment2 = (diag_dia2 - mon2_dem[0]) / angle_arr2[0]
    elif (i < angle_arr2[0]):
        increment2 = ((mon2_dem[1] - diag_dia2) / angle_arr2[1])

    offset2 = offset2 + increment2

    ## Add Increments to the Bottom Left
    # Start: Center = [-8, 0], Bottom Left = [-16, -4.5]
    point_of_rotation1 = np.array([0 - offset1 - mon1_dem[0], 0 - mon1_dem[1]/2])
    # Start: Center = [8, 0], Bottom Left = [0, -4.5]
    point_of_rotation2 = np.array([offset2, 0 - mon2_dem[1]/2])

    # The monitor's center falls half of their width to the right and left of (0, 0) such that their shared edge is always on x = 0.
    rot_around1 = [0 - offset1 - mon1_dem[0]/2, 0]
    rot_around2 = [0 + offset2 + mon2_dem[0]/2, 0]

    rec1 = Rectangle(point_of_rotation1, mon1_dem[0], mon1_dem[1], color="y", transform=Affine2D().rotate_deg_around(*(rot_around1[0], rot_around1[1]), i)+ax.transData)
    rec2 = Rectangle(point_of_rotation2, mon2_dem[0], mon2_dem[1], color="b", transform=Affine2D().rotate_deg_around(*(rot_around2[0],rot_around2[1]), -i)+ax.transData)

    ax.add_patch(rec1)
    ax.add_patch(rec2)

    plt.plot()
    plt.plot([rot_around1[0]], [rot_around1[1]], marker="o")
    plt.plot([rot_around2[0]], [rot_around2[1]], marker="o")

    ### Plot
    # plt.legend(f"{i}")
    plt.grid("on")
    plt.axis("scaled")
    plt.pause(0.0001)

plt.show()
plt.close()