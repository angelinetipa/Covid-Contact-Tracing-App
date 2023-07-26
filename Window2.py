from tkinter import * # import tkinter
class Window:
    
    def open(): # function to open window 2
        def add_data(): # function to append information into file
            FName = first_name.get()
            MName = middle_name.get()
            LName = last_name.get()
            DoBirth = date_of_birth.get()
            Number = number.get()
            Sex = Sex.get()
            Address = address.get()
            DoSubmission = date_of_submission.get()

            with open("COVID-19 cases.txt", "w") as infofile:
                infofile.write(f"""Name: {FName} {MName} {LName}  
                            Date of Birth: {DoBirth}  
                            Phone: {Number}  
                            Sex: {Sex}  
                            Address: {Address}  
                            Date of Submission: {DoSubmission}""") 
                           
        window2 = Toplevel()
        window2.title("COVID-19 Contact Tracing Form")
        window2.geometry("490x640")
        window2.resizable(False,False)

        
            
        
        # label for contact details
        Label(window2, text = "Contact Details", font = "verdana 12 bold").place(x= 5, y= 5)
        
        # label, for name
        Label(window2, text = "First Name", font = "verdana 8 bold").place(x= 10, y= 35)
        Label(window2, text = "Middle Name", font = "verdana 8 bold").place(x= 170, y= 35)
        Label(window2, text = "Last Name", font = "verdana 8 bold").place(x= 330, y= 35)
        # entry, for name
        first_name = Entry(window2, width = 23).place(x= 10, y= 55)
        middle_name = Entry(window2, width = 23).place(x= 170, y= 55)
        last_name = Entry(window2, width = 23).place(x= 330, y= 55)

        # label, for date of birth
        Label(window2, text = "Date of Birth", font = "verdana 8 bold").place(x= 10, y= 85)
        Label(window2, text = "(MM/DD/YYYY)", font = "verdana 7").place(x= 10, y= 100)
        # entry, for date of birth
        date_of_birth = Entry(window2, width = 15).place(x= 10, y= 120)

        # label, for date of submission
        Label(window2, text = "Date of Submission ", font = "verdana 8 bold").place(x= 130, y= 85)
        Label(window2, text = "(MM/DD/YYYY)", font = "verdana 7").place(x= 130, y= 100)
        # entry, for date of submission
        date_of_submission = Entry(window2, width = 22).place(x= 130, y= 120)
    
        # label, for phone number
        Label(window2, text = "Phone Number", font = "verdana 8 bold").place(x= 290, y= 85)
        # entry, for phone number
        number = Entry(window2, width = 17).place(x= 280, y= 120)

        # label, for sex
        Label(window2, text = "Sex", font = "verdana 8 bold").place(x= 400, y= 85)
        # radiobutton, for sex
        Sex = StringVar()
        Radiobutton(window2, text = "Male", variable = Sex, value = "Male").place(x= 400, y= 100)
        Radiobutton(window2, text = "Female", variable = Sex, value = "Female").place(x= 400, y= 120)
    
        # label, for address
        Label(window2, text = "Address", font = "verdana 8 bold").place(x= 10, y= 150)
        address = Entry(window2, width = 77).place(x= 10, y= 170)

        # label for health details
        Label(window2, text = "Health Details", font = "verdana 12 bold").place(x= 5, y= 220)
        Label(window2, text = "Select that applies to your situation:", font = "verdana 8 bold").place(x= 10, y= 250)

        Health = StringVar()  
        # radiobutton, when diagnosed with COVID 19
        Radiobutton(window2, text = "Diagnosed with COVID-19", variable = Health, value = "Diagnosed").place(x= 10, y= 265)
        # radiobutton, when showing symptoms of COVID 19
        Radiobutton(window2, text = "Showing COVID-19 symptoms", variable = Health, value = "Showing").place(x= 10, y= 285)
            
        # Which of the following conditions you currently have during ths time?
        Label(window2, text = "Which of the following conditions you have during this time?", font = "verdana 8 bold").place(x= 10, y= 310)
        # chechbutton for conditions
        Checkbutton(window2, text = "Fever").place(x= 10, y= 325)  
        Checkbutton(window2, text = "Cough").place(x= 80, y= 325)  
        Checkbutton(window2, text = "Breathing Difficulty").place(x= 160, y= 325)  
        Checkbutton(window2, text = "Loss of taste/smell").place(x= 305, y= 325)  

        # when it started
        Label(window2, text = "Date of Onset", font = "verdana 8 bold").place(x= 300, y= 250)
        Label(window2, text = "(MM/DD/YYYY)", font = "verdana 7").place (x= 300, y= 265)  
        # entry, for date of submission
        Entry(window2, width = 15).place(x= 300, y= 285)

        # have you traveled to any places when you diagnosed with coronavirus
        Label(window2, text = "What places have you been when experiencing this symptom/s?", font = "verdana 8 bold").place(x= 10, y= 350)
        Label(window2, text = "State the details of your travel. (Date, Places, etc.)", font = "verdana 7").place(x= 10, y= 365)
        # entry, for date of submission
        Text(window2, width = 58, height = 3).place(x= 10, y= 385)
        
        # label for emergency contact
        Label(window2, text = "Emergency Contact Information", font = "verdana 12 bold").place(x= 5, y= 465)
        Label(window2, text = "Name", font = "verdana 8 bold").place(x= 10, y= 495)
        Label(window2, text = "Phone ", font = "verdana 8 bold").place(x= 10, y= 515)
        Label(window2, text = "Address", font = "verdana 8 bold").place(x= 10, y= 535)
        Label(window2, text = "Relationship", font = "verdana 8 bold").place(x= 10, y= 555)
        # entry, for emergency contact information
        Entry(window2, width = 23).place(x= 140, y= 495)
        Entry(window2, width = 23).place(x= 140, y= 515)
        Entry(window2, width = 23).place(x= 140, y= 535)
        Entry(window2, width = 23).place(x= 140, y= 555)

        
        # button, to submit
        bttn3 = Button(window2, text = "Submit", font = "verdana 10 bold", command= add_data).place(x=210, y= 600)
            # if submitted, append into file