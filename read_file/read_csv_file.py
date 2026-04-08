from csv import DictReader, reader

with open("file.csv", "r", encoding="utf-8") as f:  # ye line file.csv ko read mode me open karegi
    csv_reader = reader(f)  # ye line file object f ko csv reader me convert
    next(csv_reader)  # ye line csv_reader me se pehli row ko skip karegi (jo header hoti hai)
    for val in csv_reader:  # ye line csv_reader me se har ek row ko val variable me store karegi
        print(val)  # ye line val variable ke value ko print karegi

with open("file.csv", "r", encoding="utf-8") as f:  # ye line file.csv ko read mode me open karegi
    csv_dict_reader = DictReader(f)  # ye line file object f ko csv dict reader me convert karegi
    for val in csv_dict_reader:  # ye line csv_dict_reader me se har ek row ko val variable me store karegi
        print(val['name'])  # ye line val variable ke value ko print karegi
    