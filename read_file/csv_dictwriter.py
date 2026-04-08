from csv import DictWriter

with open("file2.csv", "w", encoding="utf-8", newline="") as f:
    csv_dict_writer = DictWriter(f, fieldnames=["Name", "Age"])
    csv_dict_writer.writeheader()  # Write header
    csv_dict_writer.writerow({"Name": "Shubham", "Age": 25})  # Write data row
    csv_dict_writer.writerow({"Name": "Sonu", "Age": 30})      # Write data row

    csv_dict_writer.writerows([{"Name": "Rohit", "Age": 28}, {"Name": "Anjali", "Age": 22}])  # Write multiple data rows