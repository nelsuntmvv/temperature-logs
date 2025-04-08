import sys

# Check if input file is given
if len(sys.argv) != 2:
    print("Please provide the input file.")
    sys.exit()

filename = sys.argv[1]

days = []
temps = []

try:
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            days.append(parts[0])
            temps.append(int(parts[1]))

    total = sum(temps)
    average = total / len(temps)

    coldest_temp = min(temps)
    index = temps.index(coldest_temp)
    coldest_day = days[index]

    with open("output.txt", 'w') as out:
        out.write("Average Temperature: " + str(round(average, 2)) + "°C\n")
        out.write("Coldest Day: " + coldest_day + " (" + str(coldest_temp) + "°C)\n")

    print("Done! Check output.txt.")

except:
    print("Something went wrong.")