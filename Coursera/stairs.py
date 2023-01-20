import sys

number_of_hashes = int(sys.argv[1])
#number_of_hashes = 5
for i in range(1 , number_of_hashes+1):
    y = ' '*(number_of_hashes-i)+'#' * i
    print(y)
