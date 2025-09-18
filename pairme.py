n = input()

stack = [ ]

for ch in n:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack:
            print("False")
            exit()
        top = stack[-1]
        if (ch == ')' and top == '(') or\
            (ch == ']' and top == '[') or\
             (ch == '}' and top == '{' ):
            stack.pop()
        else:
            print("False")
            exit()

if not stack:
    print("True")
else:
    print("False")