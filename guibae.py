import tkinter
import customtkinter
from PIL import ImageTk,Image
import webbrowser

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("600x440")
app.title('Login')

username = ["arjun","chris","sivaram","lakshmi"]
password =  "12345"

def button_function():
	# new_window = customtkinter.CTkToplevel(app)
	# new_window.title("New Window")
	# new_window.geometry("350x150")
	
	if entry1.get() in username and entry2.get() == password:webbrowser.open("http://localhost:8501")
		# tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
		# customtkinter.CTkLabel(new_window,text="GeeksforGeeks is best for learning ANYTHING !!").pack()

	elif entry1.get() == username and entry2.get() != password:
		tkinter.messagebox.showwarning(title='Wrong password',message='Please check your password')
		
	elif entry1.get() != username and entry2.get() == password:
		tkinter.messagebox.showwarning(title='Wrong username',message='Please check your username')

	else:
		tkinter.messagebox.showerror(title="Login Failed",message="Invalid Username and password")

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
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

# You can easily integrate authentication system 

app.mainloop()