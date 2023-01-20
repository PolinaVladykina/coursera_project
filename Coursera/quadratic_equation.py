import sys
from cmath import sqrt

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b ** 2 - 4 * a * c

x_1 = int(((- b + sqrt(D)) / (2 * a)).real)
x_2 = int(((- b - sqrt(D)) / (2 * a)).real)
print(x_1)
print(x_2)