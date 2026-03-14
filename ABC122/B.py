s = input()

length = 0
longest = 0

for a in s:
    # if a == "A" or a == "C" or a == "G" or a == "T":
    if a in "ACGT":
        length += 1
    else:
        longest = max(longest, length)
        length = 0

longest = max(longest, length)
print(longest)