for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        if j == 1:
            print(format(i * j, "3d"), end="\n")
        else:
            print(format(i * j, "3d"), end=" ")