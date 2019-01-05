"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    #breakpoint()

    # Make a new directory
    # The next time you run this, it will crash if the directory exists

    # Getting the extensions available:
    extension_list = []
    extension_exist = True

    for filename in os.listdir('.'):

        if filename == ".DS_Store":
            continue

        extension = os.path.splitext(filename)[1]

        if len(extension_list) == 0:
            extension_list.append(extension)

        for each in extension_list:

            if extension == each:
                extension_exist = True
                break
            else:
                extension_exist = False

        if extension_exist == False:
            extension_list.append(extension)

    # Create extension dirs:
    print(extension_list)
    for each in extension_list:
        if each != "":
            try:
                os.mkdir(each[1:])
            except:
                os.rmdir(each[1:])
                os.mkdir(each[1:])

    #@ breakpoint()

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):

        if filename == ".DS_Store":
            continue

        extension = os.path.splitext(filename)[1]
        extension_to_move = extension[1:]
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue
        shutil.copy(filename, extension_to_move + '/' + filename)


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # TODO: add a loop to rename the files


main()
# demo_walk()
