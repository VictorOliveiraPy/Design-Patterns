from abc import  ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def speaker(self):
        pass


class Dog(Animal):
    def speaker(self):
        print('AU Au')


class Cat(Animal):
    def speaker(self):
        print('Miau!')


class Camel(Animal):
    def speaker(self):
        print('Python >>>>>>')


class Manufactures:
    def create_animal_speaker(self, kind):
        return eval(kind)().speaker()


if __name__ == '__main__':
    fact = Manufactures()
    animal = input('Qual animal voce quer que fale? [Cachorro, Gato, Camelo]')
    fact.create_animal_speaker(animal)
