m_list = [ ]
while True:
    m = input()
    if m == 'exit':
        break
    m_list.append(m)

if len(m_list) == 0:
    print("There is no song in the album")
else:
    n = input()
    if not n.isdigit():
        print("The MP3 Player has an Error")
    else:
        n = int(n)
        if n < 1 or n > len(m_list):
            print("The MP3 Player has an Error")
        else:
            print("Currently playing:", m_list[n-1])


