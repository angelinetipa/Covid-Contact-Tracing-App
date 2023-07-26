from tkinter import * # import tkinter
from Window2 import Window

window = Tk()
window.title("COVID-19 Contact Tracing App") # window title
window.geometry("490x250") # window geometry
window.resizable(False,False) # window not resizable

# label, description for app
Label(window, text = "COVID-19 Contact Tracing Form", font = "verdana 12 bold").place(x= 110, y= 5)
Label(window, text = "This form will help track down people who are being diagnosed with the virus or ").place(x= 45, y= 30)
Label(window, text = "experiencing symptoms. This can lead to timely detection and treatment, as well as").place(x= 15, y= 50)
Label(window, text = "preventing it from spreading further.").place(x= 15, y= 70)

window2 = Window()
# button, to add information
bttn1 = Button(window, text= "Add Information", font = "verdana 12", command= window2.open).place(x= 170, y= 100)

def openwindow3(): # function to open window 3
    window2 = Toplevel()
    window2.title("COVID-19 Contact Tracing Form")
    window2.geometry("490x600")
    window2.resizable(False,False)
     # entry to search names
        # for all info in files
            # if the name in data
                # display that its already submitted
# button, to search entries
bttn2 = Button(window, text= "Search Information", font = ("verdana", 12), command= openwindow3).place(x= 170, y= 150)

   

window.mainloop() # Keep the window open