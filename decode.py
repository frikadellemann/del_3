## Emil Blarke (eblar19) and Mads Frederik Larsen (madla15)

# Here we import the methods for reading and writing bits in files
# and creating the priority queue and the huffman tree
import bitIO
import PQHeap
import Huffman
import sys

# The files are opened in binary read or write mode 
# seen as 'rb' and 'wb'
inPath = sys.argv[1]
outPath = sys.argv[2]
inFile = open(inPath, 'rb')
outFile = open(outPath, 'wb')

# Streams are created
bitstreamin = bitIO.BitReader(inFile)
bitstreamout = bitIO.BitWriter(outFile)


table = list()
totalBytes = 0

# Here we populate the table, from the huffman encoded file
# We keep track of the number of bytes from the original file
for i in range(256):
    x = bitstreamin.readint32bits()
    table.append(x)
    totalBytes += x


tree = Huffman.huffman(table)

writtenBytes = 0
position = tree[0]
# It starts from the root, which is at index 0 in the list
# it sums up the written bytes to know when it's done
while writtenBytes < totalBytes:
    x = bitstreamin.readbit()
    if x == 0:
        position = position.data[0]
    else:
        position = position.data[1]
    if len(position.data) == 1:
        bitstreamout._writebits(position.data[0], 8)
        position = tree[0]
        writtenBytes += 1
    
bitstreamout.close()
bitstreamin.close()

