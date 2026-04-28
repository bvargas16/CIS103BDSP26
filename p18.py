# Brian Vargas Temperature Conversion GUI Window
from tkinter import *
from tkinter import messagebox
import math

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

def main():
    winmain = Tk()
    winmain.geometry('800x600+600+300')
    winmain.title('Temperature Converter')
    winmain.configure(bg='lightblue')
    lbltext = Label(winmain, text='Temperature Converter',
                    fg = 'yellow',
                    bg = 'black', 
                    font=('Arial Bold', 30))
    lbltext.place(x=230, y=1)

    lbltext2 = Label(winmain, text='Enter temperature in Kelvin:',
                    fg = 'black',
                    bg = 'lightblue',
                    font=('Arial Bold', 20))
    lbltext2.place(x=60, y=80)

    lbltext3 = Label(winmain, text='Kelvin to Celsius:',
                    fg = 'black',
                    bg = 'lightblue',
                    font=('Arial Bold', 20))
    lbltext3.place(x=120, y=200)

    lbltext4 = Label(winmain, text='Kelvin to Fahrenheit:',
                    fg = 'black',
                    bg = 'lightblue',
                    font=('Arial Bold', 20))
    lbltext4.place(x=120, y=320)
    
    txtbox1 = Entry(winmain, width=10, font=('Arial Bold', 30))
    txtbox1.place(x=450, y=70)

    txtbox1.bind("<Return>", lambda event: calculate())

    txtbox2 = Entry(winmain, width=10, font=('Arial Bold', 30))
    txtbox2.place(x=450, y=190)

    txtbox3 = Entry(winmain, width=10, font=('Arial Bold', 30))
    txtbox3.place(x=450, y=310)

    # messagebox.showinfo('Quit message', 'Press quit button to exit')
    def calculate():
            val = txtbox1.get().strip()
        
            if val == "":
                messagebox.showerror("Input Error", "Kelvin cannot be blank.")
                return
            try:
                kelvin = float(val)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid number for Kelvin.")
                return
            if kelvin <= 0:
                messagebox.showerror("Input Error", "Kelvin cannot be zero or negative.")
                return
            
            txtbox2.insert(0, round(kelvin_to_celsius(kelvin), 2))
            txtbox3.insert(0, round(kelvin_to_fahrenheit(kelvin), 2))


    btn1 = Button(winmain, text='Calculate', command = calculate)
    btn1.place(x=290, y=450)

    btn2 = Button(winmain, text='Clear',
                   command = lambda: [txtbox1.delete(0, END), txtbox2.delete(0, END), txtbox3.delete(0, END)])
    btn2.place(x=400, y=450)
    
    btn3 = Button(winmain, text='QUIT',
                  command = quit)
    btn3.place(x=350, y=500)
    
    winmain.mainloop()
main()