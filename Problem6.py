import numpy as np

def make_matrix(m):
    A = np.random.normal(0, np.sqrt(m), size=(m, m))
    output = np.tril(A)
    return output

iteration = 100

#my GT ID is 903491217, an odd number
for i in range(1, iteration + 1):
    cur = i * 100
    mat = make_matrix(cur)
    #subquestion 1
    p_2 = np.linalg.norm(mat, ord = 2)
    p_inf = np.linalg.norm(mat, ord = np.inf)
    ratio = p_2 / p_inf
    #subquestion 2
    cond = np.linalg.cond(mat)
    print("Iteration " + str(i) + ": size " + str(cur) 
          + "; ratio "+ str(ratio) + "; cond " + str(cond))


    

