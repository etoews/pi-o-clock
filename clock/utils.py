import string


def hyphenate(s):
    assert isinstance(s, unicode)
    no_punc = s.translate(dict.fromkeys(map(ord, string.punctuation)))
    return no_punc.replace(' ', '-').lower()
