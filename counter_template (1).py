"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       hamed talebian
Email:      hamed.talebian@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:
    def __init__(self):
        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        self.__counter = 0
        self.__main_window = Tk()
        
        self.__current_value_label = Label(self.__main_window, text=self.__counter)  # Label displaying the current value of the counter.
        self.__current_value_label.grid(row=0,column=1,columnspan=3)
        
        self.__reset_button = Button(self.__main_window, text="Reset", command=self.reset)        # Button which resets counter to zero.
        self.__reset_button.grid(row=1, column=1)
        
        self.__increase_button = Button(self.__main_window, text="Increase", command=self.increase)     # Button which increases the value of the counter by one.
        self.__increase_button.grid(row=1,column=2)
        
        self.__decrease_button = Button(self.__main_window, text="Decrease", command=self.decrease)      # Button which decreases the value of the counter by one.
        self.__decrease_button.grid(row=1, column=3)
        
        self.__quit_button  = Button(self.__main_window, text="Quit", command=self.quit)        # Button which quits the program.
        self.__quit_button.grid(row=1, column=4)
        
        self.__main_window.mainloop()
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.

    # TODO: Implement the rest of the needed methods here.
    def quit(self):
        self.__main_window.destroy()
    def reset(self):
        self.__main_window.reset()
    def increase(self):
        self.__main_window.increase()
    def decrease(self):
        self.__main_window.decrease()

    def set_current_value_label(self):
        self.__current_value_label.configure(text=self.__counter)
    
    def reset(self):
        self.__counter = 0
        self.set_current_value_label()
    def increase(self):
        self.__counter += 1
        self.set_current_value_label()
    def decrease(self):
        self.__counter -= 1
        self.set_current_value_label()

def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.
    Counter()


if __name__ == "__main__":
    main()
