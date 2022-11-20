alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е','Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ']
phr = list('ЛЕОПАРД НЕ МОЖЕТ ИЗМЕНИТЬ СВОИХ ПЯТЕН')

def vizhener_crypt(text):
    key=[]
    
    ky=input('Введите ключ: ').upper()
    key+=ky[:]
    key+=phr[:]
    print(key)
    crypt=''
    j=0
    for i in text:
        crypt+=alf[(alf.index(key[j%len(key)]) + alf.index(i)) % len(alf)]
        j+=1
    return crypt

def vizhener_decrypt(text):
    key=[]
    
    ky=input('Введите ключ: ').upper()
    key+=ky[:]
    key+=phr[:]
    crypt=''
    j=0
    for i in text:
        crypt+=alf[(alf.index(i) - alf.index(key[j%len(key)])) % len(alf)]
        j+=1
    return crypt

print('ВИЖЕНЕР')
s = vizhener_crypt(phr)
print(s)
print(vizhener_decrypt(s))