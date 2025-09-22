import sys


def print_args(arguments):
    for argument in arguments:
        print(argument)


def check_arguments(arguments):
    if arguments[1] == '-p' or arguments[1] == '-i' or arguments[1] == '-h' or arguments[1] == "-w" or arguments[1] == "-r":
        return True
    else:
        return False


def flags(arguments):
    if arguments[1] == "-p":
        for argument in arguments[2:]:
            print(argument)
    if arguments[1] == "-i":
        print("Hello World")
    if arguments[1] == "-h":
        print("Valid flags:")
        print("-p : prints out all the command line arguments after the -p")
        print('-i : prints "Hello World"')
        print("-h : prints out a help command")
    if arguments[1] == "-w":
        with open(arguments[2], "w") as file:
            if len(arguments) <= 3:
                print("No Content Provided")
            else:
                for argument in arguments[3:]:
                    file.write(argument + "\n")
    if arguments[1] == "-r":
        with open(arguments[2], "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                print(line)


def main(arguments):
    if check_arguments(arguments):
        flags(arguments)
    else:
        print_args(arguments)

if __name__ == "__main__":
    main(sys.argv[:])

