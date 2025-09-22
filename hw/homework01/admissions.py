# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


# define your functions here
def convert_row_type(s):
    new_list = []
    for item in s:
        new_list.append(float(item))
    return new_list


def calculate_score(s):
    return (((s[0]) / 160) * 0.3) + ((s[1] * 2) * 0.4) + (s[2] * 0.1) + (s[3] * 0.2)


def is_outlier(s):
    if s[2] == 0 or (s[1]*2) > (s[0]/160) + 2:
        return True
    else:
        return False
# SAT, GPA, Interest, High School Quality

def calculate_score_improved(s):
    score = calculate_score(s)
    outlier = is_outlier(s)
    if score >= 6 or outlier:
        return True
    else:
        return False


def grade_outlier(grades):
    new_list = sorted(grades)
    if new_list[1] - new_list[0] > 20:
        return True
    else:
        return False


def grade_improvement(grades):
    if grades == sorted(grades):
        return True
    else:
        return False


def main():
    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")

    print("Processing " + filename + "...")
    # grab the line with the headers

    lines = input_file.readlines()
    for line in lines[1:]:
        line = line.strip().split(",")
        name = line[0]
        line.remove(name)
        line = convert_row_type(line)
        check_row_types(line)
        four_qualifiers = line[:4]
        grades = line[4:]
        score = calculate_score(four_qualifiers)
        with open("student_scores.csv", "a") as file:
            file.write(f"{name},{score:.2f}\n")
        if score >= 6:
            with open("chosen_students.csv", "a") as file:
                file.write(f"{name}\n")
        if is_outlier(four_qualifiers) is True:
            with open("outliers.csv", "a") as file:
                file.write(f"{name}\n")
        if score >= 6 or score >= 5 and is_outlier(four_qualifiers) is True:
            with open("chosen_improved.csv", "a") as file:
                file.write(f"{name}\n")
        if calculate_score_improved(four_qualifiers):
            with open("better_improved.csv", "a") as file:
                file.write(f"{name},{four_qualifiers[0]},{four_qualifiers[1]},{four_qualifiers[2]},{four_qualifiers[3]}\n")
        if score >= 6 or score >= 5 and (is_outlier(four_qualifiers) or grade_outlier(grades) or grade_improvement(grades)):
            with open("composite_chosen.csv", "a") as file:
                file.write(f"{name}\n")

    # TODO: make sure to close all files you've opened!
    input_file.close()
    print("done!")

# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
