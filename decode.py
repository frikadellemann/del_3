# # Emil Blarke (eblar19) and Mads Frederik Larsen (madla15)
import bitIO
import PQHeap
import Huffman

# Here we import the methods for reading and writing bits in files
# and creating the priority queue and the huffman tree
infile = open('encoded.txt', 'rb')
outfile = open('decoded.txt', 'wb')

# The files are opened in binary read or write mode 
# seen as 'rb' and 'wb'
bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)

# Streams are created
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
# it sums up the total bytes to know when it's done
while readBytes < totalBytes:
    x = bitstreamin.readbit()
    if x == 0:
        position = position.left
    else:
        position = position.right
    if position.data != None:
        bitstreamout._writebits(position.data, 8)
        position = tree[0]
        writtenBytes += 1
## evt
##bitstreamout.writebit(0)
##bitstreamout.writebit(1)       
bitstreamout.close()
bitstreamin.close()

