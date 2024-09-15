import base64
from Crypto import Random
from Crypto.Hash import SHA1, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512, MD5
from Crypto.Cipher import AES, DES, DES3, CAST
import os, time

ALL_CIPHERS = {
        1: ['AES', AES],
        2: ['DES', DES],
        3: ['3DES', DES3],
        4: ['CAST-128', CAST]
}

ALL_HASHES = {
        1: ['SHA2-160', SHA1],
        2: ['SHA2-224', SHA224],
        3: ['SHA2-256', SHA256],
        4: ['SHA2-384', SHA384],
        5: ['SHA2-512', SHA512],
        6: ['SHA3-224', SHA3_224],
        7: ['SHA3-256', SHA3_256],
        8: ['SHA3-384', SHA3_384],
        9: ['SHA3-512', SHA3_512],
        0: ['MD5', MD5]
}