class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print('danger')

    
    def eats(self, eat):
        print(f"Animal eats {eat}")


class Pet(Animal):
    # method overriding
    def sound(self):
        print("friendly")


dog = Pet('Max')
dog.sound()
dog.eats('meat')
