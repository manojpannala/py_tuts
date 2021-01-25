import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    # get_close_matches(w, possibilities, n=3, ratio = 0.6)
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:  # recommended matches
        yn = input("Did you mean %s instead? Enter Y if yes or N if no." % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
    else:
        return "The word doesn't exist. Please check again."


word = input("Enter word: ")

print(translate(word))
