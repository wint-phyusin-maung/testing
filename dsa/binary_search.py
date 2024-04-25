from random import choice

def findNum(cards, query):
    lo,hg  = 0 , len(cards) - 1

    while lo <= hg:
        mid = (lo + hg) // 2
        mid_number = cards[mid]

        if mid_number == query:
            return mid
        elif mid_number < query:
            hg = mid - 1
        elif mid_number > query: 
            lo = mid + 1
    return -1 


test = {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 10}}
result = findNum(test['input']['cards'], test['input']['query'])
print(result)