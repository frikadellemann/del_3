import bitIO
import PQHeap
import Huffman
#import sys

infile = open('G.jpg', 'rb')
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
for i in range(255):
    bitstreamout.writeint32bits(table[i])
bitstreamin.close()

dictionary = Huffman.huffman(table)

infile = open('G.jpg', 'rb')
bitstreamin = bitIO.BitReader(infile)

while True:
    x = read(1)
    if not bitstreamin.readsucces():
            break
    bitstreamout.writebit(int(dictionary[x]))


bitstreamout.writebit(0)
bitstreamout.writebit(1)
bitstreamout.close()
bitstreamin.close()

