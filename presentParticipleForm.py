def user_input():
# take a word from user for changing
    return input("Give a verb for present participle: \n")

def verb_changer(word):
# change a user word to present participle form 
    if 'ie' in word[-2:]:
        return word[0:-2] + "y" + "ing"

    elif 'e' in word[-1]:
        if word == 'be'or word == 'see' or word == 'flee' or word == 'knee':
            return word + "ing"    
        else:
            return word[0:-1] + "ing"
    elif word[-3] not in "aeiou" and word[-2] in "aeiou" and word[-1] not in "aeiou":
        return word + word[-1] + "ing"

    else:
        return word + "ing"

def display(changed_word):
# print a word in present participle form
    print(f'The present participle form is : {changed_word}')


def main():
    user_verb = user_input()
    changed_word = verb_changer(user_verb)
    display(changed_word)

if __name__ == "__main__":
    main()