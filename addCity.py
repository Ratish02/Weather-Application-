from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import Image , ImageTk
import requests
from setuptools import Command
import database, cities


class addcityadd:
    API_KEY = '137ed62b65eeb01da3d53559f4f18e4c'
    def __init__(self):
        self.root = Toplevel()
        self.root.title('weather ')
        # print(self.root.winfo_screenwidth())
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1500)/2)
        self.height=int((self.fullheight-700)/2)

        s = "1400x700+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

        
    
    def city(self, data):

        self.data = data

        if self.data[5] != '':
            self.root.destroy()
            obj = cities.addcityadd()
            obj.frames(self.data)

        # self.image = ImageTk.PhotoImage(Image.open("image/10.jpg") . resize((1500 , 900)) )
        # self.imageLabel = Label(self.root, image=self.image)
        # self.imageLabel.place(x =0 , y= 0, )


        #button 1
        self.addcitybutton = Button(self.root, text=" Add city  ", cursor='hand2' ,  font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF',command=self.addcity1)
        self.addcitybutton.place(x = 200, y =80 , width=100 , height=30)

        
        
        #button2
        self.addcitybutton1 = Button(self.root, text=" Add city  ", cursor='hand2' , command=self.addcity2 , font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF')
        self.addcitybutton1.place(x = 650, y =80 , width=100 , height=30)

        #button 3
        self.addcitybutton2 = Button(self.root, text=" Add city  ", cursor='hand2' , command=self.addcity3 , font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF')
        self.addcitybutton2.place(x = 1050, y =80 , width=100 , height=30)

        
        

        self.root.mainloop()
    def addcity1(self):
        self.addcitybutton.destroy()
        

        #entry (text field)
        self.textfield1=Entry (self.root , justify='center' , width=15  , font=('Bell MT' , 25 , 'bold') , bg='#203243'  , border=0 , fg='white' )
        self.textfield1.place(x= 180 ,y=120, width='150' , height='32')
       

        self.addcity = Button(self.root, text=" Add city  ", cursor='hand2' , font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF', command = self.cityWeather1)
        self.addcity.place(x =200, y =170, width=100 , height=30)


        self.saveBtn = Button(self.root, text="Save ", cursor='hand2' , font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF', command = self.saveCities)
        self.saveBtn.place(x =650, y =600, width=100 , height=30)



        

    def addcity2(self):
        self.addcitybutton1.destroy()

        

        #entry (text field)
        self.textfield=Entry (self.root , justify='center' , width=15  , font=('Bell MT' , 25 , 'bold') , bg='#203243'  , border=0 , fg='white' )
        self.textfield.place(x= 630 ,y=120, width='150' , height='32')
        self.textfield.focus()

        self.addcity = Button(self.root, text=" Add city  ", cursor='hand2' , command=self.cityWeather2 , font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF')
        self.addcity.place(x =650, y =170, width=100 , height=30)

        self.saveBtn = Button(self.root, text="Save ", cursor='hand2' , font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF', command = self.saveCities)
        self.saveBtn.place(x =650, y =600, width=100 , height=30)

        
    def addcity3(self):
        self.addcitybutton2.destroy()


        

        #entry (text field)
        self.textfield2=Entry (self.root , justify='center' , width=15  , font=('Bell MT' , 25 , 'bold') , bg='#203243'  , border=0 , fg='white' )
        self.textfield2.place(x= 1030 ,y=120, width='150' , height='32')
        self.textfield2.focus()

        self.addcity = Button(self.root, text=" Add city  ", cursor='hand2' , command=self.cityweather3 , font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF')
        self.addcity.place(x =1050, y =170, width=100 , height=30)

        self.saveBtn = Button(self.root, text="Save ", cursor='hand2' , font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF', command = self.saveCities)
        self.saveBtn.place(x =650, y =600, width=100 , height=30)
        
    def cityWeather1(self):
        if self.textfield1.get() == '':
            messagebox.showerror('Alert', 'Enter city name first')
        else:

            cityName = self.textfield1.get()
            data, self.images1 = self.cityWeathers(cityName)
            
         # frame 1 

            self.frame1=Frame (self.root, bg='#91CEFF' )
            self.frame1.place (x=70 , y=60 , width='300', height='500')

            self.weathImage = ImageTk.PhotoImage(Image.open(self.images1) . resize((100 ,100)))
            self.imageLabel1 = Label(self.frame1, image=self.weathImage , bg="#91CEFF")
            self.imageLabel1.place(x = 0, y = 50)


            #location

            self.lablel1=Label(self.frame1, text=cityName.title(), font=('Bell MT',15) , bg= '#91CEFF' ,fg="#040405" )
            self.lablel1.place(x= 125, y=30 )
            
            #weather 
            self.userLabel = Label(self.frame1, text='°C'.title(), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
            self.userLabel.place(x =205 , y = 75 )
            
            self.userLabel = Label(self.frame1, text=str(int(data['main']['temp']) - 273), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
            self.userLabel.place(x =170 , y = 75 )
        
            #feels like
            self.userLabel = Label(self.frame1, text='Feels Like -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =50 , y = 240 , width=150 ,height=40)


            self.userLabel = Label(self.frame1, text=str(int(data['main']['feels_like']) - 273) + '°C', bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 240 , width=150 ,height=40)


            #visibility        
            self.userLabel = Label(self.frame1, text='Visibility -'.title(), bg ='#91CEFF',fg='white', font=('    Calbri   ',15,) )
            self.userLabel.place(x =50 , y = 280 , width=150 ,height=40)

            self.userLabel = Label(self.frame1, text=str(int(data['visibility']) // 1000 ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 280 , width=150 ,height=40)


            #humidity
            self.userLabel = Label(self.frame1, text='Humidity -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =50 , y = 320 , width=150 ,height=40)


            self.userLabel = Label(self.frame1, text=str(int(data['main']['humidity']) ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 322 , width=150 ,height=40)


            #wind
            self.userLabel = Label(self.frame1, text='Wind -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15,) )
            self.userLabel.place(x =50 , y = 360 , width=150 ,height=40)


            self.userLabel = Label(self.frame1,text=str(int(data['wind']['speed'])), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 360 , width=150 ,height=40)


            # self.addcity10 = Button(self.root, text=" Add city  ", cursor='hand2' , command=self.cityweather3 , font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF')
            # self.addcity10.place(x =650, y =600, width=100 , height=30)



    def cityWeather2(self):
        if self.textfield.get() == '':
            messagebox.showerror('Alert', 'Enter city name first')
        else:

            cityName = self.textfield.get()
            data, self.images2  = self.cityWeathers1(cityName)

            
            
         # frame 1 

            self.frame2=Frame (self.root, bg='#91CEFF' )
            self.frame2.place (x=550, y=60 , width='300', height='500')

            self.weathImage1 = ImageTk.PhotoImage(Image.open(self.images2) . resize((100 ,100)))
            self.imageLabel2 = Label(self.frame2, image=self.weathImage1 , bg="#91CEFF")
            self.imageLabel2.place(x = 0, y = 50)


            #location

            self.lablel1=Label(self.frame2, text=cityName.title(), font=('Bell MT',15) , bg= '#91CEFF' ,fg="#040405" )
            self.lablel1.place(x= 125, y=30 )
            
            #weather 
            self.userLabel = Label(self.frame2, text='°C'.title(), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
            self.userLabel.place(x =205 , y = 75 )
            
            self.userLabel = Label(self.frame2, text=str(int(data['main']['temp']) - 273), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
            self.userLabel.place(x =170 , y = 75 )
        
            #feels like
            self.userLabel = Label(self.frame2, text='Feels Like -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =50 , y = 240 , width=150 ,height=40)


            self.userLabel = Label(self.frame2, text=str(int(data['main']['feels_like']) - 273) + '°C', bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 240 , width=150 ,height=40)


            #visibility        
            self.userLabel = Label(self.frame2, text='Visibility -'.title(), bg ='#91CEFF',fg='white', font=('    Calbri   ',15,) )
            self.userLabel.place(x =50 , y = 280 , width=150 ,height=40)

            self.userLabel = Label(self.frame2, text=str(int(data['visibility']) // 1000 ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 280 , width=150 ,height=40)


            #humidity
            self.userLabel = Label(self.frame2, text='Humidity -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =50 , y = 320 , width=150 ,height=40)


            self.userLabel = Label(self.frame2, text=str(int(data['main']['humidity']) ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 322 , width=150 ,height=40)


            #wind
            self.userLabel = Label(self.frame2, text='Wind -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15,) )
            self.userLabel.place(x =50 , y = 360 , width=150 ,height=40)


            self.userLabel = Label(self.frame2,text=str(int(data['wind']['speed'])), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 360 , width=150 ,height=40)


            # self.addcity11 = Button(self.root, text=" Add city  ", cursor='hand2' , command=self.cityweather3 , font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF')
            # self.addcity11.place(x =650, y =600, width=100 , height=30)



    def cityweather3(self):
        if self.textfield2.get() == '':
            messagebox.showerror('Alert', 'Enter city name first')
        else:

            cityName = self.textfield2.get()
            data, self.images3  = self.cityWeathers2(cityName)
            
         # frame 1 

            self.frame3=Frame (self.root, bg='#91CEFF' )
            self.frame3.place (x=1000 , y=60 , width='300', height='500')

            self.weathImage2 = ImageTk.PhotoImage(Image.open(self.images3) . resize((100 ,100)))
            self.imageLabel3 = Label(self.frame3, image=self.weathImage2 , bg="#91CEFF")
            self.imageLabel3.place(x = 0, y = 50)


            #location

            self.lablel1=Label(self.frame3, text=cityName.title(), font=('Bell MT',15) , bg= '#91CEFF' ,fg="#040405" )
            self.lablel1.place(x= 125, y=30 )
            
            #weather 
            self.userLabel = Label(self.frame3, text='°C'.title(), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
            self.userLabel.place(x =205 , y = 75 )
            
            self.userLabel = Label(self.frame3, text=str(int(data['main']['temp']) - 273), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
            self.userLabel.place(x =170 , y = 75 )
        
            #feels like
            self.userLabel = Label(self.frame3, text='Feels Like -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =50 , y = 240 , width=150 ,height=40)


            self.userLabel = Label(self.frame3, text=str(int(data['main']['feels_like']) - 273) + '°C', bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 240 , width=150 ,height=40)


            #visibility        
            self.userLabel = Label(self.frame3, text='Visibility -'.title(), bg ='#91CEFF',fg='white', font=('    Calbri   ',15,) )
            self.userLabel.place(x =50 , y = 280 , width=150 ,height=40)

            self.userLabel = Label(self.frame3, text=str(int(data['visibility']) // 1000 ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 280 , width=150 ,height=40)


            #humidity
            self.userLabel = Label(self.frame3, text='Humidity -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =50 , y = 320 , width=150 ,height=40)


            self.userLabel = Label(self.frame3, text=str(int(data['main']['humidity']) ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 322 , width=150 ,height=40)


            #wind
            self.userLabel = Label(self.frame3, text='Wind -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15,) )
            self.userLabel.place(x =50 , y = 360 , width=150 ,height=40)


            self.userLabel = Label(self.frame3,text=str(int(data['wind']['speed'])), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
            self.userLabel.place(x =180 , y = 360 , width=150 ,height=40)


            # self.addcity12 = Button(self.root, text=" Add city  ", cursor='hand2' , command=self.cityweather3 , font=('Calbri', 15 , BOLD) , border=0 , bg='#91CEFF')
            # self.addcity12.place(x =650, y =600, width=100 , height=30)


    def cityWeathers(self, cityName):
        req = 'https://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&appid=' + self.API_KEY

        res = requests.get(req)
        data = res.json()
        print (data)

        if data['weather'][0]['icon'] == '01d':
            self.images1 = 'weatherimages/01d.png'

        elif data['weather'][0]['icon'] == '01n':
            self.images1 = 'weatherimages/01n.png'


        elif data['weather'][0]['icon'] == '02d':
            self.images1 = 'weatherimages/02d.png'  


        elif data['weather'][0]['icon'] == '02n':
            self.images1 = 'weatherimages/02n.png'


        elif data['weather'][0]['icon'] == '03d':
            self.images1 = 'weatherimages/03d.png'



        elif data['weather'][0]['icon'] == '03n':
            self.images1 = 'weatherimages/03n.png'


        elif data['weather'][0]['icon'] == '04d':
            self.images1 = 'weatherimages/04d.png'


        elif data['weather'][0]['icon'] == '04n':
            self.images1 = 'weatherimages/04n.png'


        elif data['weather'][0]['icon'] == '09d':
            self.images1 = 'weatherimages/09d.png'


        elif data['weather'][0]['icon'] == '09n':
            self.images1 = 'weatherimages/09n.png'


        elif data['weather'][0]['icon'] == '10d':
            self.images1 = 'weatherimages/10d.png'


        elif data['weather'][0]['icon'] == '10n':
            self.images1 = 'weatherimages/10n.png'


        elif data['weather'][0]['icon'] == '11d':
            self.images1 = 'weatherimages/11d.png'


        elif data['weather'][0]['icon'] == '11n':
            self.images1 = 'weatherimages/11n.png'


        elif data['weather'][0]['icon'] == '13d':
            self.images1 = 'weatherimages/13d.png'


        elif data['weather'][0]['icon'] == '13n':
            self.images1 = 'weatherimages/13n.png'


        elif data['weather'][0]['icon'] == '50d':
            self.images1 = 'weatherimages/50d.png'



        elif data['weather'][0]['icon'] == '50n':
            self.images1 = 'weatherimages/50n.png'


        return data, self.images1





    def cityWeathers1(self, cityName):
        req = 'https://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&appid=' + self.API_KEY

        res = requests.get(req)
        data = res.json()
        print (data)

        if data['weather'][0]['icon'] == '01d':
            self.images2 = 'weatherimages/01d.png'

        elif data['weather'][0]['icon'] == '01n':
            self.images2 = 'weatherimages/01n.png'


        elif data['weather'][0]['icon'] == '02d':
            self.images2 = 'weatherimages/02d.png'  


        elif data['weather'][0]['icon'] == '02n':
            self.images2 = 'weatherimages/02n.png'


        elif data['weather'][0]['icon'] == '03d':
            self.images2 = 'weatherimages/03d.png'



        elif data['weather'][0]['icon'] == '03n':
            self.images2 = 'weatherimages/03n.png'


        elif data['weather'][0]['icon'] == '04d':
            self.images2 = 'weatherimages/04d.png'


        elif data['weather'][0]['icon'] == '04n':
            self.images2 = 'weatherimages/04n.png'


        elif data['weather'][0]['icon'] == '09d':
            self.images2 = 'weatherimages/09d.png'


        elif data['weather'][0]['icon'] == '09n':
            self.images2 = 'weatherimages/09n.png'


        elif data['weather'][0]['icon'] == '10d':
            self.images2 = 'weatherimages/10d.png'


        elif data['weather'][0]['icon'] == '10n':
            self.images2 = 'weatherimages/10n.png'


        elif data['weather'][0]['icon'] == '11d':
            self.images2 = 'weatherimages/11d.png'


        elif data['weather'][0]['icon'] == '11n':
            self.images2 = 'weatherimages/11n.png'


        elif data['weather'][0]['icon'] == '13d':
            self.images2 = 'weatherimages/13d.png'


        elif data['weather'][0]['icon'] == '13n':
            self.images2 = 'weatherimages/13n.png'


        elif data['weather'][0]['icon'] == '50d':
            self.images2 = 'weatherimages/50d.png'



        elif data['weather'][0]['icon'] == '50n':
            self.images2 = 'weatherimages/50n.png'


        return data, self.images2



    def cityWeathers2(self, cityName):
        req = 'https://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&appid=' + self.API_KEY

        res = requests.get(req)
        data = res.json()
        print (data)

        if data['weather'][0]['icon'] == '01d':
            self.images3 = 'weatherimages/01d.png'

        elif data['weather'][0]['icon'] == '01n':
            self.images3 = 'weatherimages/01n.png'


        elif data['weather'][0]['icon'] == '02d':
            self.images3 = 'weatherimages/02d.png'  


        elif data['weather'][0]['icon'] == '02n':
            self.images3 = 'weatherimages/02n.png'


        elif data['weather'][0]['icon'] == '03d':
            self.images3 = 'weatherimages/03d.png'



        elif data['weather'][0]['icon'] == '03n':
            self.images3 = 'weatherimages/03n.png'


        elif data['weather'][0]['icon'] == '04d':
            self.images3 = 'weatherimages/04d.png'


        elif data['weather'][0]['icon'] == '04n':
            self.images3 = 'weatherimages/04n.png'


        elif data['weather'][0]['icon'] == '09d':
            self.images3 = 'weatherimages/09d.png'


        elif data['weather'][0]['icon'] == '09n':
            self.images3 = 'weatherimages/09n.png'


        elif data['weather'][0]['icon'] == '10d':
            self.images3 = 'weatherimages/10d.png'


        elif data['weather'][0]['icon'] == '10n':
            self.images3 = 'weatherimages/10n.png'


        elif data['weather'][0]['icon'] == '11d':
            self.images3 = 'weatherimages/11d.png'


        elif data['weather'][0]['icon'] == '11n':
            self.images3 = 'weatherimages/11n.png'


        elif data['weather'][0]['icon'] == '13d':
            self.images3 = 'weatherimages/13d.png'


        elif data['weather'][0]['icon'] == '13n':
            self.images3 = 'weatherimages/13n.png'


        elif data['weather'][0]['icon'] == '50d':
            self.images3 = 'weatherimages/50d.png'



        elif data['weather'][0]['icon'] == '50n':
            self.images3 = 'weatherimages/50n.png'


        return data, self.images3

    

    def saveCities(self):
        if self.textfield1.get() == '':
            messagebox.showerror()
        elif self.textfield.get() == '':
            messagebox.showerror()
        elif self.textfield2.get() == '':
            messagebox.showerror()
        else:
            data = (
                self.textfield1.get(),
                self.textfield.get(),
                self.textfield2.get(),
                self.data[0]
            )

            res = database.addCity(data)
            if res:
                self.root.destroy()
                messagebox.showinfo('success', 'Cities added successfully.')
            else:
                messagebox.showerror('Alert', 'something went wrong.')

if __name__== '__main__' :
    obj= addcityadd()
    obj.city()
   
