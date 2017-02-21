#!/usr/bin/python2.7

# Coded by Arun Kumar Shreevastava 21st Feb 2017
# Hide any file in a PNG file

import struct
import binascii
import sys

args = sys.argv

if(len(sys.argv)<4):
	print 'Usage: %s <input.png> <payload_file> <output.png>' % (args[0])
	sys.exit(0)

png = open(args[1],'rb').read()
custom_header = 'arun'
chunk_data = open(args[2],'rb').read()
i = 8

f = open(args[3],'wb')

#write header
f.write(png[0:i])

while i<len(png):
    bak_len = i
    length,header = struct.unpack('>I4s',png[i:i+8])
    i +=8

    data = png[i:i+length]
    i +=length

    crc = png[i:i+4]
    i +=4

    calc_crc = struct.pack('>I',binascii.crc32(header+data) & 0xffffffff)

    if(header == 'IHDR'):
        chunk_length = struct.pack('>I',len(chunk_data))
        chunk_header = struct.pack('%ds'%(len(custom_header)), custom_header )
        chunk_crc = binascii.crc32(chunk_header+chunk_data) & 0xffffffff
        chunk_crc_hex = struct.pack('>I',chunk_crc)
        f.write(chunk_length + chunk_header +chunk_data +chunk_crc_hex)
        print 'Start: %d Count: %d' % (bak_len+8, len(chunk_data))

    f.write(png[bak_len:i])
    print '[*] Header: %s Length: %d Read_CRC: %s Calc_CRC %s' %(header, length, 
    	binascii.b2a_hex(crc), binascii.b2a_hex(calc_crc))
