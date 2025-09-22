import matplotlib.pyplot as plt


def plot_histogram():
    with open("admission_algorithms_dataset.csv", "r") as file:
        students = file.readlines()
    gpa = []
    sat = []
    for student in students:
        if (student.split(",")[2]) != "GPA":
            gpa.append(float(student.split(",")[2]))
        if (student.split(",")[1]) != "SAT":
            sat.append(float(student.split(",")[1]))
    plt.hist(gpa)
    plt.savefig("gpa.png")
    plt.clf()
    plt.hist(sat)
    plt.savefig("sat_score.png")
    plt.clf()


def plot_scatter():
    with open("admission_algorithms_dataset.csv", "r") as file:
        students = file.readlines()
    gpa = []
    sat = []
    for student in students:
        if (student.split(",")[2]) != "GPA":
            gpa.append(float(student.split(",")[2]))
        if (student.split(",")[1]) != "SAT":
            sat.append(float(student.split(",")[1]))
    plt.scatter(gpa, sat)
    plt.savefig("correlation.png")
    plt.clf()


def plot_spectra():
    with open("spectrum1.txt", "r") as file:
        spec_1 = file.readlines()
    spec_1_wavelength = []
    spec_1_flux = []
    for spec in spec_1:
        spec_1_wavelength.append(float(spec.split()[0]))
        spec_1_flux.append(float(spec.split()[1]))
    with open("spectrum2.txt", "r") as file:
        spec_2 = file.readlines()
    spec_2_wavelength = []
    spec_2_flux = []
    for specs in spec_2:
        spec_2_wavelength.append(float(specs.split()[0]))
        spec_2_flux.append(float(specs.split()[1]))
    plt.plot(spec_1_wavelength, spec_1_flux, "b")
    plt.plot(spec_2_wavelength, spec_2_flux, "g")
    plt.savefig("spectra.png")
    plt.clf()


def main():
    plot_histogram()
    plot_scatter()
    plot_spectra()



if __name__ == "__main__":
    main()
