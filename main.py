from __init__ import *
from decrypt import Decrypt
from encrypt import Encrypt


def setDirectory():
    directory = str(input("Enter the directory with the file to encrypt: "))
    
    if directory == '': # Blank input, use CWD
        CWD = os.getcwd()
        print(f"\nCurrent working directory: \n{CWD}")
        return CWD

    # Not using CWD
    DIR = os.path.expanduser(directory) # Expand ~ to home directory
    if os.path.isdir(DIR):
        print(f"\nHome directory: \n{DIR}")
        return DIR
    else:
        print("Invalid directory.")
        exit()


def getFile(directory):
    try:
        filePath = os.path.join(directory, str(input("Enter the file name including '.txt': ")))
        with open(filePath, 'rb') as file:
            data = file.read()
            return data

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("An error occurred: " + str(e))
        exit()


def askForCipher():
    print("""
Symmetric ciphers:
    1. AES-256
    --- The following are not implemented yet ---
    --- Selecting them will default to AES! ---
    2. Single DES (legacy)
    3. Triple DES (legacy)
    4. CAST-128 (legacy)
    5. RC2 (legacy)
    """)
    algorithm = str(input("Enter the the cipher algorithm you want to use: "))
    return setAlgorithm('c'+algorithm)


def askForHash():
    print("""
Cryptographic hashes
    1. SHA1-160
    2. SHA2-224
    3. SHA2-256
    4. SHA2-384
    5. SHA2-512
    6. SHA3-224
    7. SHA3-256
    8. SHA3-384
    9. SHA3-512
    0. MD5
    """)
    algorithm = str(input("Enter the the cipher algorithm you want to use: "))
    return setAlgorithm('h'+algorithm)


def setAlgorithm(algorithm):
    try:
        if algorithm[0] == 'c':
            cipherChoice = int(algorithm[1])
            try:
                if cipherChoice in ALL_CIPHERS:
                    print("You have selected " + ALL_CIPHERS[cipherChoice][0] + ".")
                    if ALL_CIPHERS[cipherChoice][0] != "AES":
                        print("This cipher is not implemented yet. \nDefaulting to AES.")
                    return ALL_CIPHERS[1][1] # Default to AES
            except ValueError:
                print("Invalid input. Please enter a valid code.")
                askForCipher()
        elif algorithm[0] == 'h':
            hashChoice = int(algorithm[1])
            try:
                if hashChoice in ALL_HASHES:
                    print("You have selected " + ALL_HASHES[hashChoice][0] + ".")
                    return ALL_HASHES[hashChoice][1]
            except ValueError:
                print("Invalid input. Please enter a valid code.")
                askForHash()
    except Exception as e:
        print("An error occurred: " + str(e))
        exit()


def main():
    print("Only text files are supported at the moment.")
    print("Only AES is supported at the moment.")
    print("Only SHA-2 and SHA-3 are supported at the moment.\n")
    print(f'{"-"*60}')
    print(f"{"*"*15}  HASHES CANNOT BE DECRYPTED  {"*"*15}")
    print("Once you hash data, you cannot get the original data back")
    print(f'{"-"*60}')


    transform = str(input("""
Select type of transformation:
    [C]ipher (encrypt or decrypt data)
    [H]ash (hash data)

    [Q]uit

    Please select an option:
    """)).lower()

    if transform == 'q':
        print("Exiting...")
        time.sleep(1)
        exit()
    elif transform not in ['c', 'h']:
        print("Invalid input. Please enter a valid code.")
        main()
    else:
        try:
            if transform == 'c':
                algorithm = askForCipher()
            elif transform == 'h':
                algorithm = askForHash()
        except ValueError:
            print("An error occurred. Please try again.")


    if transform == 'c' and algorithm not in ALL_HASHES.values(): # Encrypt or decrypt file
        directory = setDirectory()
        data = getFile(directory)
        tranformation = str(input("Encrypt or decrypt [e/d]: ")).lower()

        if tranformation == 'e': # Encrypt
            print("Encrypting...")
            key = str(input("Enter the key: "))
            Encrypt(key).encrypt(data, algorithm)

        elif tranformation == 'd': # Decrypt
            print("Decrypting...")
            key = str(input("Enter the key: "))
            Decrypt(key).decrypt(data, algorithm)\

    elif transform == 'h' and algorithm not in ALL_HASHES.values(): # Hash data
        directory = setDirectory()
        data = getFile(directory)
        print("Hashing...")
        hash = algorithm.new(data) # type: ignore
        print(f"Hash: {hash.hexdigest()}")

if __name__ == '__main__':
    main()