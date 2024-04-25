programmer = "John Sohn"
#print(type(programmer))
#print(programmer)
html_code = "Su Su"
#print("HTML coder = ", html_code)

quoteOne = """
    hello,
       how are you?
"""

#print(quoteOne)

quoteTwo = '''
    It's is easier to ask forgiveness.
'''

#print(quoteTwo)

school = "Yale University"

# print(school)
# print(type(school[0]))
# print(school[5])
# print(school[0:4])
# print(len(school))

other_string = "Vassar College"
# print(other_string)

# if school == other_string:
#     print('Schools are the same!')
# else:
#     print("Schools are not the same!")


text = "invented one of the 1st linkers"

count = 0

for character in text:
    if character == "e":
        count += 1
    #print(character)

if ("one" in text):
    print("one is in the character!")
print(count)


birth = " Born in New York City "
print(birth.upper())
print(birth.lower())
print(birth.strip())

print(birth.replace('York','Fork'))

print(birth.split()) #to array

first_name = "Gepper"
second_name = "Hyper"
full_name = first_name + second_name
print(full_name)

birth_date = "{} in {} year {}"

print(birth_date.format("Born","the",2000))

print("Line 1\nLine 2")

print()