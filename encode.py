## Emil Blarke (eblar19) and Mads Frederik Larsen (madla15)

# We import the different methods for reading and writing,
# priority queue, Huffman tree and system inputs
import bitIO
import PQHeap
import Huffman
import sys

sys.setrecursionlimit(10000)

# The file paths are declared, either from commandline arguments or simple inputs
if len(sys.argv) == 3:
    inPath = sys.argv[1]
    outPath = sys.argv[2]
else:
    inPath = input('Write name of file to compress:')
    outPath = input('Write name of compressed file:')
    
# The files are opened in binarymode seen by the 'rb' and 'wb'
# We stream the files
inFile = open(inPath, 'rb')
outFile = open(outPath, 'wb')

# streams for input and output file
bitstreamin = bitIO.BitReader(inFile)
bitstreamout = bitIO.BitWriter(outFile)

# The block size of the encoding is defined, in bytes
# and the required size of the table is calculated from that
blockSize = 1 #byte
tableSize = 2**(blockSize*8)

# A table with 2^blockSize inquries, one for each of the possible bytes
table = [0] * tableSize

# Here we populate the frequency table,
# by incrementing the table in the position corresponding to the byte read
# The while loop continues as long as there are more bytes to read
byte = inFile.read(blockSize)
while byte != b'':
    table[byte[0]] += 1
    byte = inFile.read(blockSize)


# Input file is read, and the stream gets closed
bitstreamin.close()

# Writes the frequency table to the output file, as 32 bit integers
for i in range(tableSize):
    bitstreamout.writeint32bits(table[i])

# Here the huffman tree is populated from the frequency table
pq = Huffman.huffman(table)

# Recursive function for writing the Huffman codes of each byte to a list 'dictionary'
# It does an in-order traversal of the tree while keeping track of the path in the 'code'
# takes the arguments:
# 'e', the element to go from, initially the root of the tree
# 'code' an initially empty string, that it uses to keep track of the path down the tree
# 'dictionary' an initially empty list, where the codes are stored.

def populateDictionary(e, code, dictionary):
    
    if len(e.data) == 2:
        code += '0'
        populateDictionary(e.data[0], code, dictionary)
        code = code[:-1]
    else:
        dictionary[e.data[0]] = code
        return
    code += '1'
    populateDictionary(e.data[1], code, dictionary)
    code = code[:-1]

# codes and dictionary initialized for populateDictionary 
code = ''
dictionary = [0] * tableSize


populateDictionary(pq[0], code, dictionary)

# Input file is reopened, for translation
# and a new stream is made
inFile = open(inPath, 'rb')
bitstreamin = bitIO.BitReader(inFile)

# The input file is read again, translated byte wise to Huffman code
# and the codes are written to the output file
byte = inFile.read(blockSize)
while byte != b'':
    for i in dictionary[byte[0]]:
        bitstreamout.writebit(int(i))
    byte = inFile.read(blockSize)

# The streams are closed
bitstreamout.close()
bitstreamin.close()

