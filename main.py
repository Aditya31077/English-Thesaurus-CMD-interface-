import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    w=word.title()
    acro=word.capitalize()
    if word in data:
            return data[word] 

    elif w in data:
        return data[w]

    elif acro in data:
        return data[acro]    

    elif len(get_close_matches(word, data.keys()))>0:
        ques=input("Hey did you mean %s instead? Enter Y for Yes and N for No: " % get_close_matches(word,data.keys())[0])
        ques=ques.capitalize()
        if ques == "Y":
            return  data[get_close_matches(word,data.keys())[0]]
        elif ques=="N":
            return "Sorry for the inconvience.I'll try better next time"
        else:
            return "Sorry I did not understand what you wanted to know."    

    else:
       return"The word dosen't exist."
    

word=input("Enter the word: ")

final_word=translate(word)

if type(final_word)==list:
    for item in final_word:
        print(item)
else:
    print(final_word)    
