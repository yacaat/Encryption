import hashlib
import sys

alfa = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
p_secret =''
c_secret = []
p2_secret = []
#key = b'Asli'

mode = input('Encrypt or Decrypt\n')
if mode is 'd':
    print('Decrypt mode is activated.')
    c_secret = input('Please share cipher text:')
    key = input('Please share secret key:')
    hash_object = hashlib.sha256(key.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    dec_dig = str(int(hex_dig, 16))
    for j in range(len(c_secret)):
        p2_secret.append(alfa[(alfa.find(c_secret[j]) - int(dec_dig[j])) % 62])
    print(''.join(p2_secret))
    sys.exit()

elif mode is  'e':
    print('Encrypt mode is activated.')
    p_secret = input('Please share plain text:')
    key = input('Please share secret key:')
    hash_object = hashlib.sha256(key.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    dec_dig = str(int(hex_dig, 16))
    for i in range(len(p_secret)):
        c_secret.append(alfa[(alfa.find(p_secret[i]) + int(dec_dig[i])) % 62])
    print(''.join(c_secret))
else:
    print('Script will be terminated due to invalid choice.')
