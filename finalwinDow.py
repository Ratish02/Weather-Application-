from cProfile import label
from cgitb import text
import json
import time 
import sys
from tkinter import *
from tkinter.font import BOLD
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import requests
import pytz
from PIL import ImageTk
import homeWindow


class Final:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("900x600")
        self.root.title("window")
        self.root.resizable(width=False,height=False)
        self.root.config(bg='#1F3FB8')

    #Placing Window
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        self.width = int((self.fullwidth-900)/2)
        self.height = int((self.fullheight-600)/2)

        s = "900x600+" +str(self.width)+ "+" + str(self.height)

        self.root.resizable(height=False,width=False)

        self.root.geometry(s)

        # Details
        Frame_details=Frame(self.root,bg='#1F3FB8')
        Frame_details.place(x=20,y=200,height=180,width=300)

    def entries(self, data):

        self.data = data
        
        #Headings

        #self.temp = Label(self.root, text='Temp', font=('calibri',15,'bold'),fg= 'white',bg='black')
        #self.temp.place(x=50,y=220)
        
        #self.wind = Label(self.root, text='Wind', font=('calibri',15,'bold'),fg= 'white',bg='black')
        #self.wind.place(x=50,y=320)

        #self.condition = Label(self.root, text='Condition', font=('arial',11,'bold'),fg= 'white',bg='#203243')
        #self.condition.place(x=50,y=220)

        #self.humidity = Label(self.root, text='Humidity', font=('calibri',15,'bold'),fg= 'white',bg='black')
        #self.humidity.place(x=50,y=245)

        #self.description = Label(self.root, text='Description', font=('calibri',15,'bold'),fg= 'white',bg='black')
        #self.description.place(x=50,y=270)
        
        #self.pressure = Label(self.root, text='Pressure', font=('calibri',15,'bold'),fg= 'white',bg='black')
        #self.pressure.place(x=50,y=295)

        #Entry 

        self.entryValue = StringVar()
        self.entryWid = Entry(self.root, textvariable = self.entryValue, font=("Calibri", 20, "bold"),fg="black",bg='PeachPuff2')
        self.entryWid.place(x=20,y=120,height=36,width=250)

        self.search = Button(self.root, text= "Search", font=("Calibri", 15, "bold"), fg="peachpuff2",bg='black',command=self.getweather)
        self.search.place(x=270,y=120,height=38,width=100)


        #Bottom details
        frame = Frame(self.root,width=900,height=200,bg="black")
        frame.pack(side=BOTTOM)

        self.back = Button(self.root, text = "Back",font=("Calibri", 15, "bold"),fg="peachpuff2",bg="black", command = self.openpage)
        self.back.place(x=0,y=0,height=40,width=50)

        #clock
        
        self.clock = Label(self.root,font=("Helvetics",30,'bold'),fg = 'peachpuff2',bg= '#1F3FB8')
        self.clock.place(x=600,y=20)

        #timezone

        self.timezone = Label(self.root,font=("Helvetics",20,'bold'),fg = 'peachpuff2',bg= '#1F3FB8')
        self.timezone.place(x=600,y=100)

        self.long_lat=Label(self.root,font=("Helvetics",20,'bold'),fg = 'peachpuff2',bg= '#1F3FB8')
        self.long_lat.place(x=600,y=180)

        #details
        self.t = Label(font = ('calibri',15,'bold'),fg = "PeachPuff2",bg='#1F3FB8')
        self.t.place(x=50,y=220)

        #self.c = Label(font = ('arial',8,'bold'),fg = "PeachPuff2",bg='#203243')
        #self.c.place(x=150,y=220)

        self.w = Label(font = ('calibri',15,'bold'),fg = "PeachPuff2",bg='#1F3FB8')
        self.w.place(x=50,y=320)

        self.h = Label(font = ('calibri',15,'bold'),fg = "PeachPuff2",bg='#1F3FB8')
        self.h.place(x=50,y=245)

        self.d = Label(font = ('calibri',15,'bold'),fg = "PeachPuff2",bg='#1F3FB8')
        self.d.place(x=50,y=270)

        self.p = Label(font = ('calibri',15,'bold'),fg = "PeachPuff2",bg='#1F3FB8')
        self.p.place(x=50,y=295)

        #first frame
        firstframe = Frame(self.root,width=220,height=160,bg='#1F3FB8')
        firstframe.place(x=10,y=420)

        day1 = Label(firstframe,font='arial 20 bold',bg = '#1F3FB8',fg='white')
        day1.place(x=30,y=5)

        self.firstimage = Label(firstframe,bg='#1F3FB8')
        self.firstimage.place(x=120,y=40)

        self.day1temp = Label(firstframe,font='arial 15 bold',bg = '#1F3FB8',fg='white')
        self.day1temp.place(x=20,y=68)
        #second
        secondframe = Frame(self.root,width=150,height=160,bg='#1F3FB8')
        secondframe.place(x=240,y=420)

        day2= Label(secondframe,font='arial 15 bold',bg = '#1F3FB8',fg='white')
        day2.place(x=35,y=5)

        self.secondimage = Label(secondframe,bg='#1F3FB8')
        self.secondimage.place(x=10,y=30)

        self.day2temp = Label(secondframe,font='arial 10 bold',bg = '#1F3FB8',fg='white')
        self.day2temp.place(x=25,y=110)

        #third
        thirdframe = Frame(self.root,width=150,height=160,bg='#1F3FB8')
        thirdframe.place(x=400,y=420)

        day3 = Label(thirdframe,font='arial 15 bold',bg = '#1F3FB8',fg='white')
        day3.place(x=25,y=5)

        self.thirdimage = Label(thirdframe,bg='#1F3FB8')
        self.thirdimage.place(x=10,y=30)

        self.day3temp = Label(thirdframe,font='arial 10 bold',bg = '#1F3FB8',fg='white')
        self.day3temp.place(x=25,y=110)

        #fourth
        fourthframe = Frame(self.root,width=150,height=160,bg='#1F3FB8')
        fourthframe.place(x=560,y=420)

        day4 = Label(fourthframe,font='arial 15 bold',bg = '#1F3FB8',fg='white')
        day4.place(x=25,y=5)

        self.fourthimage = Label(fourthframe,bg='#1F3FB8')
        self.fourthimage.place(x=10,y=30)

        self.day4temp = Label(fourthframe,font='arial 10 bold',bg = '#1F3FB8',fg='white')
        self.day4temp.place(x=25,y=110)

        #fifth
        fifthframe = Frame(self.root,width=150,height=160,bg='#1F3FB8')
        fifthframe.place(x=720,y=420)

        day5 = Label(fifthframe,font='arial 15 bold',bg = '#1F3FB8',fg='white')
        day5.place(x=25,y=5)

        self.fifthimage = Label(fifthframe,bg='#1F3FB8')
        self.fifthimage.place(x=10,y=30)

        self.day5temp = Label(fifthframe,font='arial 10 bold',bg = '#1F3FB8',fg='white')
        self.day5temp.place(x=25,y=110)

        

        #days

        first= datetime.now()
        day1.config(text=first.strftime("%A"))

        second = first + timedelta(days=1)
        day2.config(text=second.strftime("%A"))

        third = first + timedelta(days=2)
        day3.config(text=third.strftime("%A"))

        fourth = first + timedelta(days=3)
        day4.config(text=fourth.strftime("%A"))

        fifth = first + timedelta(days=4)
        day5.config(text=fifth.strftime("%A"))

        

       




    #calling functions
        self.get_time()
        self.root.mainloop()

        
        
    #time function
    def get_time(self):
        current_time = time.strftime("%I:%M:%S %p")
        self.clock.config(text=current_time)
        self.clock.after(200,self.get_time)

    #Weather function

    def getweather(self):
        try:
            city = self.entryValue.get()
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

            self.timezone.config(text= result)
            self.long_lat.config(text =f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")
        
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            #current_time = local_time.strftime("%I:%M:%S %p")

            #self.clock.config(text=current_time)
            #self.name.config(text= "current Weather ")
        
            
            api = "https://api.openweathermap.org/data/2.5/forecast?q="+city+"&appid=d0f9dd380ee41dcb707a3674c3e02a15"
            json_data = requests.get(api).json()
            print(json_data)

            #condition = json_data['weather'][0]['main']
            description = json_data['list'][0]['weather'][0]['description']
            temp = int(json_data['list'][0]['main']['temp']-273.15)
            pressure = json_data['list'][0]['main']['pressure']
            humidity = json_data['list'][0]['main']['humidity']
            wind = json_data['list'][0]['wind']["speed"]
            


            self.t.config(text=(f"Temperature:  {temp} °C"))
            #self.c.config(text=(condition,"|","Feels","Like",temp,"°C"))
            self.w.config(text=(f"Wind: {wind} m/s"))
            self.h.config(text=(f"Humidity: {humidity} %"))
            self.d.config(text=(f"Description:  {description}"))
            self.p.config(text=(f"Pressure: {pressure} hPa"))

            #Image icon

            #first

            firstdayimage = json_data['list'][0]['weather'][0]['icon']

            photo1 = ImageTk.PhotoImage(file=f"weatherimages2//{firstdayimage}.png")
            self.firstimage.config(image=photo1)
            self.firstimage.image=photo1
            

            #second

            seconddayimage = json_data['list'][8]['weather'][0]['icon']
            
            photo2 = ImageTk.PhotoImage(file=f"weatherimages2//{seconddayimage}.png")
            self.secondimage.config(image=photo2)
            self.secondimage.image=photo2

            #third

            thirddayimage = json_data['list'][16]['weather'][0]['icon']
            
            photo3 = ImageTk.PhotoImage(file=f"weatherimages2//{thirddayimage}.png")
            self.thirdimage.config(image=photo3)
            self.thirdimage.image=photo3

            #fourth
            fourthdayimage = json_data['list'][24]['weather'][0]['icon']
            
            photo4 = ImageTk.PhotoImage(file=f"weatherimages2//{fourthdayimage}.png")
            self.fourthimage.config(image=photo4)
            self.fourthimage.image=photo4

            #fifth

            fifthdayimage = json_data['list'][32]['weather'][0]['icon']
              
            photo5 = ImageTk.PhotoImage(file=f"weatherimages2//{fifthdayimage}.png")
            self.fifthimage.config(image=photo5)
            self.fifthimage.image=photo5

            #Details According to Days 

            #first
            tempday1 = int(json_data['list'][2]['main']['temp']-273.15)
            tempnight1 = int(json_data['list'][7]['main']['temp']-273.15)
            self.day1temp.config(text = f"Day:{tempday1}°C \n Night:{tempnight1}°C")
            #second
            tempday2 = int(json_data['list'][10]['main']['temp']-273.15)
            tempnight2 = int(json_data['list'][15]['main']['temp']-273.15)
            self.day2temp.config(text = f"Day:{tempday2}°C \n Night:{tempnight2}°C")
            #third
            tempday3 = int(json_data['list'][18]['main']['temp']-273.15)
            tempnight3 = int(json_data['list'][23]['main']['temp']-273.15)
            self.day3temp.config(text = f"Day:{tempday3}°C \n Night:{tempnight3}°C")
            #fourth
            tempday4 = int(json_data['list'][26]['main']['temp']-273.15)
            tempnight4 = int(json_data['list'][31]['main']['temp']-273.15)
            self.day4temp.config(text = f"Day:{tempday4}°C \n Night:{tempnight4}°C")
            #fifth
            tempday5 = int(json_data['list'][33]['main']['temp']-273.15)
            tempnight5 = int(json_data['list'][39]['main']['temp']-273.15)
            self.day5temp.config(text = f"Day:{tempday5}°C \n Night:{tempnight5}°C")
            


        except Exception as e:
            messagebox.showerror("Weather App", "invalid Entry!!")



    def openpage(self):
        self.root.destroy()
        obj = homeWindow.searchwindow()
        obj.entries(self.data)


        


if __name__ == "__main__":
    obj = Final()
    obj.entries()