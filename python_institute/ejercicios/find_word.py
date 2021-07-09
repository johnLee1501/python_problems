def pos(text, substr):
    for letter in substr:
        if letter not in text:
            return 'No'
    return 'Si'


substr = input()
text = input()
print(pos(text, substr))
