import customtkinter as ctk
from customtkinter import CTkButton

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title("Ticket System")
app.geometry('300x500')

label_ticket = ctk.CTkLabel(app,text='Ticket Party',)
label_ticket.pack(pady=30)


app.mainloop()

