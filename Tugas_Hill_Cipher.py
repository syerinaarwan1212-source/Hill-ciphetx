# ==========================================
# TUGAS KRIPTOGRAFI: HILL CIPHER (KASUS 1 & 2)
# ==========================================

# --- BAGIAN 1: MESIN / RUMUS ---
def char_to_num(char):
    return ord(char.upper()) - ord('A')

def num_to_char(num):
    return chr((num % 26) + ord('A'))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Invers modulo tidak ada (Determinan tidak koprima dengan 26)')
    else:
        return x % m

def hill_cipher_encrypt(plaintext, key_matrix):
    clean_text = ''.join(filter(str.isalpha, plaintext)).upper()
    if len(clean_text) % 2 != 0:
        clean_text += 'X'
    ciphertext = ""
    for i in range(0, len(clean_text), 2):
        p1 = char_to_num(clean_text[i])
        p2 = char_to_num(clean_text[i+1])
        c1 = (key_matrix[0][0] * p1) + (key_matrix[0][1] * p2)
        c2 = (key_matrix[1][0] * p1) + (key_matrix[1][1] * p2)
        ciphertext += num_to_char(c1) + num_to_char(c2)
    return ciphertext

def hill_cipher_decrypt(ciphertext, key_matrix):
    det = (key_matrix[0][0] * key_matrix[1][1]) - (key_matrix[0][1] * key_matrix[1][0])
    det_mod = det % 26
    det_inv = mod_inverse(det_mod, 26)
    
    inv_matrix = [
        [(key_matrix[1][1] * det_inv) % 26, (-key_matrix[0][1] * det_inv) % 26],
        [(-key_matrix[1][0] * det_inv) % 26, (key_matrix[0][0] * det_inv) % 26]
    ]
    
    clean_text = ''.join(filter(str.isalpha, ciphertext)).upper()
    plaintext = ""
    for i in range(0, len(clean_text), 2):
        c1 = char_to_num(clean_text[i])
        c2 = char_to_num(clean_text[i+1])
        p1 = (inv_matrix[0][0] * c1) + (inv_matrix[0][1] * c2)
        p2 = (inv_matrix[1][0] * c1) + (inv_matrix[1][1] * c2)
        plaintext += num_to_char(p1) + num_to_char(p2)
    return plaintext, inv_matrix

# ==========================================
# BAGIAN 2: DATA SOAL & EKSEKUSI
# ==========================================

print("==================================================")
print("           TUGAS HILL CIPHER (1 FILE)             ")
print("==================================================\n")

# ------------------------------------------
# KASUS 1
# ------------------------------------------
print("--- KASUS 1 ---")
plaintext1 = "HILL CIPHER TIDAK SULIT"
key1 = [[5, 6], [2, 3]]

print(f"Plainteks Awal : {plaintext1}")
print(f"Kunci          : {key1}")

# Enkripsi Kasus 1
cipher1 = hill_cipher_encrypt(plaintext1, key1)
print(f"Cipherteks     : {cipher1}")

# Deskripsi Kasus 1
try:
    decrypt1, inv_matrix1 = hill_cipher_decrypt(cipher1, key1)
    print(f"Matriks Invers : {inv_matrix1}")
    print(f"Hasil Dekripsi : {decrypt1}")
except Exception as e:
    print(f"Deskripsi Gagal: {e}")

print("\n--------------------------------------------------\n")

# ------------------------------------------
# KASUS 2
# ------------------------------------------
print("--- KASUS 2 ---")
plaintext2 = "SAYA PUSING"
key2 = [[5, 8], [17, 3]]

print(f"Plainteks Awal : {plaintext2}")
print(f"Kunci          : {key2}")

# Enkripsi Kasus 2
cipher2 = hill_cipher_encrypt(plaintext2, key2)
print(f"Cipherteks     : {cipher2}")

# Deskripsi Kasus 2
try:
    decrypt2, inv_matrix2 = hill_cipher_decrypt(cipher2, key2)
    print(f"Matriks Invers : {inv_matrix2}")
    print(f"Hasil Dekripsi : {decrypt2}")
except Exception as e:
    print(f"\n[ERROR MATEMATIS SAAT DESKRIPSI]")
    print(f"Pesan  : {e}")
    print(f"Alasan : Matriks kunci Kasus 2 tidak memiliki invers modulo 26.")

print("\n==================================================")