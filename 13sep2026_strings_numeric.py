#1 Check if the user is either an admin or a moderator,
#and either they are not banned or they have verified email

is_admin = False
is_moderator = True
is_banned = True
has_verified_email = True
print((is_admin or is_moderator) and (not is_banned or has_verified_email))

#2 check if a username is a string , is not None,
#and is longer than 5 characters.
user_name = "amjad"
length = len(user_name)
print((isinstance(user_name, str) is not None) and length > 5)

#3 check if a user email is not empty , contains @ and ends with .com
email = "amjad@gmail.com"
print(email is not None and email.endswith(".com") and "@" in email)

#4 check if password is atleast 8 characters long and does not contain spaces
password = "1.  28934je5hrtebfun5"
length = len(password)
if length >= 8:
    if len(password.replace(" ","")) == len(password):
        print("correct password")
    else:
        ("Password must be space free")
else:
    print("Password must contain atleast 8 characters")
#5 check if a user name is not empty and the age is greater than or equal to 18
user_name = None
user_age = 18
print(user_name is not None and user_age >= 18)

#6
#generate a random integer between 1 and 100
#check if the result is an even number
import random
random_number = random.randint(1,1000)
print(random_number)
if random_number % 2 == 0:
    print(f"{random_number} is an even number")
else:
    print(f"{random_number} is an odd number")