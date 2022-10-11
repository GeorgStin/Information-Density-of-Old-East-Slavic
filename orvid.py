# -*- coding: utf-8 -*-


##############################################
# 1. Reading the file
# This function reads the text-file, deletes all "bad" characters
# Input:   Filename (str)
# Output:  List of tokens (list)

def get_text(filename):

    # Read the text file
    str = open(filename, 'r', encoding='utf8').read()

    # List of characters to be removed from the text (numbers, punctuation etc.)
    to_remove = string.digits + string.punctuation + "«»—"

    # List of tokens (lowercase)
    tokens = str.translate(str.maketrans('', '', to_remove)).lower().split()

    return tokens

##############################################
# 2. Syllable separator (rusyllab by Ilja Koziev | https://github.com/Koziev/rusyllab)
# The next part of the code is the simple Python package for breaking Russian words into syllables
# created by Ilja Koziev and distributed under a free, copyleft license.
# The original code was adapted for the old east slavic orthography.

# Split the words in list to contiguous list of syllables and word separators (single space chars)
# Input:   list of words (unicode strings)
# Output:  list of tokens - syllables and spaces

def split_words(words):

    tokens = []
    for word in words:
        sx = split(word)
        if len(tokens) > 0:
            tokens.append(u'START')
        tokens.extend(sx)

    return tokens


def V(c):
    return c in u"АЕЁИОУЫЭЮЯѢаеёиоуыэюяѣъ"  # +Ѣѣъ


def C(c):
    return c in u"БВГДЖЗКЛМНПРСТФХЦЧШЩбвгджзклмнпрстфхцчшщ"


def S(c):
    return c in u"Йй"


def M(c):
    return c in u"Ьь"


def BEG(c):
    return c == u"["


def END(c):
    return c == u"]"


def split(s):
    cur_pos = 0
    items = list(u"[" + s + u"]")
    while cur_pos < len(items):
        input_context = items[cur_pos:]
        res = apply1(input_context)
        if res is None:
            cur_pos += 1
        else:
            items = items[:cur_pos] + res[0] + input_context[res[1]:]
            cur_pos += res[2]
    return items[1:-1]


def apply1(s):
    if C(s[0]):
        if V(s[1]):
            if C(s[2]):
                if V(s[3]):
                    return ([s[0] + s[1], s[2], s[3]], 4, 1)  # SYLLABER_1

                if C(s[3]):
                    if V(s[4]):
                        return ([s[0] + s[1] + s[2], s[3], s[4]], 5, 1)  # SYLLABER_5

                    if C(s[4]):
                        if C(s[5]):
                            if END(s[6]):
                                return ([s[0] + s[1] + s[2] + s[3] + s[4] + s[5], s[6]], 7, 1)  # SYLLABER_11

                            if not END(s[6]):
                                return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5], s[6]], 7, 1)  # SYLLABER_12

                        if V(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3], s[4], s[5]], 6, 1)  # SYLLABER_36

                        if END(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_120

                        if M(s[5]):
                            if END(s[6]):
                                return ([s[0] + s[1] + s[2] + s[3] + s[4] + s[5], s[6]], 7, 1)  # SYLLABER_330

                    if END(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_52

                    if M(s[4]):
                        if END(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_76

                        if C(s[5]):
                            if V(s[6]):
                                return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5], s[6]], 7, 1)  # SYLLABER_250

                        if V(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_260

                if END(s[3]):
                    return ([s[0] + s[1] + s[2], s[3]], 4, 1)  # SYLLABER_6

                if M(s[3]):
                    if C(s[4]):
                        if not END(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3], s[4], s[5]], 6, 1)  # SYLLABER_13

                        if END(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_39

                        if C(s[5]):
                            if C(s[6]):
                                if END(s[7]):
                                    return (
                                    [s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6], s[7]], 8, 1)  # SYLLABER_350

                    if END(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_14

                    if V(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_20

            if END(s[2]):
                return ([s[0] + s[1], s[2]], 3, 1)  # SYLLABER_7

            if S(s[2]):
                if C(s[3]):
                    if V(s[4]):
                        return ([s[0] + s[1] + s[2], s[3], s[4]], 5, 1)  # SYLLABER_8

                    if C(s[4]):
                        if END(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_9

                    if END(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_280

                    if M(s[4]):
                        if END(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_400

                if END(s[3]):
                    return ([s[0] + s[1] + s[2], s[3]], 4, 1)  # SYLLABER_10

                return ([s[0] + s[1] + s[2]], 3, 1)  # SYLLABER_64

            if V(s[2]):
                return ([s[0] + s[1], s[2]], 3, 1)  # SYLLABER_31

        if C(s[1]):
            if C(s[2]):
                if V(s[3]):
                    if C(s[4]):
                        if C(s[5]):
                            if V(s[6]):
                                return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5], s[6]], 7, 1)  # SYLLABER_2

                            if M(s[6]):
                                if END(s[7]):
                                    return (
                                    [s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6], s[7]], 8, 1)  # SYLLABER_310

                        if END(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_3

                        if V(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3], s[4], s[5]], 6, 1)  # SYLLABER_4

                        if M(s[5]):
                            if C(s[6]):
                                if M(s[7]):
                                    if END(s[8]):
                                        return ([s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7], s[8]], 9,
                                                1)  # SYLLABER_300

                            return ([s[0] + s[1] + s[2] + s[3] + s[4] + s[5]], 6, 1)  # SYLLABER_200

                    if S(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3] + s[4]], 5, 1)  # SYLLABER_54

                    if V(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_68

                    if END(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_170

                    return ([s[0] + s[1] + s[2] + s[3]], 4, 1)  # SYLLABER_210

                if C(s[3]):
                    if V(s[4]):
                        if S(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4] + s[5]], 6, 1)  # SYLLABER_220

                        return ([s[0] + s[1] + s[2] + s[3] + s[4]], 5, 1)  # SYLLABER_98

            if V(s[2]):
                if C(s[3]):
                    if C(s[4]):
                        if V(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3], s[4], s[5]], 6, 1)  # SYLLABER_15

                        if C(s[5]):
                            if C(s[6]):
                                if END(s[7]):
                                    return (
                                    [s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6], s[7]], 8, 1)  # SYLLABER_370

                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_80

                        if M(s[5]):
                            if V(s[6]):
                                return ([s[0] + s[1] + s[2] + s[3] + s[4] + s[5], s[6]], 7, 1)  # SYLLABER_340

                            if C(s[6]):
                                if V(s[7]):
                                    return ([s[0] + s[1] + s[2] + s[3] + s[4] + s[5], s[6], s[7]], 8, 1)  # SYLLABER_390

                        if END(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_470

                    if M(s[4]):
                        if not C(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_21

                        if C(s[5]):
                            if V(s[6]):
                                return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5], s[6]], 7, 1)  # SYLLABER_48

                            if C(s[6]):
                                if V(s[7]):
                                    return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5], s[6], s[7]], 8, 1)  # SYLLABER_240

                    if END(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_62

                    if V(s[4]):
                        return ([s[0] + s[1] + s[2], s[3], s[4]], 5, 1)  # SYLLABER_230

                if V(s[3]):
                    if C(s[4]):
                        return ([s[0] + s[1] + s[2], s[3], s[4]], 5, 1)  # SYLLABER_17

                    return ([s[0] + s[1] + s[2], s[3]], 4, 1)  # SYLLABER_82

                if S(s[3]):
                    if END(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_33

                    if C(s[4]):
                        if V(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3], s[4], s[5]], 6, 1)  # SYLLABER_92

                        if C(s[5]):
                            if C(s[6]):
                                if END(s[7]):
                                    return (
                                    [s[0] + s[1] + s[2] + s[3] + s[4] + s[5] + s[6], s[7]], 8, 1)  # SYLLABER_450

                    return ([s[0] + s[1] + s[2] + s[3]], 4, 1)  # SYLLABER_190

                if END(s[3]):
                    return ([s[0] + s[1] + s[2], s[3]], 4, 1)  # SYLLABER_66

            if M(s[2]):
                if V(s[3]):
                    if END(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_410

                    if C(s[4]):
                        if V(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3], s[4], s[5]], 6, 1)  # SYLLABER_480

        if M(s[1]):
            if V(s[2]):
                if C(s[3]):
                    if V(s[4]):
                        return ([s[0] + s[1] + s[2], s[3], s[4]], 5, 1)  # SYLLABER_16

                    if C(s[4]):
                        if END(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_19

                        if V(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3], s[4], s[5]], 6, 1)  # SYLLABER_290

                        if C(s[5]):
                            if C(s[6]):
                                if V(s[7]):
                                    return ([s[0] + s[1] + s[2] + s[3] + s[4] + s[5], s[6], s[7]], 8, 1)  # SYLLABER_430

                    if END(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_22

                if END(s[3]):
                    return ([s[0] + s[1] + s[2], s[3]], 4, 1)  # SYLLABER_94

            if C(s[2]):
                if V(s[3]):
                    if S(s[4]):
                        if END(s[5]):
                            return ([s[0] + s[1] + s[2] + s[3] + s[4], s[5]], 6, 1)  # SYLLABER_320

                    if V(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_360

    if V(s[0]):
        if C(s[1]):
            if C(s[2]):
                if END(s[3]):
                    return ([s[0] + s[1] + s[2], s[3]], 4, 1)  # SYLLABER_18

                if V(s[3]):
                    return ([s[0] + s[1], s[2], s[3]], 4, 1)  # SYLLABER_28

                if C(s[3]):
                    if V(s[4]):
                        if C(s[5]):
                            return ([s[0] + s[1] + s[2], s[3], s[4], s[5]], 6, 1)  # SYLLABER_96

                        return ([s[0] + s[1], s[2], s[3], s[4]], 5, 1)  # SYLLABER_50

                    if C(s[4]):
                        if V(s[5]):
                            return ([s[0] + s[1] + s[2], s[3], s[4], s[5]], 6, 1)  # SYLLABER_460

                if M(s[3]):
                    if END(s[4]):
                        return ([s[0] + s[1] + s[2] + s[3], s[4]], 5, 1)  # SYLLABER_72

            if V(s[2]):
                return ([s[0], s[1], s[2]], 3, 1)  # SYLLABER_35

            if M(s[2]):
                if END(s[3]):
                    return ([s[0] + s[1] + s[2], s[3]], 4, 1)  # SYLLABER_40

                if C(s[3]):
                    if C(s[4]):
                        if V(s[5]):
                            return ([s[0] + s[1] + s[2], s[3], s[4], s[5]], 6, 1)  # SYLLABER_42

                    if V(s[4]):
                        return ([s[0] + s[1] + s[2], s[3], s[4]], 5, 1)  # SYLLABER_84

                if V(s[3]):
                    return ([s[0] + s[1] + s[2], s[3]], 4, 1)  # SYLLABER_78

            if END(s[2]):
                return ([s[0] + s[1], s[2]], 3, 1)  # SYLLABER_44

            return ([s[0] + s[1]], 2, 1)  # SYLLABER_56

        if END(s[1]):
            return ([s[0], s[1]], 2, 1)  # SYLLABER_30

        if V(s[1]):
            return ([s[0], s[1]], 2, 1)  # SYLLABER_34

        if S(s[1]):
            if END(s[2]):
                return ([s[0] + s[1], s[2]], 3, 1)  # SYLLABER_46

            if C(s[2]):
                if V(s[3]):
                    return ([s[0] + s[1], s[2], s[3]], 4, 1)  # SYLLABER_180

    if BEG(s[0]):
        if C(s[1]):
            if C(s[2]):
                if V(s[3]):
                    if C(s[4]):
                        if END(s[5]):
                            return ([s[0], s[1] + s[2] + s[3] + s[4], s[5]], 6, 2)  # SYLLABER_23

                        if C(s[5]):
                            if END(s[6]):
                                return ([s[0], s[1] + s[2] + s[3] + s[4] + s[5], s[6]], 7, 2)  # SYLLABER_60

                            if M(s[6]):
                                if END(s[7]):
                                    return ([s[0], s[1] + s[2] + s[3] + s[4] + s[5] + s[6], s[7]], 8, 2)  # SYLLABER_74

                    if S(s[4]):
                        if END(s[5]):
                            return ([s[0], s[1] + s[2] + s[3] + s[4], s[5]], 6, 2)  # SYLLABER_24

                    if END(s[4]):
                        return ([s[0], s[1] + s[2] + s[3], s[4]], 5, 2)  # SYLLABER_27

                if END(s[3]):
                    return ([s[0], s[1] + s[2], s[3]], 4, 2)  # SYLLABER_70

                if C(s[3]):
                    if C(s[4]):
                        if V(s[5]):
                            if C(s[6]):
                                if END(s[7]):
                                    return ([s[0], s[1] + s[2] + s[3] + s[4] + s[5] + s[6], s[7]], 8, 2)  # SYLLABER_88

                    if V(s[4]):
                        if C(s[5]):
                            if M(s[6]):
                                if END(s[7]):
                                    return ([s[0], s[1] + s[2] + s[3] + s[4] + s[5] + s[6], s[7]], 8, 2)  # SYLLABER_90

                        if END(s[5]):
                            return ([s[0], s[1] + s[2] + s[3] + s[4], s[5]], 6, 2)  # SYLLABER_140

            if V(s[2]):
                if C(s[3]):
                    if C(s[4]):
                        if M(s[5]):
                            if END(s[6]):
                                return ([s[0], s[1] + s[2] + s[3] + s[4] + s[5], s[6]], 7, 2)  # SYLLABER_26

                        if END(s[5]):
                            return ([s[0], s[1] + s[2] + s[3] + s[4], s[5]], 6, 2)  # SYLLABER_37

                    if M(s[4]):
                        if C(s[5]):
                            if C(s[6]):
                                if END(s[7]):
                                    return ([s[0], s[1] + s[2] + s[3] + s[4] + s[5] + s[6], s[7]], 8, 2)  # SYLLABER_440

                if S(s[3]):
                    if C(s[4]):
                        if END(s[5]):
                            return ([s[0], s[1] + s[2] + s[3] + s[4], s[5]], 6, 2)  # SYLLABER_160

            if END(s[2]):
                return ([s[0], s[1], s[2]], 3, 2)  # SYLLABER_32

            if M(s[2]):
                if C(s[3]):
                    if V(s[4]):
                        if END(s[5]):
                            return ([s[0], s[1] + s[2] + s[3] + s[4], s[5]], 6, 2)  # SYLLABER_58

                        if C(s[5]):
                            if END(s[6]):
                                return ([s[0], s[1] + s[2] + s[3] + s[4] + s[5], s[6]], 7, 2)  # SYLLABER_100

                            if V(s[6]):
                                return ([s[0], s[1] + s[2] + s[3] + s[4], s[5], s[6]], 7, 2)  # SYLLABER_420

                if V(s[3]):
                    if END(s[4]):
                        return ([s[0], s[1] + s[2] + s[3], s[4]], 5, 2)  # SYLLABER_86

                    if S(s[4]):
                        if END(s[5]):
                            return ([s[0], s[1] + s[2] + s[3] + s[4], s[5]], 6, 2)  # SYLLABER_110

                    if C(s[4]):
                        if M(s[5]):
                            if END(s[6]):
                                return ([s[0], s[1] + s[2] + s[3] + s[4] + s[5], s[6]], 7, 2)  # SYLLABER_150

        if V(s[1]):
            if C(s[2]):
                if M(s[3]):
                    if END(s[4]):
                        return ([s[0], s[1] + s[2] + s[3], s[4]], 5, 2)  # SYLLABER_25

                if END(s[3]):
                    return ([s[0], s[1] + s[2], s[3]], 4, 2)  # SYLLABER_29

                if C(s[3]):
                    if C(s[4]):
                        if C(s[5]):
                            if END(s[6]):
                                return ([s[0], s[1] + s[2] + s[3] + s[4] + s[5], s[6]], 7, 2)  # SYLLABER_130

        if S(s[1]):
            if V(s[2]):
                if C(s[3]):
                    if V(s[4]):
                        return ([s[0], s[1] + s[2], s[3], s[4]], 5, 2)  # SYLLABER_380


##############################################
# 3. Getting ngrams
# This function creates dictionaries with ngrams and their frequencies
# Input:   List of tokens (syllables and spaces between words)
# Output:  Unigrams (dict) {unigram: count}
#          Bigrams (dict) {bigram: count}

def get_ngrams(padded_syllables):

    # Unigrams
    unigrams = dict()

    for i in range(len(padded_syllables)):
        unigram = padded_syllables[i]

        unigrams[unigram] = unigrams.get(unigram, 0) + 1

    # Bigrams
    bigrams = dict()

    for i in range(len(padded_syllables) - 1):

        bigram = (padded_syllables[i], padded_syllables[i + 1])

        # "START" is a null marker for syllables occurring word initially
        # in this way we exclude the bigrams where the null marker stands at the end
        if bigram[1] != "START":
            bigrams[bigram] = bigrams.get(bigram, 0) + 1

    return unigrams, bigrams


##############################################
# 4. ShE (Shannon Entropy)
# This function calculates he standard Shannon entropy of texts
# entropy = -sum of p(x) * log2(p(x))
# Input:   Unigrams (dict) {unigram: count}
# Output:  Shannon Entropy (float)

def get_she(unigrams):

    entropy = 0.0

    # Total amount of all unigrams in the text
    unigrams_sum = sum(unigrams.values())

    for unigram in unigrams:

        # Total amount of certain unigram
        count_unigram = unigrams[unigram]

        if count_unigram > 0:
            # Relative freq of unigram (p(x))
            rel_unigram_freq = count_unigram / unigrams_sum

            # Entropy = -sum of p(x) * log2(p(x))
            entropy = entropy + (rel_unigram_freq * math.log(rel_unigram_freq, 2))

    return -entropy


##############################################
# 5. ID (Information Density)
# This function calculates the Information Density of texts
# ID = -sum of p(x,y) * log2 (p(x,y) / p(x))
# Input:   Unigrams (dict), Bigrams (dict)
# Output:  Information Density (float)

def get_id(unigrams, bigrams):

    ID = 0.0

    # Total amount of all unigrams in the text
    unigrams_sum = sum(unigrams.values())

    for bigram in bigrams:

        # Total amount of certain n-grams
        count_bigram = bigrams[bigram]  # (x,y)
        count_unigram = unigrams[bigram[0]]  # (x)

        if count_bigram > 0:
            # Relative freqs of n-grams
            rel_bigram_freq = count_bigram / count_unigram
            rel_unigram_freq = count_unigram / unigrams_sum

            # ID = -sum of p(x,y) * log (p(x,y) / p(x))
            ID = ID + (rel_bigram_freq * math.log((rel_bigram_freq / rel_unigram_freq), 2))

    return -ID


##############################################
# Function that calls all other functions

def run_script(filename):

    # 1. Reading the file
    tokens = get_text(filename)

    # 2. Separating to the syllables
    syllables = split_words(tokens)
    # Add START-token for the first word
    syllables.insert(0, 'START')

    # 3. Getting uni- and bigrams
    unigrams, bigrams = get_ngrams(syllables)

    # Create a dict with unigrams but without START-tokens
    unigrams_without_padding = unigrams.copy()
    del unigrams_without_padding['START']

    # 4. ShE (Shannon Entropy)
    ShE = get_she(unigrams_without_padding)

    # 5. ID (Information Density)
    ID = abs(get_id(unigrams, bigrams))

    ########## RESULTS ##########

    # Length of the text (in syllables)
    length = len(syllables)

    # Average bigram ID in the text
    avg_id = ID / len(bigrams)

    # Dict for all unigrams from the whole corpus
    global global_unigrams
    global_unigrams = Counter(global_unigrams) + Counter(unigrams)

    # Dict for all bigrams from the whole corpus
    global global_bigrams
    global_bigrams = Counter(global_bigrams) + Counter(bigrams)

    # Print results: Filename, length, ShE, ID, average ID)
    if text.endswith('.txt'):
        print(str(filename), length, ShE, ID, avg_id, sep='\t')

    else:
        print(str(file_name), length, ShE, ID, avg_id, sep='\t')


###########################################################
# Main program
###########################################################

if __name__ == "__main__":

    import string
    import math
    import os
    import sys
    from collections import Counter

    # SELECT YOUR TEXT OR FOLDER for calculating
    # e.g 'Corpus' for the whole folder with many texts
    # or 'test.txt' for the one text only
    text = 'Corpus'

    # Dicts for collecting of ngrams from all texts
    global_unigrams = Counter()
    global_bigrams = Counter()

    # Saving option (creates txt-file with results)
    # otherwise the results are output to the console
    save = input('Do you want save the results? (y/n)\n')

    if save == 'y':
        stdoutOrigin = sys.stdout
        sys.stdout = open("results.txt", "w")

    # Headline
    print('Filename', 'length (syl)', 'ShE', 'ID', 'average ID', sep='\t')

    # Function for one text only
    if text.endswith('.txt'):
        run_script(text)

    # Function for whole corpus/folder
    else:
        for root, directories, files in os.walk(text):
            for file_name in files:
                text_location = root + '/' + file_name
                if text_location.endswith('.txt'):
                    run_script(text_location)

        # Results for whole corpus
        global_she = get_she(global_unigrams)  # ShE of the corpus
        global_id = abs(get_id(global_unigrams, global_bigrams))  # ID of the corpus
        global_avg_id = global_id / sum(global_bigrams.values())  # avg ID of the corpus
        print('\nCorpus ShE:', global_she,
              '\nCorpus ID:', global_id,
              '\nCorpus average ID:', global_avg_id)

else:
    print("Script can only run as a stand-alone.")
