from csv import writer

with open("file1.csv", "w", encoding="utf-8", newline="") as f:
    csv_writer = writer(f)
    #csv_writer.writerow(["Name", "Age"])  # Write header
    #csv_writer.writerow(["Shubham", 25])     # Write data row
    #csv_writer.writerow(["Sonu", 30])       # Write data row

    csv_writer.writerows([["Name", "Age"], ["Rohit", 28], ["Anjali", 22]])  # Write multiple data rows