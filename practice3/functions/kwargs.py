def student(**kwargs):
    print("Name:",kwargs["name"])
    print("Age:",kwargs["age"])
    for key,value in kwargs.items():
        print(key + ":",value)
student(name="Nurken", age = 17 , city = "Shymkent")