import sys

#TODO: hamming code maker
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
        -sc or --supercompress
        -sd or --superdecompress
        -s or --stats
    To know what each mode does, call the script with the parameter on help mode

    The file can be either on the home folder or on the same folder as the script
    If you want to call it from elsewhere, use the path relative to one of these two.

    Additional info can be found on GitHub at https://github.com/sofiadsg/file-compressing
    '''
    print(helpmode.__doc__)

def compress(filename):
    """
    This function uses Huffman code to compress a given file and saves the compressed result with the extension .dsg.
    """
    return 0

def decompress(filename):
    """
    This function decompresses a .dsg file.
    """
    return 0

def supercompress(filename):
    """
    This function uses composed words to better compress a given file, without information loss. 
    The supercompressed file is saved with the flag .sdsg
    """
    return 0

def superdecompress(filename):
    """
    This function decompresses a .sdsg file
    """
    return 0

def stats():
    """
    Run on this mode to get some stats on your file
    """
    return 0

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
        raise NotImplementedError
        sys.exit(1)

elif mode == "--decompress" or mode == "-d":
    try:
        fileOrHelp = sys.argv[2]
    except IndexError:
        print("There is a parameter or file name missing. For more information, call the script using the --help or -h option")
        sys.exit(1)

    if fileOrHelp == "--help" or fileOrHelp == "-h":
        print(decompress.__doc__)
    else:
        raise NotImplementedError
        sys.exit(1)

elif mode == "--supercompress" or mode == "-sc":
    try:
        fileOrHelp = sys.argv[2]
    except IndexError:
        print("There is a parameter or file name missing. For more information, call the script using the --help or -h option")
        sys.exit(1)

    if fileOrHelp == "--help" or fileOrHelp == "-h":
        print(supercompress.__doc__)
    else:
        raise NotImplementedError
        sys.exit(1)

elif mode == "--superdecompress" or mode == "-sd":
    try:
        fileOrHelp = sys.argv[2]
    except IndexError:
        print("There is a parameter or file name missing. For more information, call the script using the --help or -h option")
        sys.exit(1)

    if fileOrHelp == "--help" or fileOrHelp == "-h":
        print(superdecompress.__doc__)
    else:
        raise NotImplementedError
        sys.exit(1)

elif mode == "--stats" or mode == "-s":
    try:
        fileOrHelp = sys.argv[2]
    except IndexError:
        print("There is a parameter or file name missing. For more information, call the script using the --help or -h option")
        sys.exit(1)

    if fileOrHelp == "--help" or fileOrHelp == "-h":
        print(stats.__doc__)
    else:
        raise NotImplementedError
        sys.exit(1)