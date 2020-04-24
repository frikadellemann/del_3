import bitIO
import sys

infile = open('DenGrimmeKælling.txt', 'rb')
outfile = open('Encoded.txt', 'wb')

bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)


#lav table og fyld med 0
table = list()
for i in range(255):
    table.append(0)


while True:
      
    x = bitstreamin.readint32bits()
    print(x)
    if not bitstreamin.readsucces():
               #bitstreamout.writeint32bits(liste)
                break
    
    

bitstreamout.writebit(0)
bitstreamout.writebit(1)

bitstreamout.close()
bitstreamin.close()
