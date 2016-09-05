import string


def hyphenate(s):
    no_punc = s.translate(dict.fromkeys(map(ord, string.punctuation)))
    return no_punc.replace(' ', '-').lower()
