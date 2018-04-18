from cryptography.fernet import Fernet
import base64

key = Fernet.generate_key()
print key
cipher_suite = Fernet(key)
input_txt = raw_input()
cipher_text = cipher_suite.encrypt(bytes(input_txt))
print cipher_text
plain_text = cipher_suite.decrypt(cipher_text)
print plain_text