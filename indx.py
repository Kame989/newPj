m_list = [1,2,3,5,7,9,11,13,15,17,19,21,23,25,27,29]

n = int(input())

if n in m_list:
    print(m_list.index(n))
else:
    print("-1")