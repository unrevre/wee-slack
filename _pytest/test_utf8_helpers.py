# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import sys
from collections import OrderedDict
from wee_slack import decode_from_utf8, encode_to_utf8, utf8_decode


b_ae = 'æ'.encode('utf-8')
b_oe = 'ø'.encode('utf-8')
b_aa = 'å'.encode('utf-8')
b_word = b_ae + b_oe + b_aa


def test_decode_should_not_transform_str():
    assert 'æøå' == decode_from_utf8('æøå')

def test_decode_should_not_transform_bytes():
    assert b_word == decode_from_utf8(b_word)

def test_encode_should_not_transform_str():
    assert 'æøå' == encode_to_utf8('æøå')

def test_encode_should_not_transform_bytes():
    assert b_word == encode_to_utf8(b_word)
