import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inline

x = np.linspace(0,2*np.pi)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
labels = ["90°","180°","270°","360°"]
positions = [np.pi/2,np.pi,np.pi*3/2,np.pi*2]

plt.title("graphs of trigonometric  functions")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.xticks(positions,labels)
plt.yticks([-1,-0.5,0,0.5,1])
plt.ylim(-1,1)

plt.plot(x,y1,color="r")
plt.plot(x,y2,color="b")
plt.plot(x,y3,color="g")


plt.show()
