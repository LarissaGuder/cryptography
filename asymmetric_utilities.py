import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import (
   padding, rsa, utils
)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
value_cryp = raw_input()
print value_cryp
prehashed_msg = hashlib.sha256(bytes(value_cryp)).digest()
signature = private_key.sign(
    prehashed_msg,
    padding.PSS(
       mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    utils.Prehashed(hashes.SHA256())
)
public_key = private_key.public_key()
public_key.verify(
    signature,
    prehashed_msg,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    utils.Prehashed(hashes.SHA256())
)