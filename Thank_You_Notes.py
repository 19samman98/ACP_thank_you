######################################################################
# Author: Sam McFarland
#
# Purpose: A program which takes user input of donor names and writes them to a text file to create thank you notes.
######################################################################


def names():
    """
    Opens a file to read called "names.txt" and asks for user input for each line
    param: none
    """
    promptfile = open("names.txt", "r")

    answers = []
    for line in promptfile:
        ans = input(line)
        answers.append(ans)

    return answers
    # ...


def note(fullname, person):
    """
    Opens a text file to read the file, insert info from names(), and insert answers into a thank you note
    param: fullname: the full name of the donor to be used when creating the text file.
    param: person: the person writing the letter
    """
    blankthank = open(person + "thankyou.txt", "r")
    fullnote = open("Thank You " + fullname + " from " + person + ".txt", "w")

    name_list = names()

    for line in blankthank:
        line = line.format(*name_list)
        fullnote.write(line)


def main():
    """
    A function that asks the user input for names and creates thank you notes based on the user input
    :return: None
    """
    while 1 > 0:
        print("To stop the program, please type '0' as the donor name.")
        name = input("Enter the full name of the donor:")
        if name == "0":
            quit()
        else:
            person = input("Who would you like the letter to be from? [employee, student]")
            note(name, person)


main()
