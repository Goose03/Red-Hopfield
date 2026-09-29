from .hopfield import hopfield, hopfield_update, prepare_matrix
from ..dataset.dataPrep import load_data, print_1D_in_2D

f1 = 'RedHopField/dataset/uno.txt'
f2 = 'RedHopField/dataset/dos.txt'
f3 = 'RedHopField/dataset/x.txt'

# x1 = [1, 1, 1, -1]
# x2 = [-1, -1, -1, 1]
# x3 = [1, -1, 1, -1]

x1 = prepare_matrix(load_data(f1))
x2 = prepare_matrix(load_data(f2))
x3 = prepare_matrix(load_data(f3))

res = hopfield_update(hopfield(x1, x2), x1)

print_1D_in_2D(res, 5)

print(f"Result:\n{res}")