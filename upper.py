import re
'''
text = "ThisIsAStringWithCamelCase"
words = re.findall('[A-Z][^A-Z]*', text)
print(*words)
'''

t= input().strip()
words = re.findall('[A-Z][^A-Z]*', t)
print(*words)


