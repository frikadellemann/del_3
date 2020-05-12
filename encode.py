import bitIO
import PQHeap
import Huffman
#import sys
inpath = 'text.txt'
infile = open(inpath, 'rb')
outfile = open('encoded.txt', 'wb')

bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)



table = list()
for i in range(256):
    table.append(0)
def read(byte):
    v = 0
    for i in range(byte*8):
        v = (v << 1) | bitstreamin.readbit()
    return v    


    

while True:
    x = read(1)
    if not bitstreamin.readsucces():
            break
    table[x] += 1
#print(table)
for i in range(256):
    bitstreamout.writeint32bits(table[i])

bitstreamin.close()

def prnt(e, code, dictionary):
    
    if e.data == None:
        code += '0'
        prnt(e.left, code, dictionary)
        code = code[:-1]
        code += '1'
        prnt(e.right, code, dictionary)
        code = code[:-1]
    else:
        dictionary[e.data] = code

pq = Huffman.huffman(table)
code = ''
dictionary = {}
prnt(pq[0], code, dictionary)

#print(dictionary)
infile = open(inpath, 'rb')
bitstreamin = bitIO.BitReader(infile)
k = 0
while True:
    x = read(1)
    if not bitstreamin.readsucces():
            break
    #bitstreamout.writebit(int(dictionary[x]))
    for i in dictionary[x]:
        bitstreamout.writebit(int(i))
    k += 1
    #print(dictionary[x])

#print(k)
bitstreamout.writebit(0)
bitstreamout.writebit(1)
bitstreamout.close()
bitstreamin.close()

