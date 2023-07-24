# import tkinter
from tkinter import *
window = Tk()
# window title, geometry
window.title("COVID-19 Contact Tracing App")
window.geometry("490x250")
window.resizable(False,False)

# label, description for app
Label(window, text = "COVID-19 Contact Tracing Form", font = ("verdana", 12, "bold")).place(x= 110, y= 5)
Label(window, text = "This form will help track down people who are being diagnosed with the virus or ").place(x= 45, y= 30)
Label(window, text = "experiencing symptoms. This can lead to timely detection and treatment, as well as").place(x= 15, y= 50)
Label(window, text = "preventing it from spreading further.").place(x= 15, y= 70)

# def openwindow1
def openwindow2():
    window2 = Toplevel()
    window2.title("COVID-19 Contact Tracing Form")
    window2.geometry("490x600")
    window2.resizable(False,False)
    # label for contact details
    Label(window2, text = "Contact Details", font = ("verdana", 12, "bold")).place(x= 5, y= 5)

    # label, for name
    Label(window2, text = "First Name", font = ("verdana", 8, "bold")).place(x= 10, y= 35)
    Label(window2, text = "Middle Name", font = ("verdana", 8, "bold")).place(x= 170, y= 35)
    Label(window2, text = "Last Name", font = ("verdana", 8, "bold")).place(x= 330, y= 35)
    # entry, for name
    Entry(window2, width = 23).place(x= 10, y= 55)
    Entry(window2, width = 23).place(x= 170, y= 55)
    Entry(window2, width = 23).place(x= 330, y= 55)


    # label, for date of birth
    Label(window2, text = "Date of Birth", font = ("verdana", 8, "bold")).place(x= 10, y= 85)
    Label(window2, text = "(MM/DD/YYYY)", font = ("verdana", 7)).place(x= 10, y= 100)
    # entry, for date of birth
    Entry(window2, width = 15).place(x= 10, y= 120)
    # label, for date of submission
    Label(window2, text = "Date of Submission ", font = ("verdana", 8, "bold")).place(x= 130, y= 85)
    Label(window2, text = "(MM/DD/YYYY)", font = ("verdana", 7)).place(x= 130, y= 100)
    # entry, for date of submission
    Entry(window2, width = 22).place(x= 130, y= 120)


    # label, for sex
    Label(window2, text = "Sex", font = ("verdana", 8, "bold")).place(x= 290, y= 85)
    # entry, for sex
    Entry(window2, width = 5).place(x= 290, y= 120)


    # label, for phone number
    Label(window2, text = "Phone Number", font = ("verdana", 8, "bold")).place(x= 350, y= 85)
    # entry, for phone number
    Entry(window2, width = 17).place(x= 350, y= 120)

    # label, for address
    Label(window2, text = "Address", font = ("verdana", 8, "bold")).place(x= 10, y= 150)
    Entry(window2, width = 77).place(x= 10, y= 170)


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