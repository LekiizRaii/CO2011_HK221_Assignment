# Import libraries
from matplotlib.legend_handler import HandlerPatch
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import deltaequalto0 as de0
import deltalessthan0 as dl0
import deltamorethan0 as dg0

# Input coefs and initial values
fig, axes = plt.subplots(1, 2, figsize = (14, 6))
a = float(input("Type a value: "))
b = float(input("Type b value: "))
c = float(input("Type c value: "))
d = float(input("Type d value: "))
R0 = float(input("Type R0 value: "))
J0 = float(input("Type J0 value: "))
R, J, x = None, None, None
R_traj, J_traj, x_traj = None, None, None

# Some extras values for visualization
R_start = -4.5
J_start = -1
tmax = 0.5

# Calculate R, J, x for plotting
if abs(a ** 2 + d ** 2 - 2 * a * d + 4 * b * c) < 1.0e-17:
    R, J, x = de0.visualization(a, b, c, d, R0, J0, tmax)
    R_traj, J_traj, x_traj = de0.visualization(a, b, c, d, R_start, J_start, 10)
elif a ** 2 + d ** 2 - 2 * a * d + 4 * b * c > 0:
    R, J, x = dg0.visualization(a, b, c, d, R0, J0, tmax)
    R_traj, J_traj, x_traj = dg0.visualization(a, b, c, d, R_start, J_start, 10)
else:
    R, J, x = dl0.visualization(a, b, c, d, R0, J0, tmax)
    R_traj, J_traj, x_traj = dl0.visualization(a, b, c, d, R_start, J_start, 10)

# Set axis lims for phase portrait
R0low = -5
R0high = 5
J0low = -5
J0high = 5

RomeoStyle = ""
if a > 0 and b > 0:
    RomeoStyle = "Eager Beaver"
if a > 0 and b < 0:
    RomeoStyle = "Narcissistic Nerd"
if a < 0 and b > 0:
    RomeoStyle = "Cautious Lover"
if a < 0 and b < 0:
    RomeoStyle = "Hermit"

JulietStyle = ""
if d > 0 and c > 0:
    JulietStyle = "Eager Beaver"
if d > 0 and c < 0:
    JulietStyle = "Narcissistic Nerd"
if d < 0 and c > 0:
    JulietStyle = "Cautious Lover"
if d < 0 and c < 0:
    JulietStyle = "Hermit"

# Plot R, J
axes[0].plot(x, R, label ="Romeo's")
axes[0].plot(x, J, label ="Juliet's")
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Love for the other")
axes[0].legend()
axes[0].set_title('Love between ' + RomeoStyle + ' and ' + JulietStyle)

# Preparation for quiver() plotting (for phase portrait)
r0 = np.linspace(R0low, R0high, 20)
j0 = np.linspace(J0low, J0high, 20)
nR0, nJ0 = np.meshgrid(r0, j0)
Rdot = a * nR0 + b * nJ0
Jdot = c * nR0 + d * nJ0
colorgrid = np.sqrt(Rdot*Rdot + Jdot*Jdot)
Rdotn = Rdot/np.sqrt(Rdot*Rdot + Jdot*Jdot)
Jdotn = Jdot/np.sqrt(Rdot*Rdot + Jdot*Jdot)
nR = R0high
nJ = J0high

# Plotting phase portrait by quiver()
axes[1].quiver(nR0, nJ0, Rdotn, Jdotn, colorgrid, pivot = 'mid', cmap = 'viridis')
axes[1].set_aspect('equal')
scat = axes[1].scatter(0, 0, marker = 'o',c = 'white', edgecolors = 'gray' , label = 'Fixed point (0,0)')
traj, = axes[1].plot(R_traj, J_traj, color = 'red')
axes[1].axis([R0low, R0high, J0low, J0high])
axes[1].set_title('Love between ' + RomeoStyle + ' and ' + JulietStyle)
axes[1].set_xlabel('Romeo\'s love for Juliet')
axes[1].set_ylabel('Juliet\'s love for Romeo')

# Create a fancy legend
class HandlerArrow(HandlerPatch):
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        arr = mpatches.Arrow(0, 3, 20, 0, width = 10)
        self.update_prop(arr, orig_handle, legend)
        arr.set_transform(trans)
        return [arr]
arr = mpatches.Arrow(0, 0, 1, 0, color = 'green', linewidth = 0.1, alpha = 0.5)
axes[1].legend(handles = [traj, scat, arr], labels = ['Trajectory', 'Fixed point (0, 0)', 'Vector field'], handler_map={mpatches.Arrow: HandlerArrow()}, loc = 3)

# Show the plot
plt.show()