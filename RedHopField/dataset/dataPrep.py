def load_data(f):
    with open(f, 'r') as file:
        x = [[int(value) for value in line.split()] for line in file]
    return x

def print_1D_in_2D(matrix, y):
    print("Matrix:")
    for i in range(0, len(matrix), y):
        for j in range(y):
            if matrix[i + j] == -1:
                print("0", end='')
            else:
                print("1", end='')
        print()
        