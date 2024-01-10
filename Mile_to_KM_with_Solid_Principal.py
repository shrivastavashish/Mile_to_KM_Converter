from tkinter import *
from abc import ABC, abstractmethod

# Interface for converters
class Converter(ABC):
    @abstractmethod
    def convert(self, value):
        pass

# Miles to Kilometers converter
class MilesToKmConverter(Converter):
    def convert(self, miles):
        return miles * 1.609

# GUI class adhering to SRP
class MilesToKmConverterGUI:
    def __init__(self, converter):
        self.converter = converter
        self.setup_gui()

    def miles_to_km(self):
        try:
            miles = float(self.miles_input.get())
            km = round(self.converter.convert(miles), 2)
            self.kilo_result_label.config(text="{:.2f}".format(km))
        except ValueError:
            self.kilo_result_label.config(text="Invalid Input")

    def setup_gui(self):
        self.window = Tk()
        self.window.title("Miles to Kilometers Converter")
        self.window.geometry("400x100")
        self.window.config(padx=20, pady=20)
        self.window.config(bg="light blue")

        self.miles_input = Entry(width=7)
        self.miles_input.grid(column=1, row=0)

        miles_label = Label(text="Miles", bg="black", fg="white")
        miles_label.grid(column=2, row=0)

        is_equal_label = Label(text="is equal to", bg="black", fg="white")
        is_equal_label.grid(column=0, row=1)

        self.kilo_result_label = Label(text="0.00", bg="black", fg="white")
        self.kilo_result_label.grid(column=1, row=1)

        kilo_output = Label(text="Km", bg="black", fg="white")
        kilo_output.grid(column=2, row=1)

        calc_button = Button(text="Calculate", bg="red", command=self.miles_to_km)
        calc_button.grid(column=1, row=2)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    converter = MilesToKmConverter()
    app = MilesToKmConverterGUI(converter)
    app.run()