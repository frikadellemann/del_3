import bitIO
import PQHeap
import Huffman
# Here we import the methods for reading and writing
# the priority que and the huffman tree
infile = open('encoded.txt', 'rb')
outfile = open('decoded.txt', 'wb')
# The files are opened in binary mode 
# seen by 'rb' and 'wb'
bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)
# Streaming from the files
table = list()
totalBytes = 0
for i in range(256):
    x = bitstreamin.readint32bits()
    table.append(x)
    totalBytes += x
# Here we define that we go through all 256 inquries
tree = Huffman.huffman(table)

readBytes = 0
position = tree[0]
# It starts from the root index [0]
# it sums up the total bytes which it uses to know when
# it has written all out
while readBytes < totalBytes:
    x = bitstreamin.readbit()
    if x == 0:
        position = position.left
    else:
        position = position.right
    if position.data != None:
        bitstreamout._writebits(position.data, 8)
        position = tree[0]
        readBytes += 1
## evt
##bitstreamout.writebit(0)
##bitstreamout.writebit(1)       
bitstreamout.close()
bitstreamin.close()

