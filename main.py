import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
# tangential force on a pendulum is 
# its mass * gravity * sin(theta) where
# theta is equal to the angle between the origin y axis

# assume a non inertial arm

# in kg
mass = 1

# gravity
g = -9.81

# arm length
l = 1

# sim speed in hz
speed = 30

w, h = 500, 500

initial_theta = 90

# using polar coordinates (r, theta)
theta = initial_theta
vel = 0
t = 0
dt = 0.3

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    global theta, t, vel
    a = g * math.sin(math.radians(theta))
    vel += a * dt
    theta += vel * dt   
    t += dt
    x = l * math.sin(math.radians(theta))
    y = -l * math.cos(math.radians(theta))
    line.set_data([0, x], [0, y])
    return line,

ani = FuncAnimation(fig, animate, frames=range(1000),
                    init_func=init, blit=True, repeat=True)
plt.show()