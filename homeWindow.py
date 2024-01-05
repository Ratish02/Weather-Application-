from cProfile import label
from cgitb import text
import json
from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import date, datetime
import requests
import pytz
from PIL import ImageTk
import time
import sys
import main
import loginSearch, finalwinDow, addCity


class searchwindow:
    
    API_KEY = 'd0f9dd380ee41dcb707a3674c3e02a15'
    
    def __init__(self):
          
        
        self.root = Tk()
        self.root.geometry("900x600")
        self.root.title("Search WinDow")
        self.root.resizable(width=False, height= False)
        self.root.config(bg='#1F3FB8')
        
    #Placing Window
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        self.width = int((self.fullwidth-900)/2)
        self.height = int((self.fullheight-600)/2)

        s = "900x600+" +str(self.width)+ "+" + str(self.height)

        self.root.resizable(height=False,width=False)

        self.root.geometry(s)
        
        #Bg Image
        #self.bg=ImageTk.PhotoImage(file="C:\\Users\\RATISH\\OneDrive\\Documents\\Project\\resize.png")
        #self.bg_image=Label(self.root,image=self.bg).place(x=400,y=250,relwidth=1,relheight=1)

    def entries(self, res):
        
        self.data = res
        print(self.data)
        
        self.menu = Menu(self.root)
        
        self.file = Menu(self.menu, tearoff=0)
        
        self.menu.add_cascade(label='Search', menu = self.file)
        self.file.add_command(label='Search Weather', command=self.searches)
        self.file.add_command(label='Search 5 day', command=self.open5day )
        
        self.city = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='City', menu=self.city)
        self.city.add_command(label='Add City', command=self.addCity)

        self.menu.add_cascade(label='Logout', command=self.root.destroy)
        # self.entryValue = StringVar()
        # self.entryWid = Entry(self.root, textvariable = self.entryValue, font=("Calibri", 20, "bold"),fg="#212120",bg='peachpuff2')
        # self.entryWid.place(x=210,y=100,height=40,width=400)

        # self.search = Button(self.root, text= "Search", font=("Calibri", 15, "bold"), fg="peachpuff2",bg='#212120',command=self.getweather)
        # self.search.place(x=600,y=100,height=40,width=80)
        
        # Back button
        self.back = Button(self.root, text = "Back",font=("Calibri", 15, "bold"),fg="peachpuff2",bg="black", command = self.openpage)
        # self.back.place(x=0,y=0,height=40,width=50)
        
        
        self.clock=Label(self.root,font=('calibri',30,'bold'),bg='#1F3FB8',fg='peachpuff2')
        self.clock.place(x=640,y=10,width=280)
        
        #self.date = Label(self.root,font=('calibri',30,'bold'),bg='#1F3FB8',fg='peachpuff2')
        #self.date.place(x=10,y=10,width=280)
        
        self.temp = Label(self.root, text=self.data[4].upper(), font=('calibri',20,'bold'))
        self.temp.place(x=250,y=125)
        self.t = Label(font = ('calibri',25,'bold'),fg = "PEACHPUFF2",bg='#1F3FB8')
        self.t.place(x=60,y=250,height=100,width=300)
        
        self.w = Label(font = ('calibri',22,'bold'),fg = "PEACHPUFF2",bg='#1F3FB8')
        self.w.place(x=20,y=350,height=50,width=380)

        self.h = Label(font = ('calibri',22,'bold'),fg = "PEACHPUFF2",bg='#1F3FB8')
        self.h.place(x=20,y=400,height=50,width=380)

        self.p = Label(font = ('calibri',22,'bold'),fg = "PEACHPUFF2",bg='#1F3FB8')
        self.p.place(x=20,y=450,height=50,width=380)
        
        self.d = Label(font = ('calibri',22,'bold'),fg = "PEACHPUFF2",bg='#1F3FB8')
        self.d.place(x=20,y=500,height=50,width=380)
        
        #Images
        
        self.firstimage = Label(self.root,bg='#1F3FB8')
        self.firstimage.place(x=620,y=340)

        
        #img = Image("C:\\Users\\RATISH\\OneDrive\\Documents\\Project\\info.png")       
        #img.place(x=400,y=250)
        
        self.root.config(menu = self.menu)
        self.get_time()
        self.getweather()
        self.root.mainloop()
        self.openpage()

    def searches(self):
        self.root.destroy()
        obj = loginSearch.searchwindow()
        obj.entries(self.data)
        
    def open5day(self):
        self.root.destroy()
        obj = finalwinDow.Final()
        obj.entries(self.data)

    def addCity(self):
        obj = addCity.addcityadd()
        obj.city(self.data)

        
    # time function
    def get_time(self):
        current_time = time.strftime("%I:%M:%S %p")
        self.clock.config(text=current_time)
        self.clock.after(200,self.get_time)
    
    #def get_date(self):
    #    current_date = date.

    
    def getweather(self):
        try:
            city = self.data[4]
            
            req = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=d0f9dd380ee41dcb707a3674c3e02a15' + self.API_KEY
            
            reqs = requests.get(req)
            
            data = reqs.json()
            #print(data)
            

        
            api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d0f9dd380ee41dcb707a3674c3e02a15"
            json_data = requests.get(api).json()
            #condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp']-273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']
            
            self.t.config(text=(f"Temperature:  {temp}°C"))
            #self.c.config(text=(condition,"|","Feels","Like",temp,"°C"))
            self.w.config(text=(f"Wind: {wind} m/s"))
            self.h.config(text=(f"Humidity: {humidity} %"))
            self.d.config(text=(f"Description:  {description}"))
            self.p.config(text=(f"Pressure: {pressure} hPa"))
            
            #print(json_data)
            firstdayimage = json_data['weather'][0]['icon']
            print(firstdayimage)

            photo1 = ImageTk.PhotoImage(file=f"weatherimages//{firstdayimage}.png")
            self.firstimage.config(image=photo1)
            self.firstimage.image=photo1
            
        
        except Exception as e:
            messagebox.showerror("Weather App", "invalid Entry!!")

    def openpage(self):
        self.root.destroy()
        obj = main.MainWindow()
        obj.entries()
            
            
            
if __name__ == "__main__":
    obj= searchwindow()
    obj.entries()
   