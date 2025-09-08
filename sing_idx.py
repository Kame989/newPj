n = int(input())
lyrics = ["Bling", "bang", "bang", "bling", "bang", "bang", "Bling", "bang", "bang", "born"]

full = n//10

remain = n%10

for _ in range(full):
        print(" ".join(lyrics))

if remain > 0:
    print(" ".join(lyrics[:remain]))


