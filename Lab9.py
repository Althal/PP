def inc(list1):
    return [list1[x] * 2 for x in range(len(list1))]
    
def iloczyn(ciag):
    ret = 1
    for x in range(len(ciag)):
        ret = ret*ciag[x]
    return ret
    
def palindrom(text):
    text1 = list(filter(str.isalpha, text.lower()))
    return text1 == text1[::-1]
    
def tokenize(text):
    text1 = text.split()
    return text1
	
def remove_stop_words(text):
    with open('C:\Test\W1.txt', encoding='CP1250') as input_file:
        words = input_file.read()        
    words = words.split(', ')
    text = text.lower().split()
    ret = []    
    for x in range(len(text)):
        if len(text[x]) > 2 and not text[x] in words:
            ret.append(text[x])
            
    return ret

def count_most_frequent(text, n):
    text = remove_stop_words(text)
    
    wykaz = {}
    for wyraz in text:
        wykaz[wyraz] = wykaz.get(wyraz, 0)+1
        
    wykaz = sorted(wykaz.items(), key = lambda k:(k[1], k[0]), reverse=True) 
    for x in range(n):
        print(wykaz[x])

def count_most_frequent1(n):
    with open('C:\Test\W2.txt', encoding='UTF-8') as input_file:
        text = input_file.read() 
        
    text = text.replace(',','')
    text =text.replace('.','')
    text = remove_stop_words(text)
    
    wykaz = {}
    for wyraz in text:
        wykaz[wyraz] = wykaz.get(wyraz, 0)+1
        
    wykaz = sorted(wykaz.items(), key = lambda k:(k[1], k[0]), reverse=True) 
    for x in range(n):
        print(wykaz[x])



print("Zadanie 1")
lista = [1,2,3,4]
print(inc(lista))

print("Zadanie 2")
print(iloczyn(lista))

print("Zadanie 3")
print(palindrom('Tolo ma samolot'))

print("Zadanie 4")
print(tokenize('To be, or not to be - that is the question {...}'))

print("Zadanie 5")
print(remove_stop_words('Tolo ma kilka samolotów i to ile ich ma jest tajemnicą'))

print("Zadanie 6")
count_most_frequent('abc abc abc bbc bbc cbb cbb cbb cbb dbb d ebb fbb tbb g y hbb hbb ucc ucc ucc i i i', 3)

print("Zadanie 6a")
count_most_frequent1(3)