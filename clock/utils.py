import string


def hyphenate(s):
    no_punc = s.translate(string.maketrans("", ""), string.punctuation)
    return no_punc.replace(' ', '-').lower()
