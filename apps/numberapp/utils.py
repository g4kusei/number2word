""" This file contains utility functions """


# Global wariables for change number to word
ones = ["", "one ", "two ", "three ", "four ", "five ",
        "six ", "seven ", "eight ", "nine "]
tens = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ",
        "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
twenties = ["", "", "twenty ", "thirty ", "forty ",
            "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
thousands = ["", "thousand ", "million ", "billion ", "trillion ",
             "quadrillion ", "quintillion ", "sextillion ", "septillion ", "octillion ",
             "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ",
             "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ",
             "octodecillion ", "novemdecillion ", "vigintillion "]


# function to change normal number representation to verbal
def change(number):
    # 1 - change to triple groups
    if number == 0:
        return 'zero'
    else:
        number_triples = []
        numeric_string = str(abs(number))
        for k in range(3, 33, 3):
            r = numeric_string[-k:]
            q = len(numeric_string) - k
            if q < -2:
                break
            else:
                if q >= 0:
                    number_triples.append(int(r[:3]))
                elif q >= -1:
                    number_triples.append(int(r[:2]))
                elif q >= -2:
                    number_triples.append(int(r[:1]))

        # 2 - form string with word representation
        # of number ones, tens, hundreds,
        number_in_words = ""
        for i, x in enumerate(number_triples):
            n1 = x % 10
            n2 = (x % 100) // 10
            n3 = (x % 1000) // 100
            if x == 0:
                continue
            else:
                t = thousands[i]
            if n2 == 0:
                number_in_words = ones[n1] + t + number_in_words
            elif n2 == 1:
                number_in_words = tens[n1] + t + number_in_words
            elif n2 > 1:
                number_in_words = twenties[n2] + ones[n1] + t + number_in_words
            if n3 > 0:
                number_in_words = ones[n3] + "hundred " + number_in_words
        return number_in_words

