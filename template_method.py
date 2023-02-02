from abc import ABC, abstractmethod

class Chef(ABC):

    def make_pizza(self) -> None:
        self.prepare_dough()
        self.precook_dough()
        self.prepare_ingredients()
        self.adding_ingredients()
        self.cook_pizza()
        self.package_pizza()

    def prepare_dough(self) -> None:
        print("Preparing dough")
    def precook_dough(self) -> None:
        print("Pre cooking dough")
    def cook_pizza(self) -> None:
        print("Sending the pizza to the oven") 
    def package_pizza(self)->None:
        print("Packing the pizza")


    @abstractmethod
    def prepare_ingredients(self) -> None:
        pass
    @abstractmethod
    def adding_ingredients(self) -> None:
        pass

class NoVeggieChef(Chef):
    def prepare_ingredients(self) -> None:
        print("Preparing cheese and ham") 
    def adding_ingredients(self) -> None:
        print("Adding ingredients")           

class VeggieChef(Chef):
    def prepare_ingredients(self) -> None:
        print("Preparing tomatoes, arugula and cheese")
    def adding_ingredients(self) -> None:
        print("Adding tomatoes, arugula and cheese")


def chef(abstract_class: Chef) -> None:
    abstract_class.make_pizza()


chef(NoVeggieChef())
print("\n")
chef(VeggieChef())




