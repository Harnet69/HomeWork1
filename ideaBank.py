import sys
from os import path
file_name = "my_ideas_bank"

def ideas_reader():
# check an existance of ideas file and create if not exists, read ideas from text file (file per line)
    if not path.exists("my_ideas_bank"):
        my_ideas_bank = open(file_name, "a+")
    else:
        my_ideas_bank = open(file_name, "r+")
        list_of_ideas = my_ideas_bank.readlines()
        my_ideas_bank.close()
        return list_of_ideas


def display(list_of_ideas):
# show the list of ideas
    print("There is the list of your ideas:\n")
    for index, value in enumerate(list_of_ideas, 1):
        print(index, value)

def ideas_writer(list_of_ideas):
# save ideas in text file
    print(list_of_ideas)
    blank_idea = False
    while blank_idea is False:
        new_users_idea = input("Type your brilliant idea!\n")
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


def ideas_deleter(list_of_ideas):
# delete the idea
    print("There are your ideas:\n")
    for index, value in enumerate(list_of_ideas, 1):
        print(index, value)
    out_of_range = True
    while out_of_range:
        try:
            delete_id = int(input("Give the number of idea you want to delete: \n"))
            if delete_id > len(list_of_ideas):
                print("Your number is out of range!")
                continue
            out_of_range = False
        except ValueError:
            print("Give a correct number!")
            continue
    list_of_ideas.pop(delete_id-1)
    my_ideas_bank = open(file_name, "w")
    my_ideas_bank.writelines(list_of_ideas)
    my_ideas_bank.close()
    print("The idea was deleted\n")
    for index, value in enumerate(list_of_ideas, 1):
        print(index, value)


def main():

# check_ideas_file()
    if len(sys.argv) == 1:
    #   Display first idea
        ideas_writer(ideas_reader)
        display(ideas_reader())
        #first_idea = ideas_reader()
        #print(first_idea[0])
    else:
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


if __name__ == "__main__":
    main()