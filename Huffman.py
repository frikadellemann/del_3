import PQHeap
from Element import Element

##n = len(C)
##Q = C
##for i in range(1,n-1):
##    z = new element
##    z.left = extractMin(Q)
##    z.right = extractMin(Q)
##    z.freq = z.left.freq+z.right.freq
##    Q.insert(z)
##return extractMin(Q)

def huffman(table):
    pq = []
    for i in range(len(table)):
        PQHeap.insert(pq, Element(table[i],i))
    
    for i in range(len(table)-1):
        left = PQHeap.extractMin(pq)
        right = PQHeap.extractMin(pq)
        #print(str(left.data) + ':' + str(right.data))
        e = Element(left.key + right.key, None)
        e.left = left
        e.right = right
        PQHeap.insert(pq, e)
        
    return pq
             
    
        
