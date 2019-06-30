import sys
import os
import math

#TODO: compress mode
#TODO: decompress mode
#TODO: supercompress mode
#TODO: superdecompress mode
#TODO: stats

def helpmode():
    '''
    Hello! Welcome to my file compressing script. Here is how you can use it:
    
    Help mode:
        python3 filecompressing.py [parameter] --help
        or
        python3 filecompressing.py [parameter] -h

    Usage mode:
        python3 filecompressing.py [parameter] [file name]

    The following parameters are avaible:
        -c or --compress
        -d or --decompress
    To know what each mode does, call the script with the parameter on help mode

    The file can be either on the home folder or on the same folder as the script
    If you want to call it from elsewhere, use the path relative to one of these two.

    Additional info can be found on GitHub at https://github.com/sofiadsg/file-compressing
    '''
    print(helpmode.__doc__)


def buildProbabilityArray(d):
    """
    Builds a histogram for a file. 
    """
    fileArray = []
    for i in range(len(d)):
        fileArray.append(d[i])

    probabilityArray = [0]*256
    
    for i in range(len(fileArray)):
        probabilityArray[fileArray[i]] += 1
    
    number = sum(probabilityArray)
    percentage = [x/number for x in probabilityArray]
    enthropy = 0
    for i in percentage:
        if i != 0:
                enthropy += -1*i*math.log2(i)
    
    print('The entrophy of the file is: '+str(enthropy))
    return probabilityArray,percentage

def huffman(name,usingWords = False):
    """
    build a huffman code for a given histogram
    """
    probabilityArray,percentage = buildProbabilityArray(name)
    if usingWords:
        n = 65536
    else:
        n = 256

    nonZeroProbabilityArray = {}
    for i in range(len(probabilityArray)):
        if probabilityArray[i] != 0:
            nonZeroProbabilityArray[str(i)] = probabilityArray[i]
      
    codeArray = ['']*n
    done = False
    sumHistory = []
    while not (done):
        smallestProbabilityKey = min(nonZeroProbabilityArray,key = nonZeroProbabilityArray.get)
        smallestProbabilityValue = nonZeroProbabilityArray[smallestProbabilityKey]
        del nonZeroProbabilityArray[smallestProbabilityKey]
        secondSmallestProbabilityKey = min(nonZeroProbabilityArray,key = nonZeroProbabilityArray.get)
        secondSmallestProbabilityValue = nonZeroProbabilityArray[secondSmallestProbabilityKey]
        del nonZeroProbabilityArray[secondSmallestProbabilityKey]
        newValue = smallestProbabilityValue + secondSmallestProbabilityValue
        nonZeroProbabilityArray[smallestProbabilityKey+' '+secondSmallestProbabilityKey] = newValue
        sumHistory.append((smallestProbabilityKey,secondSmallestProbabilityKey))
        if len(nonZeroProbabilityArray) == 1:
            done = True
    
    sumHistory.reverse()
    for historyTuple in sumHistory:
        first = historyTuple[0].split()
        for i in first:
            codeArray[int(i)] += '1'
        second = historyTuple[1].split()
        for i in second:
            codeArray[int(i)] += '0'
    s = 0
    for i in range(256):
        s += len(codeArray[i])*percentage[i]

    print("The average word length is: " + str(s)) 
    return codeArray

def compress(name):
    """
    Compresses a file using a Huffman algorythm to find symbols for each of the 256 possible bytes
    """
    try:
        file = open(name,"rb")
    except FileNotFoundError:
        try:
            name = os.path.expanduser('~/'+name)
            file = open(name,'rb')
        except:
            print("Can't find file! Check if it is either on the same folder as this script or your home folder")
            sys.exit(1)
    
    d = bytearray(file.read())
    file.close()

    compress_name = name + '.dsg'

    dictionary = huffman(d,usingWords=False)
    writeBuffer = ''
    for i in dictionary:
        if i != '':
            size = format(len(i),'#010b')
            size = size[2:]
            key = format(dictionary.index(i),'#010b')
            key = key[2:]
            symbol = i
            writeBuffer += size + key + symbol

    writeBuffer += '0'*8

    for i in d:
        writeBuffer+=dictionary[i]
    
    if len(writeBuffer)%8 != 0:
        padsize = 8 - len(writeBuffer)%8
        writeBuffer += '0'*padsize
        padsize = format(padsize,'#010b')
        padsize = padsize[2:]
        writeBuffer += padsize
    
    file = open(compress_name,'wb')

    for i in range(int(len(writeBuffer)/8)):
        hexBuffer = writeBuffer[8*i:8*i+8]
        hexBuffer = int(hexBuffer,2)
        hexBuffer = format(hexBuffer,'#04x')
        hexBuffer = bytes.fromhex(hexBuffer[2:])
        file.write(hexBuffer)

    file.close()
    compressedLen = len(writeBuffer)
    beforeCompressionLen = len(d)
    compressionRate = beforeCompressionLen/compressedLen*8
    print("The compression rate was: " + str(compressionRate))

def decompress(name):
    """
    Decompress a .dsg file
    """
    try:
        file = open(name,"rb")
    except FileNotFoundError:
        try:
            name = os.path.expanduser('~/'+name)
            file = open(name,'rb')
        except:
            print("Can't find file! Check if it is either on the same folder as this script or your home folder")
            sys.exit(1)

    if name[-4:] != '.dsg':
        print('This file is not the correct type. This function decompresses only .dsg files')
        sys.exit(1)
    
    file = open(name,'rb')

    d = bytearray(file.read())
    file.close()
    bitString = ''
    for i in d:
        buffer = format(i,'#010b')
        buffer = buffer[2:]        
        bitString += buffer
    
    done = False
    match = False
    i = 1
    dictionary = ['']*256
    while not done:
        size = bitString[:8]
        bitString = bitString[8:]
        size = int(size,2)
        if size==0:
            break
        index = bitString[:8]
        bitString = bitString[8:]
        index = int(index,2)
        value = bitString[:size]
        bitString = bitString[size:]
        dictionary[index] = value

    padsize = int(bitString[-8:],2)
    bitString = bitString[:-8]
    bitString = bitString[:-1*padsize]
    nonZeroDict = list(filter(lambda a: a != '', dictionary))
    writeBuffer = []

    while not done:
        while not match:
            if bitString[:i] in nonZeroDict:
                writeBuffer.append(dictionary.index(bitString[:i]))
                match = True
            else:
                i +=1

        bitString = bitString[i:]
        match = False
        i = 1

        if bitString == '':
            done = True

    decompress_name = name[:-4]
    file = open(decompress_name,'wb')
    for i in writeBuffer:
        file.write(bytes([i]))
    file.close()

try:
    mode = sys.argv[1]

except IndexError:
    print("There has been a problem with your input file and/or parameters. For more information, call the program using the --help flag")
    sys.exit(1)

if mode == "--help" or mode == "-h":
    helpmode()
    
elif mode == "--compress" or mode == "-c":
    try:
        fileOrHelp = sys.argv[2]
    except IndexError:
        print("There is a parameter or file name missing. For more information, call the script using the --help or -h option")
        sys.exit(1)

    if fileOrHelp == "--help" or fileOrHelp == "-h":
        print(compress.__doc__)
    else:
        compress(fileOrHelp)

elif mode == "--decompress" or mode == "-d":
    try:
        fileOrHelp = sys.argv[2]
    except IndexError:
        print("There is a parameter or file name missing. For more information, call the script using the --help or -h option")
        sys.exit(1)

    if fileOrHelp == "--help" or fileOrHelp == "-h":
        print(decompress.__doc__)
    else:
        decompress(fileOrHelp)