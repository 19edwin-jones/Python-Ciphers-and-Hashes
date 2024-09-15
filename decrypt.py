from __init__ import *

class Decrypt:
    def __init__(self, key):
        self.bs = AES.block_size
        self.key = SHA256.new(key.encode()).digest()
    
    def decrypt(self, data, algorithm):
        try:
            iv = SHA256.new(self.key).digest()[:self.bs]
            cipher = algorithm.new(self.key, algorithm.MODE_CBC, iv)
            decryptedData = cipher.decrypt(data)
            try:
                with open('decrypted_file.txt', 'wb') as file:
                    file.write(self._unpad(decryptedData))
            except:
                print("An error occured while decrypting the file")
        
        except Exception:
            print("An error occured while decrypting the file.")
            exit()
            
    @staticmethod
    def _unpad(data):
        return data[:-ord(data[len(data)-1:])]
