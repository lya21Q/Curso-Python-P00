animals=["dog", "cat", "elephant"]
def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + str(animals[i]) + '\n'
    return lst
print(list_animals(animals))