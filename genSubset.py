def subsets(my_set):
    result = [[]]
    for x in my_set:
        result = result + [y + [x] for y in result]
    return result


#print subsets([1,2,3])

L = [1,2,3]
sub = [[]]
for i in L:
    for j in sub:
        sub = sub + [j + [i]]
print sub