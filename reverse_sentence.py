def sentence_rev():
    user_input = input("Enter a sentence: ")
    splitted = user_input.split('is')
    rev_splitted = splitted[::-1]
    rev_splitted.insert(1, 'is')
    sentence = ''
    for i in rev_splitted:
        if rev_splitted.index(i) == -1:
            sentence += i.strip()
        else:
            sentence += (i.strip() + ' ')
    new_sentence = sentence.capitalize()
    print(new_sentence)
    return None


sentence_rev()
