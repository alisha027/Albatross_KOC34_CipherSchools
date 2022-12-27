import random

while True:
    no_of_chars = int(input("Enter the number of characters required for your password: "))
    if no_of_chars >= 12:
        break
    else:
        print("The minimum number of characters required for password is 12. Please enter a number greater than or equal to 12.\n")

list_of_chars = "A B D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 ! @ # $ % ^ & * ( )".split(" ")


password = ""

for i in range(no_of_chars):
    password += list_of_chars[random.randint(0,len(list_of_chars)-1)]

numerical_check =  False
special_char_check = False
lower_case_check = False
upper_case_check = False

for i in password:
    if i.isnumeric():
        numerical_check = True
    if i in "! @ # $ % ^ & * ( )":
        special_char_check = True
    if i.islower():
        lower_case_check = True
    if i.isupper():
        upper_case_check = True

if numerical_check and special_char_check and lower_case_check and upper_case_check:
    print(f"The password generated is {password}.")
        