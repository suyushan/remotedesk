# -*- coding: cp936 -*-
#A Test to Return a AES-File of a Common File

from Crypto.Cipher import AES
from Crypto import Random
import binascii

"""original password:"""
passwd=b'123456'
print 'The original password is',passwd

"""create way of encryption randomly
and ciphertext of original password:"""
key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
"""iv contains the information of way of encryption"""
cipher = AES.new(key, AES.MODE_CFB, iv)
msg = iv + cipher.encrypt(passwd)
"""msg is ciphertext"""
print 'The ciphertext is',binascii.b2a_hex(msg[:])

"""transform the password input into ciphertext
using the same way of encryption:"""
passwd2=b'123456'
print 'The password input is',passwd2
cipher = AES.new(key, AES.MODE_CFB, iv)
msg2 = iv + cipher.encrypt(passwd2)

"""judge whether the password input is the correct one:"""
if msg2 == msg:
    print 'pass certification'
else:
    print 'fail certification'
