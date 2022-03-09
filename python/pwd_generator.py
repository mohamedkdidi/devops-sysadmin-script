#!/usr/bin/env python
# Author: mohamedkdidi@gmail.com 
# Python 2.x
# Simple random password generator.

import string
from random import choice

#input the password length
length = int(input('\nEnter the password length: '))

def randPwd(length, chars):
   return ''.join([choice(chars) for i in range(length)])

#generate the password with lowercase, uppercase, digits and symbols
passwords = randPwd(length, string.letters + string.digits + string.punctuation)

#print the password
print ("Password with %s characters long: %s" % (length, passwords))