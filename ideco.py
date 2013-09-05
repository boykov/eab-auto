import math
import cmath
import sys,os
from numpy import *
set_printoptions(precision=16)

str = 'And no more shall we part.'

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
   return ''.join(chars)

def float_to_binary(num):
    exponent=0
    shifted_num=num
    while shifted_num != int(shifted_num):
        shifted_num*=2
        exponent+=1
    if exponent==0:
        return '{0:0b}'.format(int(shifted_num))
    binary='{0:0{1}b}'.format(int(shifted_num),exponent+1)
    integer_part=binary[:-exponent]
    fractional_part=binary[-exponent:].rstrip('0')
    return '{0}.{1}'.format(integer_part,fractional_part)

a40 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311]

a2 = map(lambda x: list(bin(int(sqrt(x)*10**16))), a40[0:8])

a3 = map(lambda x: list(bin(int(x**(1.0/3)*10**15)))[2:34], a40)

bin(1)
bin(14)

list(float_to_binary(sqrt(19)))

math.frexp(sqrt(2))

def frexp_10(decimal): 
    parts = ("%e" % decimal).split('e') 
    return float(parts[0]), int(parts[1]) 

bstr = tobits(str) + [1] + map(int,list(zeros(239))) + map(int,list(zeros(56))) + map(int,list(bin(len(tobits(str))))[2:11])

len(bstr)


# from zlib import crc32
# salt = None
# i = 0
# while i <= 0xffffffff:
#     if (crc32('away', i & 0xffffffff) & 0xffffffff) == 0xcb2a3b76 and (crc32('molt', i & 0xffffffff) & 0xffffffff) == 0x58d674f6 and (crc32('coat', i & 0xffffffff) & 0xffffffff) == 0x0da77d88:
#         salt = i
#         break
#     if i%1000000 == 0:
#         print i
#     i += 1

# print salt

# print "%X" % (salt,)

# hex(crc32('away', salt & 0xffffffff) & 0xffffffff)
# hex(crc32('molt', salt & 0xffffffff) & 0xffffffff)
# hex(crc32('coat', salt & 0xffffffff) & 0xffffffff)
# hex(crc32('owly', salt & 0xffffffff) & 0xffffffff)
