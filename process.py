import csv

try:
    temperatures = []
    days = []

    # Read input and write enhanced CSV
    with open('input.csv', 'r') as infile, open('output.csv', 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['Day', 'Temperature', 'Description']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            day = row['Day'].strip()
            temp = float(row['Temperature'].strip())
            desc = row['Description'].strip()

            writer.writerow({'Day': day, 'Temperature': temp, 'Description': desc})

            temperatures.append(temp)
            days.append((day, temp))

    # Calculate summary
    average_temp = sum(temperatures) / len(temperatures)
    coldest_day = min(days, key=lambda x: x[1])

    # Save to output.txt
    with open('output.txt', 'w') as summary_file:
        summary_file.write(f"Average temperature: {average_temp:.2f}°C\n")
        summary_file.write(f"Coldest day: {coldest_day[0]} ({coldest_day[1]}°C)\n")

    print("Done! Check output.csv and output.txt.")

except Exception as e:
    print(" Something went wrong.")
    print(f"Error: {e}")
