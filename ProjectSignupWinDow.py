from ctypes import resize
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import loginWinDow, finalwinDow
import database
import homeWindow, loginWinDow
class LoginWindow:
    def __init__(self):
        # Creating root window
        self.root = Tk()
        self.root.geometry("900x600")
        self.root.title('Sign Up WINDOW')
        self.root.resizable(width=False, height=False)
        
         #Placing Window
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        self.width = int((self.fullwidth-900)/2)
        self.height = int((self.fullheight-600)/2)

        s = "900x600+" +str(self.width)+ "+" + str(self.height)

        self.root.resizable(height=False,width=False)

        self.root.geometry(s)
        #Bg Image
        #self.bg=ImageTk.PhotoImage(file="Images\\b.gif")
        #self.bg_image=Label(self.root,image=self.bg).place(x=-2,y=-2)


    def entries(self):
        #Frame
        frame =Frame(self.root, bg='#1F3FB8')
        frame.place(x=499,y=0,height=600,width=550)
        
        
        #Title
        title=Label(frame, text="Enter Details", font=("Algerian",33,"bold"),fg="green", bg="Pink").place(x=40,y=30)
        
       
        # Username 
        self.label1 = Label(self.root, text = "Username",font=("Calibri", 16, "bold"),fg="brown", bg="Pink")
        self.label1.place(x=550,y=150)

        self.username = StringVar()
        self.entryWid = Entry(self.root, textvariable = self.username)
        self.entryWid.place(x=710,y=160,height=20,width=150)

        # E-mail
        self.label2 = Label(self.root, text = "Email",font=("Calibri", 16, "bold"),fg="brown", bg="Pink")
        self.label2.place(x=550,y=200)

        self.email = StringVar()
        self.entryWid = Entry(self.root, textvariable = self.email)
        self.entryWid.place(x=710,y=210,height=20,width=150)

        # Phone Number
        self.label3 = Label(self.root, text = "Phone Number",font=("Calibri", 16, "bold"),fg="brown", bg="Pink")
        self.label3.place(x=550,y=250)

        self.phone = StringVar()
        self.entryWid = Entry(self.root, textvariable = self.phone)
        self.entryWid.place(x=710,y=260,height=20,width=150)

        # Password 
        self.label4 = Label(self.root, text = "Password",font=("Calibri", 16, "bold"),fg="brown", bg="Pink")
        self.label4.place(x=550,y=300)

        self.passValue = StringVar()
        self.entryWid = Entry(self.root, textvariable = self.passValue, show = '*')
        self.entryWid.place(x=710,y=310,height=20,width=150)

        # Confirm Password
        self.label5 = Label(self.root, text = "Confirm Password",font=("Calibri", 15, "bold"),fg="brown", bg="Pink")
        self.label5.place(x=550,y=350)

        self.CpassValue = StringVar()
        self.entryWid = Entry(self.root, textvariable = self.CpassValue,show = '*' )
        self.entryWid.place(x=710,y=353,height=20,width=150)
        
        # Location
        self.label6 = Label(self.root, text = "Location" ,font=("Calibri", 15, "bold"),fg="brown", bg="Pink")
        self.label6.place(x=550,y=400)

        self.loc = StringVar()
        self.entryWid = Entry(self.root, textvariable = self.loc)
        self.entryWid.place(x=710,y=402,height=20,width=150)
        
        # create account Button
        self.createAccount = Button(self.root, text = "Create Account",font=("Calibri", 15, "bold"),fg="Green",bg="Pink", command = self.createAccount)
        self.createAccount.place(x=705,y=475,height=40,width=180)
        
        # Back button
        self.back = Button(self.root, text = "Back",font=("Calibri", 15, "bold"),fg="Green",bg="Pink", command = self.openpage)
        self.back.place(x=509,y=475,height=40,width=180)

        self.play_gif()             
        self.root.mainloop()

    def createAccount(self):
        # if self.username.get() == '':
        #     messagebox.showerror('Alert','Enter your Username first')
        # elif self.email.get() == '':
        #     messagebox.showerror('Alert','Enter your E-mail first')
        # elif self.phone.get() == '':
        #     messagebox.showerror('Alert','Enter your Phone Number first')
        # elif self.passValue.get() == '':
        #     messagebox.showerror('Alert','Enter your password first')
        # elif self.CpassValue.get() == '':
        #     messagebox.showerror('Alert','Confirm your password first')
        # elif self.passValue.get() != self.CpassValue.get():
        #     messagebox.showerror('Alert','Password Mismatch')
        # else:
        #     messagebox.showinfo('Success','Account Created Successfully')
        #     self.final()
    
    # def login(self):
        if self.username.get() == '':
            messagebox.showerror('Alert', 'Enter your username first.')
        elif self.email.get() == '':
            messagebox.showerror('Alert', 'Enter roll number first.')
        elif self.phone.get() == '':
            messagebox.showerror('Alert', 'Enter roll number first.')
        elif self.passValue.get() == '':
            messagebox.showerror('Alert', 'Enter roll number first.')
        elif self.CpassValue.get() == '':
            messagebox.showerror('Alert', 'Enter roll number first.')
        elif self.loc.get() == '':
            messagebox.showerror('Alert', 'Enter roll number first.')
        else:
            self.data = (
                self.username.get(),
                self.email.get(),
                self.passValue.get(),
                self.loc.get(),
                # self.contactEntry.get()
            )

            res = database.registerUser(self.data)
            if res:
                messagebox.showinfo('Success', 'User added successfully.')
                self.root.destroy()
                obj=loginWinDow.LoginWindow()
                obj.entries()
                
            else:
                messagebox.showerror('Alert', 'Something went wrong.')


    def play_gif(self):
        global img
        img = Image.open("fjt.gif")

        label7= Label(self.root)
        label7.place(x=0,y=0, width=499)

        for img in ImageSequence.Iterator(img):

            img = ImageTk.PhotoImage(img)
            label7.config(image = img)

            self.root.update()
            
    def openpage(self):
        self.root.destroy()
        obj = loginWinDow.LoginWindow()
        obj.entries()
    def final(self):
        self.root.destroy()
        obj = finalwinDow.Final()
        obj.entries()

if __name__ == "__main__":
    obj = LoginWindow()
    obj.entries()




