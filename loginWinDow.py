from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import search, finalwinDow
import ProjectSignupWinDow
import database,homeWindow

class LoginWindow:
    def __init__(self):
        # Creating root window
        self.root = Tk()
        self.root.geometry("900x600")
        self.root.title('LOGIN WINDOW')
        self.root.resizable(width=False, height=False)

        #Placing Window
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        self.width = int((self.fullwidth-900)/2)
        self.height = int((self.fullheight-600)/2)

        s = "900x600+" +str(self.width)+ "+" + str(self.height)

        self.root.resizable(height=False,width=False)

        self.root.geometry(s)
        # Bg Image
        # self.bg=ImageTk.PhotoImage(file="Images\\6BX.gif")
        # self.bg_image=Label(self.root,image=self.bg).place(x=-190,y=0,relwidth=1,relheight=1)

        
    def entries(self):
        #Frame
        Frame_login=Frame(self.root, bg='#1F3FB8')
        Frame_login.place(x=499,y=0,height=600,width=550)
        
        #Title
        title=Label(Frame_login,text="Weather APP",font=("Algerian",25,"bold"),fg="saddle brown", bg='pink').place(x=90,y=30)
        # desc=Label(Frame_login,text="UserName",font=("Goudy old styles",15,"bold"),fg="blue",bg="deep sky blue").place(x=90,y=100)
       
        # Username 
        self.label1 = Label(self.root, text = "Username",font=("Calibri", 26, "bold"),fg="saddle brown", bg='pink')
        self.label1.place(x=550,y=150)

        self.entryValue = StringVar()
        self.entryWid = Entry(self.root, textvariable = self.entryValue)
        self.entryWid.place(x=710,y=163,height=26,width=150)

        # Password 
        self.label2 = Label(self.root, text = "Password",font=("Calibri", 26, "bold"),fg="saddle brown", bg='pink')
        self.label2.place(x=552,y=220)

        self.passValue = StringVar()
        self.entryWid = Entry(self.root, textvariable = self.passValue, show = '*')
        self.entryWid.place(x=710,y=231,height=26,width=150)

        # Login Button
        self.loginButton = Button(self.root, text = "Login",font=("Calibri", 15, "bold"),fg="green", command = self.loginUser)
        self.loginButton.place(x=760,y=270,height=40,width=100)

        # New Account Button
        self.newAccountButton = Button(self.root, text = "New User",font=("Calibri", 15, "bold"),fg="Blue", command= self.openpage)
        self.newAccountButton.place(x=710,y=385,height=40,width=100)

        # Guest user
        self.guestUser = Button(self.root, text= "Guest User", font=("Calibri", 15, "bold"), fg="Blue", command= self.search)
        self.guestUser.place(x=590,y=385,height=40,width=100)
        
        # Forgot Password 
        #self.forgotPassword = Button(self.root, text= "Forgot Password", font=("Calibri", 15, "bold"), fg="green")
        #self.forgotPassword.place(x=600,y=450,height=40,width=200)
        
        #calling function
        self.play_gif()
        
        self.root.mainloop()
      
    
    def loginUser(self):
        if self.entryValue.get() == '':
            messagebox.showerror('Alert', 'Enter your username first.')
        elif self.passValue.get() == '':
            messagebox.showerror('Alert', 'Enter Password first.')
        else:
            self.data = (
                self.entryValue.get(),
                self.passValue.get(),
                # self.contactEntry.get()
                # self.id[0]
            )

            res = database.loginUser(self.data)
            if res:
                messagebox.showinfo('Success', 'Login successfully.')
                # self.final()
                self.root.destroy()
                obj = homeWindow.searchwindow()
                obj.entries(res)
                
            else:
                messagebox.showerror('Alert', 'Something went wrong.')

        

    #linking
    def openpage(self):
        self.root.destroy()
        obj = ProjectSignupWinDow.LoginWindow()
        obj.entries()
    def search(self):
        self.root.destroy()
        obj = search.searchwindow()
        obj.entries()
    def final(self):
        self.root.destroy()
        obj = finalwinDow.Final()
        obj.entries()
    
    #gif

    def play_gif(self):
        global img
        img = Image.open("fjt.gif")

        label7= Label(self.root)
        label7.place(x=0,y=0,width=499)

        for img in ImageSequence.Iterator(img):

            img = ImageTk.PhotoImage(img)
            label7.config(image = img)

            self.root.update()




   



if __name__ == "__main__":
    obj = LoginWindow()
    obj.entries()





