def test_location(cards,query,mid):
    mid_number = cards[mid]
    print("mid:",mid, "mid_number",mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'
    
def located_card(cards,query):
    low,hight = 0 , len(cards) - 1

    while low <= hight: 
        print('low',low,'hight',hight)
        mid = (low + hight) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hight = mid - 1 
        elif result == 'right':
            low = mid + 1
    return -1 


test = {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 10}}
result = located_card(test['input']['cards'], test['input']['query'])
print(result)