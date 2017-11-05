from edit_distance import edit_distance

def soundex(name):
    length = 4
    digits = '01230120022455012623010202'
    sndx = ''
    fc = ''

    for c in name.upper():
        if c.isalpha():
            if not fc: fc = c
            d = digits[ord(c)-ord('A')]
            if not sndx or (d != sndx[-1]):
                sndx += d

    sndx = fc + sndx[1:]

    sndx = sndx.replace('0','')

    return (sndx + ('0' * length))[:length]

def ngrams(n, string):
    ngrams = set()
    start = 0
    end = start + n
    while end <= len(string):
        ngrams.add(soundex(string[start:end]))
        start+=1
        end+=1
    return ngrams

#jaccard coefficient for n-grams of two words
def jaccard_and_intersection(n, string1, string2):
    ngram1 = ngrams(n, string1)
    ngram2 = ngrams(n, string2)

    intersection_size = len(ngram1 & ngram2)
    union_size = len(ngram1 | ngram2)

    print 'INTERSECTION', intersection_size

    return (intersection_size / float(union_size), intersection_size)


if __name__ == '__main__':
    print jaccard(3, "house", "houser")
    # 0.75

    print jaccard(3, "intersection", "intention")
    # 0.307
