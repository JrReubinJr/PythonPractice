__author__ = "reubin"

def age_in_seconds():
    user_age = input("Enter your age: ")
    age_seconds = int(user_age) * 365 *24 * 60 *60
    print("Your age in seconds is {}".format(age_seconds))

age_in_seconds()