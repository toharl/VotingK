from cvxopt import matrix, solvers


import helper
A = helper.load_pickle('A_v1.pickle')
b = helper.load_pickle('b_v1.pickle')
#print(A)
import numpy as np
import scipy.io

scipy.io.savemat('Ab_v1.mat', dict(A=A, b=b))
with open("A_v1.txt", "w") as text_file:
    print(f"{A}", file=text_file)
with open("b_v1.txt", "w") as text_file:
    print(f"{b}", file=text_file)
