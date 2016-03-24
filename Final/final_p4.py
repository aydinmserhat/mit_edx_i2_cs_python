L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
#L = [1, 1, 1, 1, 4]
n = 4
def getSublists(L, n):
    sublist = []
    for i in range(len(L)):
        nsublist = L[i:n+i][:]
        if len(nsublist) == n:
            sublist.append(nsublist)
    return sublist


print getSublists(L,n)


def longestRun(L):
    n = 1
    val = [1]
    for k in range(len(L)-1):
        if L[k] <= L[k + 1]:
            n = n + 1
            val.append(n)
        else:
            n = 1

    return max(val)


print longestRun([7, 4, 1, -7, -11])