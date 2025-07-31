rank_order = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
ranks = input().split()

sorted_ranks = [ ]  # createan empty list to store sorted ranks
for r in rank_order: #r  = each element eg. 'A' , '2'...'K' in rank_order(list)
    if r in ranks: #is r in ranks(user input list), if yes then do the next line, if not skip the next line do else: block if it exists.
        sorted_ranks.append(r) # append r to sorted_ranks if r exists in ranks

#or
#sorted_ranks = sorted(ranks, key=lambda r: rank_order.index(r))

print(sorted_ranks)  # → ['A','4','5','8','9','K']
print(*sorted_ranks)  # → A 4 5 8 9 K

