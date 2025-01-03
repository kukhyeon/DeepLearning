import numpy as np

def NOR(x1, x2):
    X = np.array([x1, x2])
    w1, w2, bias = -0.8, -0.8, 0.7
    W = np.array([w1, w2])
    tmp = np.sum(X*W) + bias
    
    if tmp <= 0:
        return 0
    else:
        return 1
    
# test
if __name__ == "__main__":
    print(NOR(0, 0))
    print(NOR(0, 1))
    print(NOR(1, 0))
    print(NOR(1, 1))