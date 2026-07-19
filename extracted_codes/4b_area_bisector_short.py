import numpy as np
import matplotlib.pyplot as plt
def tri(x,a,b,c):
    return np.maximum(np.minimum((x-a)/(b-a),(c-x)/(c-b)),0)
x = np.linspace(0,10,2000)
m1 = tri(x,1,3,5)
m2 = tri(x,4,6,9)
m = np.maximum(m1,m2)
dx = x[1]-x[0]
area = np.cumsum(m)*dx
boa = x[np.where(area >= area[-1]/2)[0][0]]
plt.plot(x,m1,'--')
plt.plot(x,m2,'--')
plt.plot(x,m)
plt.fill_between(x,m,alpha=0.3)
plt.axvline(boa)
plt.grid()
plt.show()
print("BOA =", round(boa,3))
