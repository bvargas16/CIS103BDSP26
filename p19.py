from tkinter import *
def main():
    mainwin = Tk()
    color = 'white'
    wcan = Canvas(mainwin, bg = color,
                  width=650, height=800)
    wcan.pack()

    #Skinny Rectangle
    wcan.create_rectangle(150,380,500,450,
                fill='yellow', outline='black', width=5)

    #First Medium Circle
    wcan.create_oval(150,150,300,300,
                fill='red', outline='black', width=5)
    
    # Second Medium Circle
    wcan.create_oval(350,150,500,300,
                fill='blue', outline='black', width=5)
    
    #Third Huge Circle
    wcan.create_oval(10,10,650,650,
                outline='green', width=3)
    
    # Black Polygon
    wcan.create_polygon(200,580,500,580,350,700,
                outline='black', width=50)
    
    
    mainwin.mainloop()
main()