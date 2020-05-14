import PQHeap
from Element import Element

# Function that makes a Huffman tree from a list of frequencies
# Takes a list as the single argument and returns a tree filled with Elements,
# in the first position of a list
def huffman(table):
    # Initializing priority queue
    pq = []
    # Filling priority queue with Elements,
    # using the frequency as key and a list, with only the bytes value, as data
    for i in range(len(table)):
        PQHeap.insert(pq, Element(table[i],[i]))
    # Building the Huffman tree
    # combines the two lowest frequency elements, extracted from the queue,
    # into a tree  and inserts the tree back in the queue
    # This is done until the queue only has a single element, the Huffman tree
    for i in range(len(table)-1):
        left = PQHeap.extractMin(pq)
        right = PQHeap.extractMin(pq)
        # The frequencies of the two children are summed and used as key for the new element
        # The children are put in a list and stored in data of the element
        e = Element(left.key + right.key, [left,right])
        PQHeap.insert(pq, e)

    return pq
      
    
        
