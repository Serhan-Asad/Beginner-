def bubble_sort(lst,key="name"):
    size=len(lst)

    for j in range(size-1):
        swap=False
        for i in range(size - 1):
            if lst[i][key] > lst[i + 1][key]:
                s = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = s
                swap=True
        if not swap:
            break
    return lst

elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]


bubble_sort(elements)
print(elements)
