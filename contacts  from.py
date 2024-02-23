import tkinter as tk

class ContactForm:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Contact Information Form")

        # Create a Frame to hold the form elements
        self.form_frame = tk.Frame(parent, padx=20, pady=20)
        self.form_frame.pack()

        # Create labels and Entry widgets for the contact form
        self.name_label = tk.Label(self.form_frame, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")
        
        self.name_entry = tk.Entry(self.form_frame)
        self.name_entry.grid(row=0, column=1)

        self.email_label = tk.Label(self.form_frame, text="Email:")
        self.email_label.grid(row=1, column=0, sticky="w")

        self.email_entry = tk.Entry(self.form_frame)
        self.email_entry.grid(row=1, column=1)

        self.phone_label = tk.Label(self.form_frame, text="Phone:")
        self.phone_label.grid(row=2, column=0, sticky="w")

        self.phone_entry = tk.Entry(self.form_frame)
        self.phone_entry.grid(row=2, column=1)

        self.hobby_label = tk.Label(self.form_frame, text="Hobby:")
        self.hobby_label.grid(row=3, column=0, sticky="w")
        
        self.hobby_entry = tk.Entry(self.form_frame)
        self.hobby_entry.grid(row=3, column=1)

        # Create a Submit button
        self.submit_button = tk.Button(self.form_frame, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=3, columnspan=2, pady=10)

    def submit_form(self):
        # Retrieve and display the submitted data
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        hobby = self.hobby_entry.get()
        

        # Display the submitted data in a message box
        messagebox.showinfo("Submitted Information", message)
        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nhobby: {hobby}"
        tk.messagebox.showinfo("Submitted Information", message)

if __name__ == "__main__":
    parent = tk.Tk()
    app = ContactForm(parent)
    parent.mainloop()
