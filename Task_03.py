words = ['абв'] 
listOfWordsToTry = ['абв', 'авбабававб ']
def validate(w):
    for word in words:
        if w.startswith(word):
            return False
    return True