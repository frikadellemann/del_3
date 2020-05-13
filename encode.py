# # Emil Blarke (eblar19) and Mads Frederik Larsen (madla15)
# We import the different methods for reading and writing, priority queue and Huffman tree 
import bitIO
import PQHeap
import Huffman
# The files are opened in binarymode seen by the 'rb' and 'wb'
# We stream the files
inpath = 'sample.txt'
infile = open(inpath, 'rb')
outfile = open('encoded.txt', 'wb')


bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)

# A table with 256 inquires, one for each of the possible bytes
table = list()
for i in range(256):
    table.append(0)

## delete??
def read(byte):
    v = 0
    for i in range(byte*8):
        v = (v << 1) | bitstreamin.readbit()
    return v
# Here we populate the frequency table,
# by incrementing in the table position corresponding to the read byte
# The while loop continues as long as there is something to read
# and breaks when file is read through

while True:
    x = read(1)
    if not bitstreamin.readsucces():
            break
    table[x] += 1

# Input file is read, and the stream gets closed
bitstreamin.close()

# Writes the frequency table to the output file, as 32 bit integers
for i in range(256):
    bitstreamout.writeint32bits(table[i])

#
#
#

# a recursive function for writing the Huffman codes of each byte to a dictionary
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

# Here the huffman tree is populated from the frequency table
pq = Huffman.huffman(table)

# codes and dictionary initialized
code = ''
dictionary = {}

# dictionary made
prnt(pq[0], code, dictionary)

# Input file is reopened, for translation
# and a new stream is made
infile = open(inpath, 'rb')
bitstreamin = bitIO.BitReader(infile)

# The input file is read again, translated byte wise to Huffman code
# and the codes are written to the output file
while True:
    x = read(1)
    if not bitstreamin.readsucces():
            break
    for i in dictionary[x]:
        bitstreamout.writebit(int(i))

# Finally the streams are closed
bitstreamout.writebit(0)
bitstreamout.writebit(1)
bitstreamout.close()
bitstreamin.close()

