import sys


# recieve a word from user for changing
def user_input(sys_argv):
    user_words = []
    for word in sys_argv[1:]:
        user_words.append(word)
    return user_words


# change a user word to present participle forms
def verb_changer(user_words):
    vowels = "aeiou"
    changed_words = []

    for word in user_words:
        if 'ie' in word[-2:]:
            changed_words.append(word[0:-2] + "y" + "ing")
        elif 'e' in word[-1]:
            if word == 'be'or word == 'see' or word == 'flee' or word == 'knee':
                changed_words.append(word + "ing")
            else:
                changed_words.append(word[0:-1] + "ing")
        elif word[-3] not in vowels and word[-2] in vowels and word[-1] not in vowels:
            changed_words.append(word + word[-1] + "ing")

        else:
            changed_words.append(word + "ing")
    return changed_words


# print a word in present participle form
def display(user_words, changed_word):
    result = list(zip(user_words, changed_word))
    max_words_length = 0
    # look for word with max length for a right allignment
    for w, w_ch in result:
        if len(w) > max_words_length:
            max_words_length = len(w)
    print(f"\n{'Verb':<{max_words_length}}  | Present Participle form\n")
    for w, w_ch in result:
        print(f"{w:<{max_words_length}}  | {w_ch}")


def main():
    if len(sys.argv) < 2:
        print("You didn't type any word for changing!")
    else:
        user_words = user_input(sys.argv)
        changed_words = verb_changer(user_words)
        display(user_words, changed_words)


if __name__ == "__main__":
    main()
