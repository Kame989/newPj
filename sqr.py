n = int(input())
if n <= 2:
    print("Box's height must be more than 2")
else:
    print('#'*n)#top

    for _ in range(n-2):  # middle rows
        print('#' + ' ' * (n-2) + '#')

    print('#'*n)  # bottom


    '''
    Quick dry-run for n = 3
Top: ###

Middle rows: n-2 = 1 iteration → # #

Bottom: ###

Output:

shell
Copy code
###
# #
###
And if the user enters n = 2 (or less), you immediately get:

rust
Copy code
Box's height must be more than 2
with no box drawn.







You said:
for _ in range(n-2):
    print('#' + ' '*(n-2) + '#')                           
    

When n = 3, then:

for _ in range(n-2):  # → range(1) → one iteration with _ 
    print('#' + ' '*(n-2) + '#')
becomes:

so
print('#' + ' ' * 1 + '#')  # since n-2 = 1

# #
Exactly one middle row, giving the full 3×3 box:

shell
Copy code
###    top
# #     one middle row
###    bottom

meaningso for _ in range(n-2): just tell how many time to repeat inside block of code in this case n= 3 , only one time. 
it is different from; for i in range(): as i = iteration index which start from 0 to n-1

or



    for i in range (n):
        for j in range(n):
            if (i==0 or i==n-1 or j==0 or j==n-1):
                print("*", end=" ")
            else:
                print("", end="  ")
        print()'''