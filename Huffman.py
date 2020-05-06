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
        e = Element(left.key + right.key, None)
        e.left = left
        e.right = right
        PQHeap.insert(pq, e)
        
    code = ''
    dictionary = {}
    prnt(pq[0], code, dictionary)
    return dictionary

    
def prnt(e, code, dictionary):
    
    if e.data == None:
        code += '0'
        prnt(e.right, code, dictionary)
        code = code[:-1]
        code += '1'
        prnt(e.left, code, dictionary)
        code = code[:-1]
    else:
        #print(code)
        #print(str(e.key) + ':' + str(e.data))
        dictionary[e.data] = code
             
    
        
