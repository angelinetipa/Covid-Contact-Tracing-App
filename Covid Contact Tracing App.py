# import tkinter
from tkinter import *
window = Tk()
# window title, geometry
window.title("COVID-19 Contact Tracing App")
window.geometry("490x250")
window.resizable(False,False)

# label, description for app
Label(window, text = "COVID-19 Contact Tracing Form", font = ("verdana", 12, "bold")).place( x= 110, y= 5)
Label(window, text = "This form will help track down people who are being diagnosed with the virus or ").place(x= 45, y= 30)
Label(window, text = "experiencing symptoms. This can lead to timely detection and treatment, as well as").place(x= 15, y= 50)
Label(window, text = "preventing it from spreading further.").place(x= 15, y= 70)

# def openwindow1
def openwindow2():
    window2 = Toplevel()
    window2.title("COVID-19 Contact Tracing Form")
    # label for contact details
    Label(window2, text = "Contact Details", font = ("verdana", 12, "bold", "italic")).place( x= 0, y= 5)
    # entry, for date of submission 
    # entry, for name
    # entry, for date of birth
    # entry, for gender
    # entry, for phone number
    # entry, for address
    

# button, to add information
bttn1 = Button(window, text= "Add Information", font = ("verdana", 12), command= openwindow2).place(x= 170, y= 100)
    

    # label for health details
    # checkbutton, for current situation
        # if diagnosed with Coronavirus
            # when it started
            # have you traveled to any places when you diagnosed with coronavirus
                # if yes state the details of your travel
        # if showing coronavirus symptoms
            # when it started
            # What conditions you currently have during this time? (Check all that apply)
            # have you traveled to any places when you diagnosed with coronavirus
                # if yes state the details of your travel

    # label for emergency contact
    # entry, for emergency contact information
    # button, to submit
        # if submitted, append into file

# button, to search entries
    # entry to search names
        # for all info in files
            # if the name in data
                # display that its already submitted

window.mainloop()