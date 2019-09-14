import sys
from os import path


file_name = "my_ideas_bank"


# check an existance and create file if not exists, read ideas from file
def ideas_reader():
    if not path.exists(file_name):
        my_ideas_bank = open(file_name, "a+")
    else:
        my_ideas_bank = open(file_name, "r+")
        list_of_ideas = my_ideas_bank.readlines()
        my_ideas_bank.close()
        return list_of_ideas


# show the list of ideas
def display(list_of_ideas):
    print("Your ideabank:\n")
    for index, value in enumerate(list_of_ideas, 1):
        print(f"{index}. {value}")


# save ideas in text file
def ideas_writer(list_of_ideas):
    blank_idea = False
    while blank_idea is False:
        new_users_idea = input("What is your new idea:\n")
        if new_users_idea == "" or new_users_idea == " ":
            print("Your idea can't be empty")
            blank_idea = False
        else:
            blank_idea = True
    new_users_idea = new_users_idea + "\n"
    my_ideas_bank = open(file_name, "a+")
    my_ideas_bank.write(new_users_idea)
    my_ideas_bank.close()
    print("New idea added")


# delete the idea(works on two ways, depends of quantity of arguments)
def ideas_deleter(list_of_ideas, *argv):
    print("Your ideabank:\n")
    if not argv:
        for index, value in enumerate(list_of_ideas, 1):
            print(index, value)
        out_of_range = True
        while out_of_range:
            try:
                delete_id = int(input("Give the number of idea you want to delete:\n"))
                if delete_id <= 0 or delete_id > len(list_of_ideas):
                    print("Your don't have idea with such number")
                    continue
                out_of_range = False
            except ValueError:
                print("Give a correct number!")
                continue
    else:
        delete_id = int(argv[0])
    try:
        list_of_ideas.pop(delete_id-1)
        my_ideas_bank = open(file_name, "w")
        my_ideas_bank.writelines(list_of_ideas)
        my_ideas_bank.close()
        print("The idea was deleted\n")
        for index, value in enumerate(list_of_ideas, 1):
            print(index, value)
    except IndexError:
        print("Your don't have idea with such number!")


def main():
    if len(sys.argv) == 1:
        # Display first idea
        ideas_writer(ideas_reader)
        display(ideas_reader())
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--list":
            # Show all ideas
            display(ideas_reader())
        elif sys.argv[1] == "--add":
            # Add a new idea
            ideas_writer(ideas_reader)
        elif sys.argv[1] == "--del":
            # Remove an idea by id
            ideas_deleter(ideas_reader())
        else:
            print("Unknown command")
    elif len(sys.argv) == 3:
        if sys.argv[1] == "--del":
            ideas_deleter(ideas_reader(), sys.argv[2])
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
