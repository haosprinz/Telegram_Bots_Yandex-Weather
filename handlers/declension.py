import pymorphy2


def declension(text):
    morph = pymorphy2.MorphAnalyzer()
    result = ""
    for i in text.split():
        txt = morph.parse(i)[0]
        inflect = txt.inflect({'loct'})
        result += inflect.word + " "

    return result.capitalize()