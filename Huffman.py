import PQHeap
from Element import Element

def huffman(table):
    # Initializing priority queue
    pq = []
    # Filling priority queue
    for i in range(len(table)):
        PQHeap.insert(pq, Element(table[i],[i]))
    # Building the Huffman tree
    # combines the two lowest frequency elements, extracted from the queue,
    # into a tree  and inserts the tree in the queue
    # This is done until the queue only has a single element, the Huffman tree
    for i in range(len(table)-1):
        left = PQHeap.extractMin(pq)
        right = PQHeap.extractMin(pq)
        e = Element(left.key + right.key, [left,right])
        PQHeap.insert(pq, e)

    return pq
             
    
        
