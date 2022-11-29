
class Character:
    # TODO: the class implementation goes here.
    def __init__(self, name):
        
        self.get_name(name)
        #self.give_item(item)

    def get_name(self, name):
        self.__name = name
    
    def printout(self):
        print(f"name: {self.__name}")

def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    character1.printout()
    character2.printout()

if __name__ == "__main__":
    main()