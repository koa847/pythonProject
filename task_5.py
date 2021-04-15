import random

def get_jokes(count, flag = False):
    """
    Сreates jokes from the given words

    :param count:
    :param flag:
    :return:
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    list_jokes = []
    test = lambda ls, wd: ls.remove(wd) if flag else ls
    while i < count:
        noun = random.choice(nouns)
        test(nouns, noun)
        adverb = random.choice(adverbs)
        test(adverbs, adverb)
        adjective = random.choice(adjectives)
        test(adjectives, adjective)
        joke = ' '.join([noun, adverb, adjective])
        list_jokes.append(joke)
        i += 1
    return list_jokes


print(get_jokes(4))
print(get_jokes(5, True))
print(get_jokes(flag=False, count=5))
