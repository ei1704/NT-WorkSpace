import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inline

x = np.linspace(0,2*np.pi)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
labels = ["90°","180°","270°","360°"]
positions = [np.pi/2,np.pi,np.pi*3/2,np.pi*2]

fig = plt.figure(figsize=(8,2))

ax = fig.add_subplot(1,3,1)
ax.set_title("y=sin(x)")
#ax.xlabel("x-axis")
#ax.ylabel("y-axis")
ax.grid(True)
ax.set_xticks(positions)
ax.set_xticklabels(labels)
#ax.set_xlabels(labels)
#ax.set_xlabels([-1,-0.5,0,0.5,1])
ax.set_ylim(-1,1)
ax.plot(x,y1,color="r")


bx = fig.add_subplot(1,3,2)
bx.set_title("y=cos(x)")
bx.grid(True)
bx.set_xticks(positions)
bx.set_xticklabels(labels)
bx.set_ylim(-1,1)
bx.plot(x,y2,color="b")

cx = fig.add_subplot(1,3,3)
cx.set_title("y=tan(x)")
cx.grid(True)
cx.set_xticks(positions)
cx.set_xticklabels(labels)
cx.set_ylim(-1,1)
cx.plot(x,y3,color="g")

plt.show()
