import random
import unittest
from atbashmmxx.core import Rotbash, Keybash


TEXT = 'Hello! This is a test for Atbash-MMXX.'


class TestStringMethods(unittest.TestCase):
    def test_rotbash(self):
        key = _rand_key_int()
        rb = Rotbash(key)
        rb_cipher = rb.cipher(TEXT)
        rb_output = rb.cipher(rb_cipher)
        self.assertEqual(rb_output, TEXT, 'KEY: ' + str(key))

    def test_keybash(self):
        key = _rand_key_string()
        kb = Keybash(key)
        kb_cipher = kb.cipher(TEXT)
        kb_output = kb.cipher(kb_cipher)
        self.assertEqual(kb_output, TEXT, 'KEY: ' + key)


def _rand_key_int():
    return random.randint(0, 25)


def _rand_key_string(length=6):
    return ''.join([chr(random.randint(97, 122)) for i in range(length)])


if __name__ == '__main__':
    unittest.main()
