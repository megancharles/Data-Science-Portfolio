import csv
import matplotlib.pyplot as plt

# Read the CSV file and count the number of males and females
with open('Biostats.csv', newline='', encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    # Create a dictionary called sex_counts with key-value pairs to store the count of the categories
    Sex_counts = {'M': 0, 'F': 0}
    # Count the number of M and F in that column
    for row in reader:
        Sex = row["Sex"]
        if Sex == 'M':
            Sex_counts['M'] += 1
        elif Sex == 'F':
            Sex_counts['F'] += 1

# Extract x (Sexs) and y (counts) values from the dictionary
x = list(Sex_counts.keys())
y = list(Sex_counts.values())

# Create a bar chart
plt.figure(figsize=(6, 6))
plt.bar(x, y)
plt.xlabel("Sex")
plt.ylabel("Count of Participants")
plt.title("Sex Distribution in the Dataset")
plt.show()
