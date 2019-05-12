# Python code to implement a hamming coding algorythm for a hexadecimal string of a known size

def buildProbabilityArray8(name):
    with open(name,"rb") as file:
        d = bytearray(file.read())
    
    probabilityArray = [0]*255

    for i in range(len(d)):
        probabilityArray[d[i]] += 1

    return probabilityArray

def hamming8(name):
    a = buildProbabilityArray8(name)
    print(a)


if __name__ == "__main__":
    hamming8("example.txt")