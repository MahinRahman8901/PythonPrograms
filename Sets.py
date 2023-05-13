def check_uses_all_letters(sentence):
    l = sentence.lower()
    return len(set(l)) == 27

def check_and_print(sentence):
    if check_uses_all_letters(sentence):
        print(sentence, "has used all the letters")
    else:
        print(sentence, "has not used all the letters")

if __name__ == '__main__':
    check_and_print("The quick brown fox jumps over the lazy dog")
    check_and_print("Pack my box with five dozen liquor jugs")
    check_and_print("The explorer was frozen in his big kayak just after making strange discoveries")
    check_and_print("Mahin is cool")
    check_and_print("abcdefghijklmnopqrstuvwxyz ")
