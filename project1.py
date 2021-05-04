import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def defination(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0: # to check the list have values in it
        YN = input("Did you mean %s? Enter Y to Yes N to No. " %get_close_matches(word, data.keys())[0])
        if YN == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif YN == "N":
            return "The word does not exist."
        else:
            return "We did not understand your entry."
    else:
        print ("wrong entry.")

print(defination(input("enter your word to search: ")))

