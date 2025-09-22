
def read_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lab = []
        hw = []
        project = []
        midterm1 = []
        midterm2 = []
        final = []
        for line in lines:
            if line[0] == "#":
                continue
            if line.strip() == '':
                continue
            line = line.strip().split(",")
            if "Lab" in line[0]:
                lab.append(line)
            elif "Homework" in line[0]:
                hw.append(line)
            elif "Project" in line[0] or "FreeCoding" in line[0]:
                project.append(line)
            elif "Midterm1" in line[0]:
                midterm1.append(line)
            elif "Midterm2" in line[0]:
                midterm2.append(line)
            elif "Final" in line[0]:
                final.append(line)
    return lab, hw, project, midterm1, midterm2, final


def initial_output(lab, hw, project, midterm1, midterm2, final):
    lab_point_value = 20
    hw_point_value = 50
    project_point_value = 100
    midterm_point_value = 40
    final_point_value = 70
    lab_percentage = 0
    hw_percentage = 0
    project_percentage = 0
    mid1_percentage = 0
    mid2_percentage = 0
    final_percentage = 0
    for list in lab, hw, project, midterm1, midterm2, final:
        if not list:
            continue
        else:
            if "Lab" in list[0][0]:
                lab_percentage = calculate_total_points("Labs:", list, lab_point_value)
            if "Homework" in list[0][0]:
                hw_percentage = calculate_total_points("Homework:", list, hw_point_value)
            if "Project" in list[0][0] or "FreeCoding" in list[0][0]:
                project_percentage = calculate_total_points("Projects:", list, project_point_value)
            if "Midterm1" in list[0][0]:
                mid1_percentage = calculate_total_points("Midterm 1:", list, midterm_point_value)
            if "Midterm2" in list[0][0]:
                mid2_percentage = calculate_total_points("Midterm 2:", list, midterm_point_value)
            if "Final" in list[0][0]:
                final_percentage = calculate_total_points("Final:", list, final_point_value)
    return lab_percentage, hw_percentage, project_percentage, mid1_percentage, mid2_percentage, final_percentage


def calculate_total_points(name, list, point_value):
    counter = 0
    total = 0
    for item in list:
        thing = float(item[1].strip())
        counter += 1
        total += thing
    percentage = (total/(counter * point_value)) * 100
    print(f"{name}{total: .1f}/{counter * point_value} {percentage:.1f}%")
    return percentage


def drop_lowest(grades):
    new_list = sorted(grades, key=lambda x: x[1])
    return new_list[1:]


def final_grade(lab_p, hw_p, project_p, mid1_p, mid2_p, final_p):
    new_list = []
    grade_type = 0
    for percentage in lab_p, hw_p, project_p, mid1_p, mid2_p, final_p:
        if percentage == 0:
            continue
        else:
            new_list.append([grade_type,percentage])
        grade_type += 1
    grade_weights = [15, 10, 25, 15, 15, 20]
    total_percent = 0
    counter = 0
    for percentage in lab_p, hw_p, project_p, mid1_p, mid2_p, final_p:
        total_percent += (percentage * (grade_weights[counter]* 0.01))
        counter += 1
    if len(new_list) == 6:
        return total_percent
    else:
        fraction_percent= 0
        for item in new_list:
            fraction_percent += grade_weights[item[0]]
        return total_percent/(fraction_percent * 0.01)


def letter_grade(percent):
    grade_scale = [["A", 93], ["A-", 90], ["B+", 87], ["B", 83], ["B-", 80], ["C+", 77], ["C", 73], ["C-", 70], ["D+", 67], ["D", 63], ["D-", 60], ["E", 59.999999]]
    letter = "A"
    counter = 0
    for thing in grade_scale:
        if percent < thing[1]:
            letter = grade_scale[counter + 1][0]
        counter += 1
    print()
    print(f"The overall grade in the class is: {letter} ({percent:.2f}%)")


def main():
    filename = input("Enter filename: ")
    lab, hw, project, midterm1, midterm2, final = read_lines(filename)
    lab = drop_lowest(drop_lowest(lab))
    hw = drop_lowest(hw)
    lab_p, hw_p, project_p, mid1_p, mid2_p, final_p = initial_output(lab, hw, project, midterm1, midterm2, final)
    end_percentage = final_grade(lab_p, hw_p, project_p, mid1_p, mid2_p, final_p)
    letter_grade(end_percentage)


if __name__ == "__main__":
    main()
