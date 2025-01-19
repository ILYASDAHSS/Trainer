class Trainer:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_average(self):
        if len(self.grades) == 0:
            average = 0.0
        else:
            average = sum(self.grades) / len(self.grades)

        print(f"Average of {self.name}: {average}")

        if 10 <= average < 12:
            print("Satisfactory")
        elif 12 <= average < 14:
            print("Fairly Good")
        elif 14 <= average < 16:
            print("Good")
        elif average >= 16:
            print("Very Good")
        else:
            print("Insufficient Average")

        return average


grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))


trainee = Trainee("Ilyas", [grade1, grade2])
trainee.calculate_average()