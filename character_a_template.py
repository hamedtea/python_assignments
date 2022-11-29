"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""

class Character:
    # TODO: the class implementation goes here.
    def __init__(self, name):
        
        self.__name = name
        self.__item_list = []
        self.__check_list = []
    
    def get_name(self):
        return self.__name
    
    def give_item(self, item):
            self.__item_list.append(item)
            if item not in self.__check_list:
                self.__check_list.append(item)
            else:
                pass
    def check_item(self, item):
        if item not in self.__check_list:
            self.__check_list.append(item)
        else:
            pass



    def remove_item(self, item):
        self.__item_list.remove(item)
    
    def has_item(self, item):
        if item in self.__item_list:
            return True
        else:    
            return False
    
    def how_many(self, item):
        return self.__item_list.count(item)
    
    def printout(self):
        print(f"Name: {self.get_name()}")
        for i in sorted(self.__check_list):
            if self.how_many(i) == 0: 
                pass
            else:
                print(f"  {self.how_many(i)} {i}")
        
        if len(self.__item_list) == 0:
            print("  --nothing--")
        else:
            pass
def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    
    character1.remove_item("sausage")
    character2.remove_item("hero outfit")
    
    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
