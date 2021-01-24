def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
monday_temp = [9.1, 8.8, 10]


print(mean(student_grades))

def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_input = int(input("Enter the temperature: "))

print(weather_condition(user_input))




