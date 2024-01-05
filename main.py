from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import loginWinDow, search

class MainWindow:
    def __init__(self):
        # Creating root window
        self.root = Tk()
        self.root.geometry("900x600")
        self.root.title('Weather App')
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
        self.bg=ImageTk.PhotoImage(file="banner.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        
    def entries(self):
        self.label1 = Label(self.root, text = "Select User",font=("Algerian", 26, "bold"),fg="blue", bg='white')
        self.label1.place(x=330,y=270)
        
        # Guest User Button
        self.guestUser = Button(self.root, text = "Guest User",font=("Calibri", 15, "bold"),fg="green", command = self.search)
        self.guestUser.place(x=290,y=350,height=40,width=150)
        
        # Login Button
        self.loginButton = Button(self.root, text = "Login",font=("Calibri", 15, "bold"),fg="green", command = self.openpage)
        self.loginButton.place(x=460,y=350,height=40,width=150)
        
        self.root.mainloop()
        
    def openpage(self):
        self.root.destroy()
        obj = loginWinDow.LoginWindow()
        obj.entries()
    def search(self):
        self.root.destroy()
        obj = search.searchwindow()
        obj.entries()
        
if __name__ == "__main__" :
    obj = MainWindow()
    obj.entries()