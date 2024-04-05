class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def is_adult(self):
        return self.age >= 18

class ScoreData:
    def __init__(self, score1, score2, score3, score4, score5):
        self.scores = [score1, score2, score3, score4, score5]

    def total_score(self):
        return sum(self.scores)

def calculate_score(person, score_data):
    total_score = score_data.total_score()
    is_adult = person.is_adult()

    print("Name:", person.name)
    print("Age:", person.age)
    print("Gender:", person.gender)
    print("Height:", person.height)
    print("Weight:", person.weight)
    print("Total Score:", total_score)
    print("Adult:", is_adult)

# Приклад виклику функції
person = Person("John", 25, "Male", 175, 70)
score_data = ScoreData(85, 90, 75, 88, 92)
calculate_score(person, score_data)