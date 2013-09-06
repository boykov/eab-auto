import math
import cmath
import sys,os
import BitVector
from numpy import *
set_printoptions(precision=16)

init_str = 'And no more shall we part.'

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
    
def frexp_10(decimal): 
    parts = ("%e" % decimal).split('e') 
    return float(parts[0]), int(parts[1]) 

a40 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311]

a2 = map(lambda x: list(float_to_binary(frexp(x**(1.0/2))[0])[2:34]), a40[0:8])
a3 = map(lambda x: list(float_to_binary(frexp(x**(1.0/3))[0])[2:34]), a40)

math.frexp(sqrt(19))
float_to_binary(frexp(sqrt(19))[0])[2:34]

bstr = tobits(init_str) + [1] + map(int,list(zeros(239))) + map(int,list(zeros(56))) + map(int,list(bin(len(tobits(init_str))))[2:10])

h = map(lambda x: BitVector.BitVector(bitlist = map(int,x)), a2)
k = map(lambda x: BitVector.BitVector(bitlist = map(int,x)), a3)
f = map(lambda x: BitVector.BitVector(bitlist = map(lambda x: 0,x)), a2)

w = map(lambda x: BitVector.BitVector(bitlist = map(lambda x: 0,x)), a3)

for i in range(16):
    w[i] = BitVector.BitVector(bitlist = bstr[i*32:(i+1)*32])

def create_bitstring(string):
    return '00000000000000000000000000000000'[len(string):] + string

def bitsum(*args):
    s = 0
    for a in args:
        s = s + int(str(a),2)
    return bin(s % 4294967296)[2:]
    
for i in range(16,64):
    s0 = w[i-15].deep_copy().__rshift__(7)
    s1 = w[i-15].deep_copy().__rshift__(18)
    s2 = w[i-15].deep_copy().shift_right(3)
    s3 = w[i-2].deep_copy().__rshift__(17)
    s4 = w[i-2].deep_copy().__rshift__(19)
    s5 = w[i-2].deep_copy().shift_right(10)
    s6 = s0.__xor__(s1).__xor__(s2)
    s7 = s3.__xor__(s4).__xor__(s5)
    w[i] = BitVector.BitVector(bitstring = create_bitstring(bitsum(w[i-16],s6,w[i-7],s7)))

for i in range(8):
    f[i] = h[i]

for i in range(0,64):
    s0 = f[0].deep_copy().__rshift__(2)
    s1 = f[0].deep_copy().__rshift__(13)
    s2 = f[0].deep_copy().__rshift__(22)
    s3 = f[0].__and__(f[1])
    s4 = f[0].__and__(f[2])
    s5 = f[1].__and__(f[2])
    s6 = f[4].deep_copy().__rshift__(6)
    s7 = f[4].deep_copy().__rshift__(11)
    s8 = f[4].deep_copy().__rshift__(25)
    s9 = f[4].__and__(f[5])
    s10 = f[4].__invert__()
    s11 = s10.__and__(f[6])
    s12 = s0.__xor__(s1).__xor__(s2)
    s13 = s3.__xor__(s4).__xor__(s5)
    s14 = s6.__xor__(s7).__xor__(s8)
    s15 = s9.__xor__(s11)
    s16 = BitVector.BitVector(bitstring = create_bitstring(bitsum(s12,s13)))
    s17 = BitVector.BitVector(bitstring = create_bitstring(bitsum(f[7],s14,s15,k[i],w[i])))
    f[7] = f[6]
    f[6] = f[5]
    f[5] = f[4]
    f[4] = BitVector.BitVector(bitstring = create_bitstring(bitsum(f[3],s17)))
    f[3] = f[2]
    f[2] = f[1]
    f[1] = f[0]
    f[0] = BitVector.BitVector(bitstring = create_bitstring(bitsum(s16,s17)))

for i in range(8):    
    h[i] = BitVector.BitVector(bitstring = create_bitstring(bitsum(h[i],f[i])))

print ''.join(map(lambda x: hex(int(str(x),2))[2:], h))

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
