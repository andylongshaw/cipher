import unittest


class MyTestCase(unittest.TestCase):
    def test_encrypt_single_rotator(self):
        plaintext = 'Stable'
        rotator = 1
        ciphertext = 'Tubcmf'

        encrypted = encrypt(plaintext, rotator)

        self.assertEqual(encrypted, ciphertext)

    def test_encrypt_double_rotator(self):
        plaintext = 'Stable'
        rotator = 2
        ciphertext = 'Uvcdng'

        encrypted = encrypt(plaintext, rotator)

        self.assertEqual(encrypted, ciphertext)

    def test_decrypt(self):
        plaintext = 'Stable'
        rotator = 2
        ciphertext = 'Uvcdng'

        decrypted = decrypt(ciphertext, rotator)

        self.assertEqual(decrypted, plaintext)

    def test_crack_without_rotator_2(self):
        plaintext = 'Stable'
        rotator = 2
        ciphertext = 'Uvcdng'

        derived_rotator, derived_plaintext = determine_rotator(ciphertext)

        self.assertEqual(derived_rotator, rotator)
        self.assertEqual(derived_plaintext, plaintext)

    def test_crack_without_rotator_1(self):
        plaintext = 'Stable'
        rotator = 1
        ciphertext = 'Tubcmf'

        derived_rotator, derived_plaintext = determine_rotator(ciphertext)

        self.assertEqual(derived_rotator, rotator)
        self.assertEqual(derived_plaintext, plaintext)

    def test_encrypt_Theresa(self):
        plaintext = 'Strong and Stable'
        rotator = 1
        ciphertext = 'Tuspoh boe Tubcmf'

        encrypted = encrypt(plaintext, rotator)

        self.assertEqual(encrypted, ciphertext)

    def test_crack_Theresa_1(self):
        plaintext = 'Strong and Stable'
        rotator = 1
        ciphertext = 'Tuspoh boe Tubcmf'

        derived_rotator, derived_plaintext = determine_rotator(ciphertext)

        self.assertEqual(derived_rotator, rotator)
        self.assertEqual(derived_plaintext, plaintext)


def determine_rotator(ciphertext):

    for rotator in range(1,3):
        if determine_rotator_recurse(ciphertext.split(), rotator):
            return rotator, decrypt(ciphertext, rotator)

    raise LookupError('Could not find match')

def determine_rotator_recurse(word_list, rotator):
    if not word_list:
        return True

    file = open("wordlist.txt", 'r')
    wordlist = file.readlines().map()
    first, rest = word_list[0], word_list[1:]

    possible_plaintext = decrypt(first, rotator)
    if possible_plaintext in wordlist:
        return determine_rotator_recurse(rest, rotator)
    else:
        return False


def decrypt(ciphertext, rotator):
    decrypted = ''

    for c in ciphertext:
        decrypted = decrypted + lookup(c, -rotator)

    return decrypted


def encrypt(plaintext, rotator):
    encrypted = ''

    for c in plaintext:
        encrypted = encrypted + lookup(c, rotator)

    return encrypted


def lookup(c, rotator):
    characters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'S', 'T', 'U']

    if c in characters:
        index = characters.index(c)
        index = index + rotator
        return characters[index]
    return c


if __name__ == '__main__':
    unittest.main()
