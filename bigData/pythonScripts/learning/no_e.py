
def has_no_e(word):
    for letter in word:
        if letter == 'e':
             return True
        else:
            setValue = False
    return setValue

print has_no_e("I am in the information does it have an e")
