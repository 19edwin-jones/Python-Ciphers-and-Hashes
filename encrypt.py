from __init__ import *

class Encrypt(object):
    def __init__(self, key):
        self.bs = AES.block_size
        self.key = SHA256.new(key.encode()).digest()

    def encrypt(self, data,algorithm):
        try:
            paddedData = self._pad(data)
            iv = SHA256.new(self.key).digest()[:self.bs]
            cipher = algorithm.new(self.key, algorithm.MODE_CBC, iv)
            encryptedData = cipher.encrypt(paddedData)
            try:
                with open('encrypted_file', 'wb') as file:
                    file.write(encryptedData)
            except:
                print("An error occured while encrypting the file")
            return encryptedData
        
        except Exception as e:
            print("An error occurred: " + str(e))
            return None
        
    def _pad(self, data):
        return data + (self.bs - len(data) % self.bs) * chr(self.bs - len(data) % self.bs).encode()