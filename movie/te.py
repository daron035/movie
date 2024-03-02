c = ['2020', '1980']
# c = [2020, 1980]

a = [(int(i), int(i)+10) for i in c]
# a = list(map(list, a))
print(a)
a = [x for l in a for x in l]
print(a)