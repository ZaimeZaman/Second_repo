#Q.5: Write a program in python to print the output as given
#  XXXXXX
#  XXXXX
#   xxxx
#    xxx
#    xx
#     x using for loop...

print("\n\n\t***This is a pattern printing program***\n\n")
rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("X", end=" ")
    print("")
print("\n\t***THANKS***\n\n")