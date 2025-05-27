from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher




app = Flask(__name__)
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher() 
playfair_cipher = PlayFairCipher() 
transposition_cipher = TranspositionCipher()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar", methods=["GET"])
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return render_template('caesar.html', encrypted=encrypted_text)

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return render_template('caesar.html', decrypted=decrypted_text)
# Vigenere Cipher
@app.route("/vigenere", methods=["GET"])
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt_vigenere", methods=["POST"])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)
    return render_template('vigenere.html', encrypted=encrypted_text)

@app.route("/decrypt_vigenere", methods=["POST"])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)
    return render_template('vigenere.html', decrypted=decrypted_text)


#RAIl FENCE
# --- RAILFENCE ---
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/encrypt_railfence", methods=["POST"])
def encrypt_railfence():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted = railfence_cipher.rail_fence_encrypt(text, key)
    return render_template("railfence.html", encrypted=encrypted)

@app.route("/decrypt_railfence", methods=["POST"])
def decrypt_railfence():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted = railfence_cipher.rail_fence_decrypt(text, key)
    return render_template("railfence.html", decrypted=decrypted)

# Play

@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/encrypt_playfair", methods=["POST"])
def encrypt_playfair():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted = playfair_cipher.playfair_encrypt(text, matrix)
    return render_template("playfair.html", encrypted=encrypted)

@app.route("/decrypt_playfair", methods=["POST"])
def decrypt_playfair():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted = playfair_cipher.playfair_decrypt(text, matrix)
    return render_template("playfair.html", decrypted=decrypted)


#TRAN   
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

@app.route("/encrypt_transposition", methods=["POST"])
def encrypt_transposition():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted = transposition_cipher.encrypt(text, key)
    return render_template("transposition.html", encrypted=encrypted)

@app.route("/decrypt_transposition", methods=["POST"])
def decrypt_transposition():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted = transposition_cipher.decrypt(text, key)
    return render_template("transposition.html", decrypted=decrypted)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
