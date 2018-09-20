import numpy as np 

def count_init(matrix):
    dict_count={}
    size=np.size(matrix)
    matrix = matrix.reshape(size,1)
    for m in matrix:
        m=float(m)
        if(m in dict_count.keys()):
            dict_count[m]=dict_count[m]+1
        else:
            dict_count[m]=1
    return dict_count
b = np.array(np.random.rand(2,5))
print(count_init(b))


