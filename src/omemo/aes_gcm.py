# -*- coding: utf-8 -*-
#
# Copyright 2015 Bahtiar `kalkin-` Gadimov <bahtiar@gadimov.de>
#
# This file is part of python-omemo library.
#
# The python-omemo library is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# python-omemo is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# the python-omemo library.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys

from omemo.padding import padding_add
from omemo.padding import padding_remove

try:
    from omemo.aes_gcm_native import aes_decrypt
    from omemo.aes_gcm_native import aes_encrypt
except ImportError:
    from omemo.aes_gcm_fallback import aes_decrypt
    from omemo.aes_gcm_fallback import aes_encrypt


def encrypt(plaintext):
    key = os.urandom(16)
    iv = os.urandom(16)
    encoded_plaintext = padding_add(plaintext).encode('utf-8')
    return key, iv, aes_encrypt(key, iv, encoded_plaintext)


def decrypt(key, iv, ciphertext):
    plaintext = padding_remove(aes_decrypt(key, iv, ciphertext).decode('utf-8'))
    if sys.version_info < (3, 0):
        return unicode(plaintext)
    else:
        return plaintext


class NoValidSessions(Exception):
    pass
