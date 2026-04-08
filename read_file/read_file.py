f = open("file.txt", "r", encoding="utf-8")  # ye line file.txt ko read mode me open karegi
content = f.read()  # ye line file ke content ko read karegi aur content variable me store karegi
print(content)  # ye line content variable ke value ko print karegi
f.close()  # ye line file ko close karegi