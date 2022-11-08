# ########### CODING EXERCISE ##########
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# sentence_list = sentence.split()
# sentence_count = {word: len(word) for word in sentence_list}
#
# print(sentence_count)

# ############### CODING EXERCISE ##################
# import random
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
#
# student_scores = {name: random.randint(1, 100) for name in names}
# print(student_scores)
# passed_students = {name: value for (name, value) in student_scores.items() if value >= 60}
# print(passed_students)


# ############### CODING EXERCISE ##################
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
# # Write your code 👇 below:
#
# weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row)







