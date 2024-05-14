class User:
    def __init__(self, weight=None, height=None, sex=None, age=None):
        self.weight = weight
        self.height = height
        self.sex = sex
        self.age = age

    def update(self, weight, height, sex, age):
        self.weight = weight
        self.height = height
        self.sex = sex
        self.age = age
        print(f"Weight: {self.weight}, Height: {self.height}, Sex: {self.sex}, Age: {self.age}")

    def to_dict(self):
        return {
            "weight": self.weight,
            "height": self.height,
            "sex": self.sex,
            "age": self.age
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            weight=data.get('weight'),
            height=data.get('height'),
            sex=data.get('sex'),
            age=data.get('age')
        )
