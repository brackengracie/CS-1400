print("")
print("Welcome to the Leet Speak Translator")
print("")
print("If you have a file that is written in leet")
print("speak, we can translate it back to normal")
print("english for you.")
print("")
print("just give me the name of the file you want")
print("to have translated, and the name you want")
print("for the translated file.")
print("")

# 1. What are we returning?

# This method opens a file and converts it to a string
# @param {String} file_name: the name of the file you want to open
# @returns String
def open_file_and_convert_to_String(file_name):
    file = open(file_name, "r") # open the file
    leet = "" # create a blank string to store the converted lines in

    # Go through each line in the file and strip white space
    for line in file:
        leet =  leet + line.strip() + "\n"

    file.close()
    return leet

def translate(string):
    translation = ""

    for char in string:
        translated_char = translate_char(char)
        translation = translation + translated_char

    return translation

def create_file(converted_file, new_file_name):
    new_file = open(new_file_name, "w")

    translation = translate(converted_file)
    # We need to separate lines,

    new_file.write(translation)
    new_file.close()

def translate_char(char):
    if char == "4":
        return "a"
    if char == "8":
        return "b"
    if char == "3":
        return "e"
    if char == "1":
        return "l"
    if char == "0":
        return "o"
    if char == "5":
        return "s"
    if char == "7":
        return "t"
    if char == "@":
        return "a"

    return char

def main():
    # What file do we want to translate?
    translate_file_name = input("What file would you like to translate? ")

    # Get the file that needs to be translated and assign it to a variable
    converted_file = open_file_and_convert_to_String(translate_file_name)

    # What would you like to name the new file?
    new_file_name = input("What would you like to name the output file? ")

    # translate the file
    create_file(converted_file, new_file_name)

main()
