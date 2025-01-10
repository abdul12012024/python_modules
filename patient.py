class Patient:
    def __init__(self, name, age, bed_number):
        self.name = name
        self.age = age
        self.bed_number = bed_number

    def describe(self):
        print(f"Patient Name: {self.name}, Age: {self.age}, bed_number: {self.bed_number}")
