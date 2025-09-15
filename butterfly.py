n = int(input())   # user inputs size, controls height and width

# ---------- TOP HALF ----------
for i in range(0, n, 1):  
    # Left stars (grow from 1 to n)
    for j in range(0, i+1, 1):
        print("*", end="")

    # Middle dashes part 1 (count = n - i)
    for k in range(n, i, -1):
        print("-", end="")

    # Middle dashes part 2 (count = n - i - 1)
    for k in range(n, i+1, -1):
        print("-", end="")

    # Right stars (mirror of left)
    for l in range(0, i+1, 1):
        print("*", end="")

    # End of line
    print()

# Middle solid line of stars (always width = 2n+1)
print("*" * ((2*n) + 1))


# ---------- BOTTOM HALF ----------
for i in range(0, n, 1):
    # Left stars (shrink from n down to 1)
    for j in range(n, i, -1):
        print("*", end="")

    # Middle dashes part 1 (count = i+1)
    for k in range(0, i+1, 1):
        print("-", end="")

    # Middle dashes part 2 (count = i)
    for k in range(0, i, 1):
        print("-", end="")

    # Right stars (mirror of left)
    for j in range(n, i, -1):
        print("*", end="")

    # End of line
    print()