import bitIO
import PQHeap
#import sys

infile = open('G.jpg', 'rb')
outfile = open('encoded.txt', 'wb')

bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)


#lav table og fyld med 0
table = list()
for i in range(256):
    table.append(0)
print(len(table))
def read(byte):
    v = 0
    for i in range(byte*8):
        v = (v << 1) | bitstreamin.readbit()
    return v    

#def write(table):
    

while True:
    x = read(1)
    #print(x)
    if not bitstreamin.readsucces():
            break
    table[x] += 1
    

for i in range(255):
    bitstreamout.writeint32bits(table[i])
print(table)


    

bitstreamout.writebit(0)
bitstreamout.writebit(1)

bitstreamout.close()
bitstreamin.close()
