class person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"{self.name}({self.age})({self.height})"


class Student(person):
    def __init__(self, name, age, height, av_marks, grade):
        super().__init__(name, age, height)
        self.av_marks = av_marks
        self.grade = grade

    def info(self):
        print("My name is", "", self.name, ",", "Am", "", self.age, "", "years old", "", "and", "", self.height, "",
              "feet tall.")


class Credits(Student):
    def education(self):
        print("Am {},{} years old and {} feet tall,my average marks is {} representing a {},I feel great".format(
                self.name, self.age, self.height, self.av_marks, self.grade))


st1 = Credits("Ezra", 20, 6, "365", "B")
st2 = Credits("Fatma", 19, 5, "390", "B+")

print(st1)
print(st2)
st1.info(), st1.education()
st2.info(), st2.education()
