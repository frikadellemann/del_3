## Emil Blarke (eblar19) and Mads Frederik Larsen (madla15)

# Here we import the methods for reading and writing bits in files
# and creating the priority queue and the huffman tree
import bitIO
import PQHeap
import Huffman
import sys

# The file paths are declared, either from commandline arguments or simple inputs
if len(sys.argv) == 3:
    inPath = sys.argv[1]
    outPath = sys.argv[2]
else:
    inPath = input('Write name of compressed file: ')
    outPath = input('Write name of decompressed file: ')

# The files are opened in binary read or write mode 
# seen as 'rb' and 'wb'
inFile = open(inPath, 'rb')
outFile = open(outPath, 'wb')

# Streams are created
bitstreamin = bitIO.BitReader(inFile)
bitstreamout = bitIO.BitWriter(outFile)

# The block size of the encoding is defined, in bytes
# and the required size of the table is calculated from that
blockSize = 1
tableSize = 2**(blockSize*8)

# Initialize frequency table as an empty list
table = list()
totalBlocks = 0

# Populate the table, from the huffman encoded file
# We keep track of the number of blocks from the original file
for i in range(tableSize):
    x = bitstreamin.readint32bits()
    table.append(x)
    totalBlocks += x


tree = Huffman.huffman(table)

# Initialize variables used in decoding
writtenBlocks = 0
position = tree[0]

# It starts from the root, which is at index 0 in the list
# it sums up the written blocks, to know when it's done
while writtenBlocks < totalBlocks:
    x = bitstreamin.readbit()
    if x == 0:
        position = position.data[0]
    else:
        position = position.data[1]
    if len(position.data) == 1:
        outFile.write(bytes([position.data[0]]))
        position = tree[0]
        writtenBlocks += 1

# Work is done, so the streams are closed    
bitstreamout.close()
bitstreamin.close()

