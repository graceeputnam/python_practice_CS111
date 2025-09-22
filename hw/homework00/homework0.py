## CONSTANTS SHOULD GO BELOW THIS COMMENT ##
PEOPLE_PER_LARGE = 7
PEOPLE_PER_MEDIUM = 3
PEOPLE_PER_SMALL = 1
PI = 3.14159265
DIAMETER_LARGE = 20
DIAMETER_MEDIUM = 16
DIAMETER_SMALL = 12
COST_LARGE = 14.68
COST_MEDIUM = 11.48
COST_SMALL = 7.28


def pizzas_amount(guests):
    large = guests // PEOPLE_PER_LARGE
    remainder = guests % PEOPLE_PER_LARGE
    medium = remainder // PEOPLE_PER_MEDIUM
    remainder_2 = remainder % PEOPLE_PER_MEDIUM
    small = remainder_2 // PEOPLE_PER_SMALL
    if remainder_2 % PEOPLE_PER_SMALL:
        small += 1
    print(f"{large} large pizzas, {medium} medium pizzas, and {small} small pizzas will be needed.")
    return large, medium, small


def total_area(large, medium, small, guests):
    total = 0
    total += (large * (PI * ((DIAMETER_LARGE/2)**2)))
    total += (medium * (PI * ((DIAMETER_MEDIUM/2)**2)))
    total += (small * (PI * ((DIAMETER_SMALL/2)**2)))
    per_student = (total/guests)
    print()
    print(f"A total of {total:.2f} square inches of pizza will be ordered ({per_student:.2f} per guest).")


def find_cost_tip(large, medium, small):
    tip = input("Please enter the tip as a percentage (i.e. 10 means 10%): ")
    total = 0
    total += (large * COST_LARGE)
    total += (medium * COST_MEDIUM)
    total += (small * COST_SMALL)
    total += ((float(tip)* .01)*total)
    print(f"The total cost of the event will be: ${total:.2f}")


def main():
    guests = int(input("Please enter how many guests to order for: "))
    large, medium, small = pizzas_amount(guests)
    total_area(large, medium, small, guests)
    find_cost_tip(large, medium, small)
    ## YOUR CODE SHOULD GO IN THIS FUNCTION ##


if __name__ == "__main__":
    main()
