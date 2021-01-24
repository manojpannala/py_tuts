def sentence_maker(phrase):
    interrogatives = ("how", "what", "when", "why", "who")
    capitalized = phrase.capitalize()

    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

#print(sentence_maker("how are you"))

#to store the values
results = []

while True:
    user_input = input ("Say something: ")
    if user_input == "stop":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))
