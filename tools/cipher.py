#! /usr/bin/env python3

"""
Simple symmetric static encryption and decryption routines for the advent calendar data to prevent snooping.

This is definitely not real encryption, just enough to stop someone right clicking and viewing source for spoilers.
"""

import base64
import sys

def uc_rot13(s):
    """
    Rot13 but only for upper case characters.
    If input s is a bytearray the result will be a bytearray.
    If input s is a string the result will be a string.
    Assumes utf-8.
    """
    result = []
    if isinstance(s, str):
        b = s.encode('utf-8')
    if isinstance(s, bytes):
        b = s
    for c in b:
        if c >= ord('A') and c <= ord('M'):
            result.append(chr(c + 13))
        elif c >= ord('N') and c <= ord('Z'):
            result.append(chr(c + 13 - 26))
        else:
            result.append(chr(c))
    if isinstance(s, str):
        return "".join(result)
    return "".join(result).encode('utf-8')

def encrypt(plain):
    """'encrypt' plain text - return rot13 + base64 encoded version of plain."""
    return uc_rot13(base64.b64encode(plain.encode('utf-8'))).decode('utf-8')

def decrypt(secret):
    """'decrypt'."""
    return base64.b64decode(uc_rot13(secret)).decode('utf-8')

def main():
    """Quick tests for encrypt and decrypt."""
    plain = "3) Edradour 10 - Distillery Edition & 12) Glenfiddich 18"
    cipher = "ZykgEJEyLJEvdKVgZGNgYFORaKA0aJxsMKW5VRIkaKEpb24gWiNxZikgE2xlbmMpMTEpL2ggZGg="
    print("plain:\t\t\t\t", plain)
    print("cipher:\t\t\t\t", cipher)
    print("encrypt(plain):\t\t\t", encrypt(plain))
    assert (encrypt(plain) == cipher), "Encrypted text doesn't match expected cipher text"
    print("encrypt(plain) == cipher:\t", encrypt(plain) == cipher)
    print("decrypt(cipher):\t\t", decrypt(cipher))
    print("decrypt(cipher) == plain:\t", decrypt(cipher) == plain)
    assert (decrypt(cipher) == plain), "Decrypted text doesn't match expected plain text"
    return 0

if __name__ == '__main__':
    sys.exit(main())