import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    #word=word.lower()
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s instead? Press Y if Yes or N if No : "%get_close_matches(word,data.keys())[0])
        if yn=="Y" or yn=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N" or yn=="n":
            return "Word doesn't exist. Please double check!"
        else:
            return "We doesn't understand your entry. Please Check!"

    else:
        return "Word doesn't exist. Please double check!"

word=input("Enter a word: ")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
