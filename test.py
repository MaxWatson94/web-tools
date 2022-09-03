from tkinter import *
import time
 
def collectdata():
    ports = [1, 2, 3, 4, 5]
    ##length = len(ports)
    for p in ports:
        currentport.insert(END, p)
        window.update_idletasks()
        time.sleep(2)
 
window = Tk()
window.title("Pressure Scanner")
window.geometry('300x300')
 
button = Button(window, text = "Collect Data", command = collectdata).pack()
 
Label(window, text = "Output below should update every loop cycle")
 
Label(window, text = "Current Port").pack()
currentport = Listbox(window)
currentport.pack()
 
window.mainloop()