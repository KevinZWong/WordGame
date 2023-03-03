import enchant


class WordGen:
    def __init__(self):
        pass
        
    def is_word(word):
        dictionary = enchant.Dict("en_US")
        return dictionary.check(word)

# example usage
if is_word("hello"):
    print("hello is a word")
else:
    print("hello is not a word")8