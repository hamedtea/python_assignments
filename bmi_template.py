"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *
from tkinter.font import nametofont


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow)

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow)

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text="calculate the BMI", background="green", foreground="red",
                                                            command=self.calculate_BMI)

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(text="your BMI is calculated here!")

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(text="Body mass index is your weight divided by your squared height")

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text="push this button to quit", command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_value.grid(row=0, column=0)
        self.__height_value.grid(row=0, column=1)
        self.__calculate_button.grid(row=3, column=0, sticky=E+W)
        self.__stop_button.grid(row=3, column=1)
        self.__result_text.grid(row=2, column=0, columnspan=1,sticky=E+W)
        self.__explanation_text.grid(row=1, column=0, columnspan=2, sticky=E+W)

    # TODO: Implement this method.
    def get_weight_and_height_value(self):
        try:
            weight_value = float(self.__weight_value.get())
            height_value = float(self.__height_value.get())
        except ValueError:
            self.reset_fields() 
        
        return (weight_value, height_value)
    
            
    def check_error(self):
        if self.__weight_value < 0: 
            if self.__height_value < 0:
                self.reset_fields()
            else:
                pass
        else:
            pass
        return

    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        (w, h) = self.get_weight_and_height_value()
        self.__BMI = w/(h*h)
        self.set_result_text()

    def set_result_text(self):
        if self.__BMI <= 18.5:
            self.__result_text.configure(text=f"your BMI is {self.__BMI:.2f}. You are underweight.")
        elif self.__BMI <= 25: 
            self.__result_text.configure(text=f"your BMI is {self.__BMI:.2f}. Your weight is normal.")
        else:
            self.__result_text.configure(text=f"your BMI is {self.__BMI:.2f}. You are overweight.")



    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """


        """if self.weight_value < 0 or self.height_value < 0:
            self.__result_text.configure(text=f"NAN")
            self.__explanation_text.configure(text="Error: height and weight must be positive.") 
        else:"""
        self.__result_text.configure(text=f"NAN")
        self.__explanation_text.configure(text="Error: height and weight must be numbers.")
        self.__weight_value = Entry(self.__mainwindow)
        self.__height_value = Entry(self.__mainwindow) 
    
    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
