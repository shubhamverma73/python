def kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwargs(name="shubham", age=25, city="delhi")