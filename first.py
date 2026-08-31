words = set()

#function that takes the argument words and return it in lower caps
def check(word):
    return word.lower() in words

#function that takes one argument and opens it, then fills it and updates it 
def load(dictionary):
    with open(dictionary) as file:
        words.update(file.read().splitline())
    return type

# function to check for length of words
def sized():
    return len(words)


def unload():
    return True