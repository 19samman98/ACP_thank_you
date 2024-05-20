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


def story(fullname):
    """
    Opens blankthankyou.txt to read the file, insert answers from the list created by names(), and insert answers into blankthankyou.txt
    param: fullname: the full name of the donor to be used when creating the text file.
    """
    blankthank = open("blankthankyou.txt", "r")
    fullnote = open("Thank You " + fullname + ".txt", "w")

    name_list = names()

    for line in blankthank:
        line = line.format(*name_list)
        fullnote.write(line)


def main():
    name = " "
    while 1 > 0:
        print("To stop the program, please type '0' as the donor name.")
        name = input("Enter the full name of the donor:")
        if name == "0":
            quit()
        story(name)


main()
