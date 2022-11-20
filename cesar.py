

key=2
phrase='Help me please'

def progress():

    ciphertext = ''
    for i in range(len(phrase)):
        special = phrase[i]
        new_special = special.lower()
        if new_special == " ":
            ciphertext += ' '
        elif special.isalpha():
                ciphertext += chr((ord(new_special) + key - 97) % 26 + 97)
    #print(ciphertext)
    return ciphertext
    

s=progress()
print(s)

def deprogress(ciphertext):

    phrase = ''
    for i in range(len(ciphertext)):
        special = ciphertext[i]
        new_special = special.lower()
        if new_special == " ":
            phrase += ' '
        elif special.isalpha():
                phrase += chr((ord(new_special) - key - 97) % 26 + 97)
    #print(phrase)
    return phrase

phrase2=deprogress(s)
print(phrase2)