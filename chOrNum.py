n = input().strip()

num = ''
sum = 0  # keep your variable name

for char in n:
    if char.isdigit():
        num = num + char          # build the current number chunk
    else:
        if num != '':             # end of a chunk -> add it
            sum = sum + int(num)
            num = ''              # reset for next chunk

# if the string ends with digits, add that last chunk
if num != '':
    sum = sum + int(num)

format_sum = f"{sum:04d}"
print(format_sum)

'''For n = "J43OP" with your (chunk-sum) logic:

Start: num = '', sum = 0

J → not digit → else → num empty → do nothing

4 → digit → num = '4'

3 → digit → num = '43'

O → not digit → else runs and num is not empty →
sum = 0 + int('43') = 43, then num = ''

P → not digit → else → num empty → do nothing

End of loop → if num: is false → final sum = 43 → prints 0043

So yes: when the O arrives, you “cash in” the finished chunk '43' → add 43 to sum, then reset num to empty. ✅

One more subtle point you’ve likely got: if the string ends with digits, there’s no trailing letter to trigger the else, so we add the last chunk after the loop:

Example tail "...62df0"

you’ll build chunks: ... '62' (cash in when d hits) and then '0' at the end

loop ends with num == '0' → the final if num: adds 0 to the total
'''

