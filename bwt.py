seq = "ACTTGACGCTACGTGCATGAC$"

lis = []
for i in range(len(seq)):
    # print(i)
    tmp = seq[i:] + seq[:i]
    # print(tmp)
    lis.append(tmp)

sorted_lis = sorted(lis)
# for i in sorted_lis:
#     print(i)
first = []
last = []
for i in sorted_lis:
    first.append(i[0])
    last.append(i[-1])
print(first)
print(last)
