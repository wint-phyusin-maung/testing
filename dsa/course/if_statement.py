age = input("Your age: ")

if ( 10 <= int(age) <= 18):
    print("You can play the game now!")
else:
    print("Sorry, you age is not allowed to play!")


adult =  True if int(age) >= 18 else False

print(adult)

print("If done!")

