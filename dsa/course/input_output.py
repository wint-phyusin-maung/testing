fruit = ['apple', 'orange', 'pineapple', 'blueberry', 'grape']
tax = 1.25 
prices = [5400, 3000, 4000, 10000, 5000]

fruit_name = input('Enter fruit name: ')

found = False 

for i, item in enumerate(fruit):
    if item == fruit_name:
        result = tax * prices[i]
        print(result)
        found = True
        break

if not found:
    print('Fruit is not found!')