import bitIO
import sys

infile = open('DenGrimmeKælling.txt', 'rb')
outfile = open('Encoded.txt', 'wb')

bitstreamin = bitIO.BitReader(infile)
bitstreamout = bitIO.BitWriter(outfile)

i = bitstreamin.readint32bits()
#lav liste/table add 1 på liste[i]

#lav liste/table
while True:
      
    x = bitstreamin.readint32bits()
    #add 1 på liste[x]
    
    
    
    if not bitstreamin.readsucces():
               #bitstreamout.writeint32bits(liste)
                break
    

bitstreamout.writebit(0)
bitstreamout.writebit(1)

bitstreamout.close()
bitstreamin.close()
