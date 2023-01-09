class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hello, my name is", self.name,
              "and I am", self.age, "years old!")


Ibukun = person("Ibukun", 26)
print(Ibukun.speak())
