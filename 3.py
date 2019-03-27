def max(a):
    Max=a[0]
    N = 4
    for i in range(0,N) :
        This=0
        j = i
        for j in range(0,N) :
        This += a[j]
        if This > Max:
        Max = This
    return Max