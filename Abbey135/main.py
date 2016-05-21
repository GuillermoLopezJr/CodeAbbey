code = {' ': '11', 'e': '101', 't': '1001', 'o': '10001', 'n': '10000', 'a': '011', 's': '0101', 'i': '01001', 'r': '01000', 'h': '0011', 'd': '00101', 'l': '001001', '!': '001000', 'u': '00011', 'c': '000101', 'f': '000100', 'm': '000011', 'p': '0000101', 'g': '0000100', 'w': '0000011', 'b': '0000010', 'y': '0000001', 'v': '00000001', 'j': '000000001', 'k': '000000000', 'x': '00000000001', 'q': '000000000001', 'z': '000000000000'}

def appendZeroes(bits, length):
    if (len(bits) == length):
        return bits
    else:
           amount = length - len(bits)
           word = bits + '0'*amount 
           return word
            
def sepChunk(bitStream, amount): 
    byte = ""
    counter = 0;
    byteList = []
    for ch in bitStream:
        byte += ch
        counter += 1
        if (counter == amount):
           byteList.append(byte)
           counter = 0
           byte = ""

    if (counter != 0):
        byte = appendZeroes(byte, amount) 
        byteList.append(byte)

    return byteList
    
def printAns(hexList):
    print("\nanswer: ")
    for elt in hexList:
        print(elt, end=" ")

def main():
    print("input data: ")
    sentence = input()
    bitStream = "" 
    for ch in sentence:
        bitStream += code[ch]
    byteList = sepChunk(bitStream, 8)
    hexList = []
    for byte in byteList:
        dec = int(byte, 2)
        hexList.append('{:02x}'.format(dec).upper())

    printAns(hexList) 

main()
