import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)
cursor = con.cursor()


def translate(w):
    w = w.lower()
    if w in results:
        return results[w]
    elif len(get_close_matches(w, results.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w, results.keys())[0])
        if yn == "Y":
            return results[get_close_matches(w, results.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please check again."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please check again."


word = input("Enter the word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


#if results:
#    for result in results:
#        print(result[1])
#else:
#    print("No word found.")
