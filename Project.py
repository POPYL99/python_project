def vigenere(plainText, key):
    encText = ""
    key_length = len(key)
    for i in range(len(plainText)):
        char = plainText[i]
        if char.isalpha():  #We gust do chars
            keycChar = key[i % key_length].upper()
            shift = ord(keycChar) - ord('A')
            if char.isupper():
                encText += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encText += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            encText += char
    return encText

#It returns the Text to us before encryption
def decrypt(encryptedText, key):
    decryptedText = ""
    key_length = len(key)
    for i in range(len(encryptedText)):
        char = encryptedText[i]
        if char.isalpha():
            keyChar = key[i % key_length].upper()
            shift = ord(keyChar) - ord('A')
            if char.isupper():
                decryptedText += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decryptedText += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            decryptedText += char
    return decryptedText



#function to Creating files based on the length of the text
def file(encText, filename):
    with open(filename, 'w') as file:
        file.write(encText)

#Enter Text and Keys
plainText = input("Enter the text to encrypt: ")
key = input("Enter the key: ")

encryptedText = vigenere(plainText, key)
decryptedText = decrypt(encryptedText, key)

print("\nEncrypted Text: ", encryptedText) #print the text encrypted
print("\nDecrypted Text: ", decryptedText) #print the text afteer encrypted

for i in range(len(plainText)):# for to do files like length of text
    filePath = f"File{i+1}.txt"
    file(encryptedText[:i+1], filePath)
    print(f"char {i+1} saved to {filePath}")

