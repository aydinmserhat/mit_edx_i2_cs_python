# this file is just a sample

L = ['a', 'b', 'a']
d = {}
lst = []
for elm in L:
    d[elm] = d.get(elm, 0) + 1

print d
print d.values()

maximum = max(d.values())
print maximum

counts = [(j, i) for i, j in d.items()]
count, max_elm = max(counts)
print max_elm
maximum_elm = max(d, key = d.get)
print maximum_elm

for i in range(maximum):
    lst.append(maximum_elm)
print lst
L = lst
print L

