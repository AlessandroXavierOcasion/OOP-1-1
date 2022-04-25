#Program 1: Modify the program below by adding two conversion methods - Fahrenheit to Celsius and Kelvin to Celsius (50 points)
def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp
 class CelsiusToFahrenheit(TemperatureConversion):
  def conversion(self):
   return (self._temp * 9) / 5 + 32
 class CelsiusToKelvin(TemperatureConversion):
  def conversion(self):
   return self._temp + 273.15
 class FahrenheitToCelsius(TemperatureConversion):
  def conversion(self):
   return ((self._temp - 32) * 5) / 9
 class KelvinToCelsius(TemperatureConversion):
  def conversion(self):
   return self._temp - 273.15

 tempInCelsius = float(input("Enter the temperature in Celsius: "))
 convert = CelsiusToKelvin(tempInCelsius)
 print(str(convert.conversion()) + " Kelvin")
 convert = CelsiusToFahrenheit(tempInCelsius)
 print(str(convert.conversion()) + " Fahrenheit")
 tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
 convert = FahrenheitToCelsius(tempInFahrenheit)
 print(str(convert.conversion()) + " Celsius")
 tempInKelvin = float(input("Enter the temperature in Kelvin: "))
 convert = KelvinToCelsius(tempInKelvin)
 print(str(convert.conversion()) + " Celsius")


main()
#Program 2. Create a program to produce the interface. After typing the name in the first text field, click the button to display the name to another text field. (Hint: See the figures.  - 50 points)
import tkinter
from tkinter import*

window = Tk()
window.title("Midterm in OOP")
window.geometry("500x400+30+20")

lbl = Label(window, text="Enter your Fullname:", fg="red")
lbl.place(x=80, y=110)

txtfld = Entry(window, bd=4, font=("verdana", 16))
txtfld.place(x=200, y=100)

txtfld2 = Entry(window, bd=4, font=("verdana", 16))
txtfld2.place(x=200, y=220)

def clicked():
    value=txtfld.get()
    txtfld2.insert(END, str(value))

bttn= Button(window, text="Click to display your Fullname", fg="red", command=clicked)
bttn.place(x=20, y=225)

window.mainloop()

