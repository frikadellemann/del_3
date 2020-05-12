import bitIO
import PQHeap
import Huffman

infile = open('encoded.txt', 'rb')
outfile = open('decoded.txt', 'wb')

bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)

table = list()
totalBytes = 0
for i in range(256):
    x = bitstreamin.readint32bits()
    table.append(x)
    totalBytes += x

tree = Huffman.huffman(table)

readBytes = 0
position = tree[0]

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

