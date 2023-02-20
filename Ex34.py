# Задача 34: Ритм есть, если число гласных букв в каждой фразе одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение в программу с клавиатуры. В ответе напишите 
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

inpStr = input('Введите строку со стихом: ').lower()

def is_vovel(letter):   
    vovels = ['а','е','ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    if letter in vovels:
        return True
    else:
        return False

def is_rhytm(inputStr):
    inpStr=inputStr.split()
    listOfVovelCounters = set()

    for i in inpStr:
        counter = 0
        for j in range(0, len(i)):
            if is_vovel(i[j]):
                counter +=1
        listOfVovelCounters.add(counter)
        if(len(listOfVovelCounters) > 1):
            return False
    return True


if(is_rhytm(inpStr)):
    print('Парам пам-пам')
else:
    print('Пам парам')
