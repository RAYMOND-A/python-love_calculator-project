# Love calculator coding challenge

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

combined_name = lower_name1 + lower_name2
print(combined_name)

number_of_t = combined_name.count('t')
number_of_r = combined_name.count('r')
number_of_u = combined_name.count('u')
number_of_e = combined_name.count('e')

number_of_true = number_of_t + number_of_r + number_of_u + number_of_e
string_number_of_true = str(number_of_true)
print(str(number_of_true))

number_of_l = combined_name.count('l')
number_of_o = combined_name.count('o')
number_of_v = combined_name.count('v')
number_of_e = combined_name.count('e')

number_of_love = number_of_l + number_of_o + number_of_v + number_of_e
string_number_of_love = str(number_of_love)
print(str(number_of_love))

love_score = string_number_of_true + string_number_of_love
print(love_score)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is **{love_score}**, you go together like coke and mentos.")
elif int(love_score) > 40 and int(love_score) < 50:
    print(f"Your score is **{love_score}**, you are alright together")
else:
    print(f"Your score is **{love_score}**")

