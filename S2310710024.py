__doc__ = "sample file for ploting method \
           baed on \
           https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/"

#based on
#source: https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/

#required imports
import argparse
import matplotlib.pyplot as plt
import numpy as np

#================================================
# set argsparser 
parser = argparse.ArgumentParser()

parser.add_argument('-mass', type=int, default=1000)
parser.add_argument('-velocity', type=int, default=20)
parser.add_argument('-friction', type=float, default=0.65)

args = parser.parse_args()

print("\nMass:", args.mass, "kg")
print("Velocity:", args.velocity, "m/s")
print("Friction:", args.friction)

# Implementation

mass = args.mass          # mass
velocity0 = args.velocity     # v(t=0)
friction = args.friction      # mu
acc = 0                   # acceleration
gravity = 9.81            # gravity on earth  

# with: Fr = friction * mass * gravity
acc = friction * gravity

# time
t = np.linspace(0, (velocity0 / acc))

# calculate velocity
velocityBreaking = velocity0 - (acc * t)

# calculate braking distance
distanceBraking = velocity0 * t - (1/2) * acc * pow(t, 2)
# braking distance with rule of thumb
rot_distanceBraking = pow((velocity0*3.6/10), 2)

# print results 
print("\nTime for stillstand:", round(t[-1], 2), "s")
print("Braking distance:", round(distanceBraking[-1], 2), "m")
print("Braking distance with rule of thumb:", round(rot_distanceBraking, 2), "m\n")

# Plot results 

#define figure
fig,axs = plt.subplots(1, 2, figsize=(20,10))

# add one plot for velocity
axs[0].plot(t,velocityBreaking)
axs[0].set_xlabel("time [s]")
axs[0].set_ylabel("velocity [m/s]")
axs[0].grid()

# add another plot for the braking distance
axs[1].plot(t, distanceBraking)
axs[1].set_xlabel("time [s]")
axs[1].set_ylabel("distance [m]")
axs[1].grid()

#add plot label
fig.suptitle("Plots\n\n1. velocity/time\n2. distance/time", fontweight ="bold")

# export as PDF
plt.savefig("Plots.pdf")
plt.show()
