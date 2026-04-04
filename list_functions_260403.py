num_list = [23, 45, 27, 11, 25, 65, 78]

def getIndex(num_list,target):
    i=0
    for a in num_list:
        if a == target:
            return i
        else:
            i+=1
print(getIndex(num_list, 25))

def getMax(nl):
    max_val = nl[0]
    for n in nl:
        if n > max_val:
            max_val = n
    return max_val
        
nl = [23, 45, 27, 11, 25, 65, 78]
print(getMax(nl))

def getMin(nl):
    min_val = nl[0]
    for i in nl:
        if i < min_val:
            min_val = i
    return min_val
        
nl = [23, 45, 27, 11, 25, 65, 78]
print(getMin(nl))

def countGT(nl, t):
    c = 0
    for n in nl:
        if n > t:
            c += 1
    return c
nl = [23, 45, 27, 11, 25, 65, 78]
print(countGT(nl, 45))

def sumList(nl):
    t = 0
    for n in nl:
        t += int(n)
    return t
nl = [23, 45, 27, 11, 25, 65, 78]

print(sumList(nl))

def swapList(nl):
    l = len(nl)
    for i in range(l//2):
        nl[i], nl[l -1 -i] = nl[l -1 -i], nl[i]

nl = [23, 45, 27, 11, 25, 65, 78]

swapList(nl)
print(nl)