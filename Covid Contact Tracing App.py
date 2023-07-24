# import tkinter
from tkinter import *
window = Tk()
# window title, geometry
window.title("COVID-19 Contact Tracing App")
window.geometry("500x600")
# label, description for app
Label(window, text = "COVID-19 Contact Tracing Form", font = ("verdana", 12, "bold")).place(x=100, y=10)
# button, to add information

    # label for contact details
    # entry, for date of submission
    # entry, for name
    # entry, for date of birth
    # entry, for gender
    # entry, for phone number
    # entry, for address

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