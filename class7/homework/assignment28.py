# Name: Owen Shi
# Sunday, Oct. 27th, 2024
# Assignment 28

hour = int(input("Enter hour (in 24 hour time): "))

if hour < 12:
    print("Good Morning")
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
else:
    print("Good Evening")
