import tkinter
import customtkinter
from PIL import ImageTk,Image
import database as db
import webbrowser

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("600x440")
app.title('Login')

def button_function1():
	
	value = db.selected()	
	listed = []
	for row in value:
		listed.append(row[0])
	usrnam = entry1.get()
	
	if usrnam in listed:
		passchek = db.check(usrnam)
		
		if entry2.get() == passchek:
			webbrowser.open("http://localhost:8501")

		else:
			tkinter.messagebox.showwarning(title='Wrong password',message='Wrong password')
	else:
		tkinter.messagebox.showerror(title="Login Failed",message="Invalid Username or password")

def button_function2():
	print("hello button 2")

label = customtkinter.CTkLabel(app,text="Portfolio Management")
  
label.pack(pady=20)

    


img1=ImageTk.PhotoImage(Image.open("pic.jpg"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
l2.place(x=50, y=45)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

l3=customtkinter.CTkLabel(master=frame, text="Forget password?",font=('Century Gothic',12))
l3.place(x=155,y=195)

#Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function1, corner_radius=6)
button1.place(x=50, y=240)

button2 = customtkinter.CTkButton(master=frame,width=200, text="Sign-Up", command=button_function2, corner_radius=6)
button2.place(x=60, y=300)

# You can easily integrate authentication system 

app.mainloop()