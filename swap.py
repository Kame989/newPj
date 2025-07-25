sen = input( )
word = sen.split()
print(word)
re_word = word[ : : -1]
result = " ".join(re_word)
print(result)