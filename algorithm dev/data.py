import csv

# Create a new CSV file and open it for writing
with open('data.csv', mode='w') as file:

    # Define the CSV writer object
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Time', 'Temp', 'Price', ''])

    # Write some data rows
    writer.writerow(['Alice', 25, 'Female'])
    writer.writerow(['Bob', 32, 'Male'])
    writer.writerow(['Charlie', 18, 'Non-binary'])
