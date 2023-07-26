from tkinter import * # import tkinter
from tkinter import messagebox

window = Tk()
window.title("COVID-19 Contact Tracing App") # window title
window.geometry("490x250") # window geometry
window.resizable(False,False) # window not resizable
window.configure(bg="dark red")

# label, description for app
Label(window, text = "COVID-19 Contact Tracing", font = "Impact 30", fg= "white", bg= "dark red").place(x=40, y= 20)
Label(window, text = "This form will help track down people who are being diagnosed with the virus or ", fg= "white", bg= "dark red").place(x= 45, y= 80)
Label(window, text = "experiencing symptoms. This can lead to timely detection and treatment, as well as", fg= "white", bg= "dark red").place(x= 15, y= 97)
Label(window, text = "preventing it from spreading further.", fg= "white", bg= "dark red").place(x= 15, y= 114)

def search_names(): # function to open window 3
    search_name = entry_search.get().lower()
    if search_name:
        # read file
        with open("COVID-19 cases.txt", "r") as file:
            found_entries = []
            # for every line in file find the entry 
            for line in file:
                data = line.strip().split(",")
                first_name, last_name, *_ = line.strip().split(",")
                if search_name.lower() in first_name.lower() or search_name.lower() in last_name.lower():
                    # Check if data has at least 18 elements before accessing index 12 and 13
                    if len(data) >= 18:
                        entry = f"Name: {first_name} {data[2]} {last_name}\n" \
                                f"Sex: {data[3]}\n" \
                                f"Date of Birth: {data[4]}\n" \
                                f"Phone Number: {data[5]}\n" \
                                f"Address: {data[6]}\n" \
                                f"Date of Submission: {data[7]}\n" \
                                f"Health: {data[8]}\n" \
                                f"Symptoms: {', '.join([symptom for symptom, var in zip(['Fever', 'Cough', 'Breathing Difficulty', 'Loss of taste/smell'], data[8:12]) if var == '1'])}\n" \
                                f"Date of Onset: {data[12]}\n" \
                                f"Places: {data[13]}\n" \
                                f"Emergency Contact Information:\n" \
                                f"Name: {data[14]}\n" \
                                f"Phone: {data[15]}\n" \
                                f"Relationship: {data[16]}\n" \
                                f"Address: {data[17]}\n\n"
                    else:
                        # Handle cases where the data is not complete
                        entry = f"Name: {first_name} {last_name}\nData is incomplete.\n\n"

                    found_entries.append(entry)

            if found_entries:
                result_window = Toplevel()
                result_window.title("Data Results")
                result_window.geometry("350x600")
                result_window.resizable(False, False)
                result_window.configure(bg="gray")
                text = Text(result_window, width=40, height=36)
                text.place(x=10, y=10)

                for entry in found_entries:
                    text.insert(END, entry)
            else:
                messagebox.showinfo("No Match", "No matching entries found.")
    else:
        messagebox.showwarning("Search Error", "Please enter a name to search.")

entry_search = Entry(window, width= 30, bd= 3)
entry_search.place(x= 117, y= 155)
button_search = Button(window, text= "Search", font = "verdana 8 bold", width = 8, bd = 4, command= search_names)
button_search.place(x= 305, y= 153)

def open_window2(): # function to open window 2
    def add_data(): # function to append information into file
        first_name = entry_first_name.get()
        middle_name = entry_middle_name.get()
        last_name = entry_last_name.get()
        DoBirth = entry_date_of_birth.get()
        Number = entry_number.get()
        Sex = sex.get()
        Address = entry_address.get()
        DoSubmission = entry_date_of_submission.get()
        Health = health.get()
        Symptoms = ",".join([symptom for symptom, var in [
        ("Fever", symptom_fever.get()),
        ("Cough", symptom_cough.get()),
        ("Breathing Difficulty", symptom_breathing_difficulty.get()),
        ("Loss of taste/smell", symptom_loss_of_taste_smell.get())] if var == 1])
        DoOnset = entry_date_of_onset.get()
        Places = entry_text_places.get("1.0", "end")
        Name = entry_name.get()
        Phone = entry_phone.get()
        Relationship = entry_relationship.get()
        Address2 = entry_address2.get()

        # Check if any of the required fields are empty
        if not (first_name and last_name and DoBirth and Number and Sex and Address and DoSubmission and Health and Symptoms and DoOnset and Places and Name and Phone and Relationship and Address2):
            messagebox.showwarning("Incomplete Data", "Please fill in all the fields.")
        else:
            # Save the data to the file
            with open("COVID-19 cases.txt", "a") as file:
                file.write(f"{first_name},{middle_name},{last_name},{DoBirth},{Number},{Sex},{Address},{DoSubmission},{Health},{Symptoms},{DoOnset},{Places},{Name},{Phone},{Relationship},{Address2}\n")
            messagebox.showinfo("Success", "Data added successfully!")

    window2 = Toplevel()
    window2.title("COVID-19 Contact Tracing Form")
    window2.geometry("500x670")
    window2.configure(bg="gray")
    window2.resizable(False,False)

    frame1 = Frame(window2, width= 480, height= 205, highlightbackground= "dark red", highlightthickness= 2)
    frame1.place(x= 10, y= 10)
    # label for contact details
    Label(frame1, text = "Contact Details", font = "verdana 12 bold").place(x= 5, y= 5)
        
    # label, for name
    Label(frame1, text = "First Name", font = "verdana 8 bold").place(x= 10, y= 35)
    Label(frame1, text = "Middle Name", font = "verdana 8 bold").place(x= 168, y= 35)
    Label(frame1, text = "Last Name", font = "verdana 8 bold").place(x= 325, y= 35)
    # entry, for name
    entry_first_name = Entry(frame1, width = 23)
    entry_middle_name = Entry(frame1, width = 23)
    entry_last_name = Entry(frame1, width = 23)
    entry_first_name.place(x= 10, y= 55)
    entry_middle_name.place(x= 168, y= 55)
    entry_last_name.place(x= 325, y= 55)

    # label, for date of birth
    Label(frame1, text = "Date of Birth", font = "verdana 8 bold").place(x= 10, y= 85)
    Label(frame1, text = "(MM/DD/YYYY)", font = "verdana 7").place(x= 10, y= 100)
    # entry, for date of birth
    entry_date_of_birth = Entry(frame1, width = 14)
    entry_date_of_birth.place(x= 10, y= 120)

    # label, for date of submission
    Label(frame1, text = "Date of Submission ", font = "verdana 8 bold").place(x= 115, y= 85)
    Label(frame1, text = "(MM/DD/YYYY)", font = "verdana 7").place(x= 115, y= 100)
    # entry, for date of submission
    entry_date_of_submission = Entry(frame1, width = 21)
    entry_date_of_submission.place(x= 115, y= 120)

    # label, for phone number
    Label(frame1, text = "Phone Number", font = "verdana 8 bold").place(x= 260, y= 85)
    # entry, for phone number
    entry_number = Entry(frame1, width = 16)
    entry_number.place(x= 260, y= 120)

    # label, for sex
    Label(frame1, text = "Sex", font = "verdana 8 bold").place(x= 380, y= 85)
    # radiobutton, for sex
    sex = StringVar()
    Radiobutton(frame1, text = "Male", variable = sex, value = "Male").place(x= 385, y= 100)
    Radiobutton(frame1, text = "Female", variable = sex, value = "Female").place(x= 385, y= 120)
    
    # label, for address
    Label(frame1, text = "Address", font = "verdana 8 bold").place(x= 10, y= 150)
    entry_address = Entry(frame1, width = 75)
    entry_address.place(x= 10, y= 170)

    frame2 = Frame(window2, width= 480, height= 250, highlightbackground= "dark red", highlightthickness= 2)
    frame2.place(x= 10, y= 225)
    # label for health details
    Label(frame2, text = "Health Details", font = "verdana 12 bold").place(x= 5, y= 5)
    Label(frame2, text = "Select that applies to your situation:", font = "verdana 8 bold").place(x= 10, y= 35)

    health = StringVar()  
    # radiobutton, when diagnosed with COVID 19
    Radiobutton(frame2, text = "Diagnosed with COVID-19", variable = health, value = "Diagnosed").place(x= 10, y= 50)
    # radiobutton, when showing symptoms of COVID 19
    Radiobutton(frame2, text = "Showing COVID-19 symptoms", variable = health, value = "Showing").place(x= 10, y= 70)

    # Create separate IntVar() variables for each symptom
    symptom_fever = IntVar()
    symptom_cough = IntVar()
    symptom_breathing_difficulty = IntVar()
    symptom_loss_of_taste_smell = IntVar()    
    # Which of the following conditions you currently have during ths time?
    Label(frame2, text = "Which of the following conditions you have during this time?", font = "verdana 8 bold").place(x= 10, y= 99)
    # Checkbuttons for conditions
    Checkbutton(frame2, text="Fever", variable=symptom_fever, onvalue=1, offvalue=0).place(x=10, y=115)
    Checkbutton(frame2, text="Cough", variable=symptom_cough, onvalue=1, offvalue=0).place(x=90, y=115)
    Checkbutton(frame2, text="Breathing Difficulty", variable=symptom_breathing_difficulty, onvalue=1, offvalue=0).place(x=180, y=115)
    Checkbutton(frame2, text="Loss of taste/smell", variable=symptom_loss_of_taste_smell, onvalue=1, offvalue=0).place(x=330, y=115)


    # when it started
    Label(frame2, text = "Date of Onset", font = "verdana 8 bold").place(x= 300, y= 35)
    Label(frame2, text = "(MM/DD/YYYY)", font = "verdana 7").place (x= 300, y= 50)  
    # entry, for date of submission
    entry_date_of_onset = Entry(frame2, width = 15)
    entry_date_of_onset.place(x= 300, y= 70)
        
    # have you traveled to any places when you diagnosed with coronavirus
    Label(frame2, text = "What places have you been when experiencing this symptom/s?", font = "verdana 8 bold").place(x= 10, y= 144)
    Label(frame2, text = "State the details of your travel. (Date, Places, etc.)", font = "verdana 7").place(x= 10, y= 160)
    # entry, for places
    entry_text_places = Text(frame2, width = 56, height = 3)
    entry_text_places.place(x= 10, y= 180)
    

    frame3 = Frame(window2, width= 480, height= 130, highlightbackground= "dark red", highlightthickness= 2)
    frame3.place(x= 10, y= 485)
    # label for emergency contact
    Label(frame3, text = "Emergency Contact Information", font = "verdana 12 bold").place(x= 5, y= 5)
    Label(frame3, text = "Name", font = "verdana 8 bold").place(x= 10, y= 35)
    Label(frame3, text = "Phone ", font = "verdana 8 bold").place(x= 10, y= 55)
    Label(frame3, text = "Relationship", font = "verdana 8 bold").place(x= 10, y= 75)
    Label(frame3, text = "Address", font = "verdana 8 bold").place(x= 10, y= 95)
    
    # entry, for emergency contact information
    entry_name = Entry(frame3, width = 23)
    entry_phone = Entry(frame3, width = 23)
    entry_relationship = Entry(frame3, width = 23)
    entry_address2 = Entry(frame3, width = 23)
    entry_name.place(x= 140, y= 37)
    entry_phone.place(x= 140, y= 57)
    entry_relationship.place(x= 140, y= 77)
    entry_address2.place(x= 140, y= 97)

    # button, to submit
    button_submit = Button(window2, text = "Submit", font = "verdana 13 bold", command= add_data)
    button_submit.place(x=205, y= 625)
        # if submitted, append into file

label_add_data = Label(window, text= "Add Data?", font= "verdana 8", fg= "white", bg= "dark red")
label_add_data.place(x=180, y= 210)
# button, to add information  
button_add_data = Button(window, text= "Click here", font = "verdana 6", fg= "white", bg= "dark red", command= open_window2)
button_add_data.place(x= 250, y= 211)

window.mainloop() # Keep the window open