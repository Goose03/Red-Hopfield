def prepare_1D_matrix(x):
    return [-1 if value == 0 else value for value in x]

def prepare_2D_matrix(x):
    return [
        -1 if value == 0 else value
        for row in x
        for value in row
    ]

def prepare_matrix(x):
    if isinstance(x[0], list):
        return prepare_2D_matrix(x)
    else:
        return prepare_1D_matrix(x)

def hopfield(x1, x2):
    T = [[0 for _ in range(len(x2))] for _ in range(len(x1))]

    for i in range(len(x1)):
        for j in range(len(x2)):
            T[i][j] += x1[i] * x1[j]
            T[i][j] += x2[i] * x2[j]
            if i == j:
                T[i][j] = 0
    return T
    
def hopfield_update(T, x):
    new_x = [0 for _ in range(len(x))]
    for i in range(len(T)):
        s = 0
        for k in range(len(T)):
            s += T[i][k] * x[k]
        new_x[i] = 1 if s > 0 else -1
    return new_x
