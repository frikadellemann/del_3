import bitIO
import PQHeap
import Huffman
# We import the diffrent methods for reading and writing, priority que and Huffman tree 
inpath = 'sample.txt'
infile = open(inpath, 'rb')
outfile = open('encoded.txt', 'wb')
# The files are opened in binarymode seen by the 'rb' and 'wb'
# We stream the files
bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)
# A table with 256 inquires one for each of the possible instances of bytes
# its definde as 8bits
table = list()
for i in range(256):
    table.append(0)
def read(byte):
    v = 0
    for i in range(byte*8):
        v = (v << 1) | bitstreamin.readbit()
    return v    
# The while loop continues as long it has something to read
# else it sees its job done and breaks
# it reads from the inputfile and write it into the table
while True:
    x = read(1)
    if not bitstreamin.readsucces():
            break
    table[x] += 1

for i in range(256):
    bitstreamout.writeint32bits(table[i])

bitstreamin.close()
#
#
#
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
#
#
#
pq = Huffman.huffman(table)
code = ''
dictionary = {}
prnt(pq[0], code, dictionary)

infile = open(inpath, 'rb')
bitstreamin = bitIO.BitReader(infile)
k = 0
while True:
    x = read(1)
    if not bitstreamin.readsucces():
            break
    for i in dictionary[x]:
        bitstreamout.writebit(int(i))
    k += 1

bitstreamout.writebit(0)
bitstreamout.writebit(1)
bitstreamout.close()
bitstreamin.close()

