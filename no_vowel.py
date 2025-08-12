'''
x = input().strip()


for ch in x:
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
        ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        print("Vowel")
    else:
        print("Consonant")
'''

text = input().strip()
vowel = ['a','e','i','o','u', 'A','E','I','O','U']
re =''

for ch in text:
    if ch not in vowel: # chk if element/ch is vowel or not
        re = re+ch #if yes(means ch is not vowel), keep it        


print(re)



