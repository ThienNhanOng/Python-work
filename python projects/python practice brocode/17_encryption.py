#this lesson will teach you how to write an encrypted message
# this lesson can be a lesson for intro to cyber security
# this lesson help practice lists, random, 
import random
import string

#this will allow us to use numbers punctuations and english letters
characters = " " + string.punctuation + string.digits + string.ascii_letters
characters = list(characters)
key = characters.copy()

random.shuffle(key)

#this will show the encryption key, characters that are available
#print(characters)
#print(f"characters: {characters}")
print(f"key: {key}")

#encryption message
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = characters.index(letter)
    cipher_text += key [index]
    
print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#decryption message
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += characters [index]

print(f"encrypted message: {cipher_text}") 
print(f"original message: {plain_text}")
