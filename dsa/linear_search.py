tests = []

test = {
    'input': {
        'cards': [13, 11, 10, 6, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

def findNumber(cards,query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

        
result = findNumber(test['input']['cards'], test['input']['query'])

print(result)




