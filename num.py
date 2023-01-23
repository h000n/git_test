# import numpy as np
# from tqdm import tqdm
# w1 = np.zeros((1,1))
# w0 = w1
# X=np.random.rand(100,1)
# Y = X*2+2
# ones = np.ones((len(Y),1))
# lr=0.0001
# for i in tqdm(range(100000)):
#     dif = Y-np.dot(X,w1.T)-w0
#     w1 = w1+lr*(2/len(Y))*np.dot(X.T,dif)
#     w0 = w0+lr*(2/len(Y))*np.dot(ones.T,dif)



# diff = (Y-np.dot(X,w1.T)-w0)
# print(w1,w0,diff[diff>0.05])

import numpy as np
from tqdm import tqdm
w0 = np.zeros((1,1))
X=np.random.rand(100,100)
Y = X*2+2
ones = np.ones((len(Y),1))
W = np.zeros((100,1))
lr=0.001
print(X.shape)

for i in tqdm(range(1)):
    pred = np.dot(X.T,W)
    dif = Y-pred-w0
    W = W+lr*(2/len(Y))*np.dot(X,dif)
    w0 = w0+lr*(2/len(Y))*np.dot(ones.T,dif)

print(W)
