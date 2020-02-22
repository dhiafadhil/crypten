from Crypto.PublicKey import RSA


def PublicAndPrivateKey():
    keyPair = RSA.generate(4096)

    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    with open('public_key.pem', 'wb') as f:
        f.write(pubKeyPEM)

    privKeyPEM = keyPair.exportKey()

    with open('private_key.pem', 'wb') as f:
        f.write(privKeyPEM)