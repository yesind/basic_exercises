# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(len([i for i in word.lower() if i in "уеёэоаыяию"]))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
[print(i[0]) for i in sentence.split()]


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
l=[len(i) for i in sentence.split()]
print(sum(l)/len(l))
