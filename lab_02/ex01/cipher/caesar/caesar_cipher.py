from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, plain: str, key: int):
        len_alphabet = len(self.alphabet)  # 26
        plain_text = plain.upper()
        list_encrypt = []

        for i in plain_text:
            letter = self.alphabet.index(i)
            cipher_index = (letter + key) % len_alphabet
            cipher_text = self.alphabet[cipher_index]
            list_encrypt.append(cipher_text)

        return "".join(list_encrypt)

    def decrypt_text(self, cipher: str, key: int):
        len_alphabet = len(self.alphabet)  # 26
        cipher_text = cipher.upper()
        list_decrypt = []

        for i in cipher_text:
            letter = self.alphabet.index(i)
            cipher_index = (letter - key) % len_alphabet
            plain_text = self.alphabet[cipher_index]
            list_decrypt.append(plain_text)

        return "".join(list_decrypt)
