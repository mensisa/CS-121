#Pattern A
print("Pattern A\n")
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Pattern B
print("\nPattern B\n")
for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Pattern C
print("\nPattern C\n")
for i in range(1, 7):
    print("  " * (6 - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

#Pattern D
print("\nPattern D\n")
for i in range(6, 0, -1):
    print("  " * (6 - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
