# File Compressing
Proposed file compressing script developed as a final assignment for the Information Theory course at the University of Brasilia

## Installation

1. Either obtain the folder with the script `filecompressing.py` + a readme file somehow or clone this repository from GitHub using the following line on your command prompt: ```git clone https://github.com/sofiadsg/file-compressing```
2. The script requires no building, but it is written in Python (works for Python 2 and Python 3). If you wish to use this script and do not have Python installed on your computer, you can see instructions on how to install it on the [Python website](https://www.python.org/downloads/)

## Usage

This script can be used for compressing or decompressing files using Huffman Code. It has three possible modes:

1. Compressing: uses Huffman code to compress a file. Use it with ```python3 filecompressing.py -c [yourfile]```
2. Decompressing: decompresses a .dsg file. Use it with ```python3 filecompressing.py -d [yourfile].dsg```
3. Help: Call ```python3 filecompressing.py -h``` to get information on the script usage
