#Палиндром

'''
stringForCheck = input('Input your text:')
strObject = ''
symbols = [',', ' ', '.',';', '!']
stringWithoutSymbol = ''

def buildInStr(object): #Преобразует список в строку
    global strObject
    if (type(object)==list):
        for i in object:
            strObject += i
        return strObject
def reverse(text): #Обратный порядок строки
    return text[::-1]
def is_palindrome(text): #проверка на палиндром
    return text == reverse(text)

for symbol in symbols: #Проверка есть ли в строке знаки препинания и изъятие их из строки
    if symbol in stringForCheck:
        strObject = ''
        stringForCheck = stringForCheck.split(symbol)
        stringWithoutSymbol = buildInStr(stringForCheck)
        stringForCheck = stringWithoutSymbol
    else:
        stringWithoutSymbol = stringForCheck

if (is_palindrome(stringWithoutSymbol.lower())):
    print("{0} - Yes, It's palindrome.".format(stringWithoutSymbol))
else:
    print("{0} - No, isn't palindrome.".format(stringWithoutSymbol))
'''  

#Second method

stringForCheck = input('Input your text:')
symbols = [',', ' ', '.',';', '!']

def reverse(text): #Обратный порядок строки
    return text[::-1]
def is_palindrome(text): #проверка на палиндром
    return text == reverse(text)

for symbol in symbols: #Проверка есть ли в строке знаки препинания и изъятие их из строки
    if symbol in stringForCheck:
        stringForCheck = stringForCheck.replace(symbol, '')

if (is_palindrome(stringForCheck.lower())):
    print("{0} - Yes, It's palindrome.".format(stringForCheck))
else:
    print("{0} - No, isn't palindrome.".format(stringForCheck))
