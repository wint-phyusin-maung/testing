i = 1
while i <= 10:
    print(i)
    if i == 4:
        i = i + 3
        continue
    i = i + 1

print('Loop Done!')

text = ""
print("Enter 'stop' to quit!")
while text != "stop":
    text = input("Enter: ")
    if text == "stop":
        break
