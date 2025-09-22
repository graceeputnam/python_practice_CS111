def get_others(number):
    num = float(input("Enter a floating point number "))
    fam = input("Enter a family relationship (mother, grandfather, cousin, etc.) ")
    noun = input("Enter a noun ")
    adjective = input("Enter an adjective ")
    print(f"{int(number) // 20} score and {num:.3f} years ago, our fore{fam}s brought forth upon this {noun} a {adjective} nation.")


def check_num():
    number = input("Enter an integer divisible by 20 ")
    if not int(number) % 20 == 0:
        print(f"{number} is not divisible by 20!")
    else:
        get_others(number)


def main():
    check_num()


if __name__ == "__main__":
    main()
