n = len(C)
Q = C
for i in range(1,n-1):
    z = new element
    z.left = extractMin(Q)
    z.right = extractMin(Q)
    z.freq = z.left.freq+z.right.freq
    Q.insert(z)
return extractMin(Q)

