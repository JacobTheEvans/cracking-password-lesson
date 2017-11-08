from string import digits, ascii_uppercase, ascii_lowercase, punctuation
from itertools import product


def gen_possible_strings_without_punctuation(minLength, maxLength):
    #all possible characters taken from the string lib
    possibleChars = digits + ascii_uppercase + ascii_lowercase
    #the string of all possible characters turned into a list
    charsList = list(possibleChars)

    #the list of all possible passwords
    result = []

    for n in range(minLength, maxLength + 1):
        #product is used to avoid having 5 nested for loops
        #see example https://stackoverflow.com/questions/11095759/itertools-product-return-value
        for comb in product(charsList, repeat=n):
            #append the password as a string
            result.append(''.join(comb))

    return result


print(gen_possible_strings_without_punctuation(1, 5))
