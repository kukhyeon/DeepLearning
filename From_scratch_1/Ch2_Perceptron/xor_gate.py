import numpy as np
from and_gate import AND
from or_gate import OR

# A xor B = A'B + AB'
def XOR(x1, x2):
    s1 = AND(1-x1, x2)
    s2 = AND(x1, 1-x2)
    y = OR(s1, s2)
    if y > 0:
        return 1
    else:
        return 0
    
if __name__ == "__main__":
    print(XOR(0, 0))
    print(XOR(0, 1))
    print(XOR(1, 0))
    print(XOR(1, 1))