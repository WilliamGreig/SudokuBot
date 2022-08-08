
class Food:
    def __init__(self):
        pass

    def __add__(self, other):
        return self.taste + other.taste

    def glorb(self, other):
        pass


class Sandwich(Food):
    def __init__(self, description, taste):
        self.description = description
        self.taste = taste

    def __str__(self):
        return self.description


class Spaghetti(Food):
    def __init__(self, description, pasta_type, taste):
        self.description = description
        self.taste = taste
        self.pasta_type = pasta_type

class Soda:
    def __init__(self):
        pass


ham_sammy = Sandwich("Ham Sandwich", 3)
penne = Spaghetti("Carbonara", "Penne", 5)


