"""

"""
import re
import argparse
import pyperclip
import string

parser = argparse.ArgumentParser()
parser.add_argument('-d', action='store_true', help='space delimiter flag')
parser.add_argument('program', help='The program you want to run b2a or a2b')
parser.add_argument('data', help='The data to be converted')
args = parser.parse_args()

def ascii2bin(stringg):
    binary = ''
    print(stringg)
    for i in stringg:
        converted = bin(ord(i))
        if i in string.punctuation or i in string.whitespace:
            binary += '00' + converted[2:]
        else:
            binary += '0' + converted[2:]
        print(converted)
    if args.d is True:
        return ' '.join(re.findall('........', binary))
    else:
        return binary

def bin2ascii(binary):
    binary = binary.replace(" ", "")
    asciitxt = ''
    processed = ' '.join(re.findall('........', binary))
    processed = processed.split(' ')
    for byte in processed:
        asciitxt += chr(int(byte, 2))
    return asciitxt

print('='*16)
print('BINARY CONVERTER')
print('='*16)
print(' ')
if args.program == 'b2a':
    result = bin2ascii(args.data)
    print('You are converting from BINARY to ASCII.')
    print(' ')
    print('Binary: ' + args.data + ' ---> ASCII: ' + result)
    print('Result: ' + result)
    pyperclip.copy(result)
else:
    result = ascii2bin(args.data)
    print('You are converting from ASCII to BINARY.')
    print(' ')
    print('ASCII: ' + args.data + ' ---> BINARY: ' + result)
    print('Result: ' + result)
    pyperclip.copy(result)
print(' ')
print('The conversion has been copied to your clipboard.')
