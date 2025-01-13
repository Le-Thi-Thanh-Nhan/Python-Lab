class Animal:
    def __init__(self, name = '', sound = ''):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f'{self.name} goes {self.sound}')
    
class Dog(Animal):
    def __init__(self, name = '', sound = '', breed = ''):
        super().__init__(name, sound)
        self.breed = breed
    
    def HienThi(self):
        print(f'Name: {self.name}, Sound: {self.sound}, Breed: {self.breed}')
    
dog = Dog('Dog', 'Bark', 'Husky')
dog.HienThi()
dog.make_sound()