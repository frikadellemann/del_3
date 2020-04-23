import bitIO
import sys

infile = open('DenGrimmeKælling.txt', 'rb')
outfile = open('Encoded.txt', 'wb')

bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)
i = bitstreamin.readint32bits()
bitstreamout.writeint32bits(i)

while True:
    x = bitstreamin.readbit()

    if not bitstreamin.readsucces():
               break
    bitstreamout.writebit(x)

bitstreamout.writebit(0)
bitstreamout.writebit(1)

bitstreamout.close()
bitstreamin.close()
