import csv
import matplotlib.pyplot as plt

years = []
north = []
south = []


with open("../data/SN_d_hem_V2.0.csv") as file:
    reader = csv.reader(file, delimiter=';', skipinitialspace=True)
    
    for line in reader:
        years.append(float(line[3]))
        north.append(int(line[5]))
        south.append(-int(line[6]))

plt.fill_between(years, north, color="#22CE00FF", alpha=0.5, label="Northern Hemisphere")
plt.fill_between(years, south, color="#CF008AFF", alpha=0.5, label="Southern Hemisphere")
ax = plt.gca()
ax.set_facecolor("#FFFFFFFF")

plt.title("Solar Cycle Hemispheric Asymmetry (1992-2026)")
plt.xlabel("Year")
plt.ylabel("Sunspot number")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()