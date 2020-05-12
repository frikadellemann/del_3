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
#print(table)
   
#print(totalBytes)
pq = Huffman.huffman(table)

##code = ''
##dictionary = {}
##def prnt(e, code, dictionary):
##    
##    if e.data == None:
##        code += '0'
##        prnt(e.right, code, dictionary)
##        code = code[:-1]
##        code += '1'
##        prnt(e.left, code, dictionary)
##        code = code[:-1]
##    else:
##        dictionary[e.data] = code
##prnt(pq[0], code, dictionary)
##print(dictionary[119])
##print(dictionary[108])
##print(dictionary[107])
##print(dictionary[106])
#print(totalBytes)
readBytes = 0
position = pq[0]

while readBytes < totalBytes:
    x = bitstreamin.readbit()
    if x == 0:
        position = position.left
    else:
        position = position.right
    if position.data != None:
        bitstreamout._writebits(position.data, 8)
        #print(position.data)
        position = pq[0]
        readBytes += 1
    

    
bitstreamout.close()
bitstreamin.close()

