## Emil Blarke (eblar19) and Mads Frederik Larsen (madla15)

# We import the different methods for reading and writing,
# priority queue, Huffman tree and system inputs
import bitIO
import PQHeap
import Huffman
import sys



# The files are opened in binarymode seen by the 'rb' and 'wb'
# We stream the files
inPath = sys.argv[1]
outPath = sys.argv[2]

inFile = open(inPath, 'rb')
outFile = open(outPath, 'wb')


bitstreamin = bitIO.BitReader(inFile)
bitstreamout = bitIO.BitWriter(outFile)


# A table with 256 inquires, one for each of the possible bytes
table = [0] * 256


# streams for input and output file
bitstreamin = bitIO.BitReader(inFile)
bitstreamout = bitIO.BitWriter(outFile)

# A table with 256 inquires, one for each of the possible bytes
# all are set to 0 in initilized value
table = list()
for i in range(256):
    table.append(0)

## delete??
def read(byte):
    v = 0
    for i in range(byte*8):
        v = (v << 1) | bitstreamin.readbit()
    return v

inFile = open(inPath, 'rb')
outFile = open(outPath, 'wb')


bitstreamin = bitIO.BitReader(inFile)
bitstreamout = bitIO.BitWriter(outFile)

# A table with 256 inquires, one for each of the possible bytes
table = [0] * 256


# Here we populate the frequency table,
# by incrementing the table in the position corresponding to the byte read
# The while loop continues as long as there are more bytes to read


byte = inFile.read(1)
while byte != b'':
    table[byte[0]] += 1
    byte = inFile.read(1)


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
    
    if len(e.data) == 2:
        code += '0'
        prnt(e.data[0], code, dictionary)
        code = code[:-1]
        code += '1'
        prnt(e.data[1], code, dictionary)
        code = code[:-1]
    else:
        dictionary[e.data[0]] = code

# Here the huffman tree is populated from the frequency table
pq = Huffman.huffman(table)

# codes and dictionary for 'byte to code' initialized
code = ''
dictionary = [0] *256


# dictionary made
prnt(pq[0], code, dictionary)

# Input file is reopened, for translation
# and a new stream is made
inFile = open(inPath, 'rb')
bitstreamin = bitIO.BitReader(inFile)

# The input file is read again, translated byte wise to Huffman code
# and the codes are written to the output file
byte = inFile.read(1)
while byte != b'':
    for i in dictionary[byte[0]]:
        bitstreamout.writebit(int(i))
    byte = inFile.read(1)

# Finally the streams are closed
bitstreamout.close()
bitstreamin.close()

