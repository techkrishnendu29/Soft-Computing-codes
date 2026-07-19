import numpy as np
import matplotlib.pyplot as plt
# XOR dataset
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])
y = np.array([-1,1,1,-1])
lr = 0.01
epochs = 20
w = np.zeros(X.shape[1])
b = 0
cost_list = []
for epoch in range(epochs):
    net_input = np.dot(X,w) + b
    output = net_input
    error = y - output
    w = w + lr * np.dot(X.T,error)
    b = b + lr * error.sum()
    cost = (error**2).sum()/2
    cost_list.append(cost)
print("Final Weights:",w)
print("Bias:",b)
net_input = np.dot(X,w)+b
pred = np.where(net_input>=0,1,-1)
print("Actual:",y)
print("Predicted:",pred)
plt.plot(range(1,epochs+1),cost_list)
plt.xlabel("Epoch")
plt.ylabel("Cost")
plt.title("ADALINE Training Error on XOR")
plt.show()
