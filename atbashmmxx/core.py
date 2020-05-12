class Rotbash:
    def __init__(self, rotate=0):
        if not isinstance(rotate, int):
            rotate = 0
        self._rotate = rotate

    def cipher(self, text=''):
        return ''.join(
            self._cipher_char(char) for char in list(text)
        )

    def _cipher_char(self, char=' '):
        if not char.isalpha():
            return char
        offset = 65 if char < 'a' else 97
        value = ord(char) - offset
        return chr(
            ((25 - (value + self._rotate) % 26) + offset)
        )


class Keybash(Rotbash):
    def __init__(self, key=''):
        self._key = [
            ord(char) - 97 if char.isalpha() else 0 
            for char in list(str(key.lower()))
        ] or [0]
        self._key_len = len(self._key)
        self._key_position = 0
        self._rotate = self._key[0]

    def cipher(self, text=''):
        self._key_position = 0
        return super().cipher(text)

    def _cipher_char(self, char=' '):
        self._rotate = self._key[self._key_position % self._key_len]
        if char.isalpha():
            self._key_position += 1
        return super()._cipher_char(char)
