class User:
    def __init__(self):
        self.weight = None
        self.height = None
        self.sex = None
        self.age = None

    def update(self, weight, height, sex, age):
        self.weight = weight
        self.height = height
        self.sex = sex
        self.age = age
        print(f"Weight: {self.weight}, Height: {self.height}, Sex: {self.sex}, Age: {self.age}")
