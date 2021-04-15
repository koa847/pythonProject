def num_translate(en_word):
    num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return num_dict.get(en_word)

def num_translate_adv(en_word):
    num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if en_word.istitle():
        en_word = en_word.lower()
        num = str(num_dict.get(en_word))
        return num.capitalize()
    return num_dict.get(en_word)


word = input("Введите число от одного до десяти: ")
print(num_translate(word))
print(num_translate_adv(word))