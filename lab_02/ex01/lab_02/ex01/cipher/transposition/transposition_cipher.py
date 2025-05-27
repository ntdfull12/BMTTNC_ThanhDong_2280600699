class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        # Tạo một danh sách chứa các chuỗi trống cho các cột
        decrypted_text = [''] * key
        # Tính số lượng ký tự trong mỗi cột
        num_rows = len(text) // key
        num_extra_cells = len(text) % key

        # Các cột có số lượng ký tự khác nhau nếu văn bản không chia hết đều cho key
        column_lengths = [num_rows + 1 if i < num_extra_cells else num_rows for i in range(key)]

        # Chỉ số của ký tự trong văn bản mã hóa
        index = 0
        for col in range(key):
            for row in range(column_lengths[col]):
                decrypted_text[col] += text[index]
                index += 1

        # Ghép các phần tử trong decrypted_text lại thành chuỗi
        # Mỗi cột trong decrypted_text chứa các ký tự, ghép chúng lại thành văn bản giải mã
        decrypted_message = ''
        for row in range(num_rows + (1 if num_extra_cells > 0 else 0)):
            for col in range(key):
                if row < len(decrypted_text[col]):
                    decrypted_message += decrypted_text[col][row]
        
        return decrypted_message