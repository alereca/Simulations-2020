import numpy as np

def hypergeometric_num(p,ns,tn):
    x, r, tnn, pn = 0, np.random.uniform(), tn, p
    for i in range (ns):
        if r > p:
            s = 0
        else:
            s = 1
            x += 1
        pn = (tnn*pn - s)/(tnn-1)
        tn -= 1

    return x

