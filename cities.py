from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import Image , ImageTk
import requests


class addcityadd:
    API_KEY = '137ed62b65eeb01da3d53559f4f18e4c'
    def __init__(self):
        self.root = Toplevel()
        self.root.title('weather ')
        # print(self.root.winfo_screenwidth())
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1400)/2)
        self.height=int((self.fullheight-600)/2)

        s = "1400x600+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def frames(self, data):

        self.data = data

        city1 = self.data[5]
        city2 = self.data[6]
        city3 = self.data[7]


        self.data1, self.image1 = self.cityWeathers2(city1)
        self.frame1=Frame (self.root, bg='#91CEFF' )
        self.frame1.place (x=70 , y=60 , width='300', height='500')

        self.weathImage = ImageTk.PhotoImage(Image.open(self.image1) . resize((100 ,100)))
        self.imageLabel1 = Label(self.frame1, image=self.weathImage , bg="#91CEFF")
        self.imageLabel1.place(x = 0, y = 50)


            #location

        self.lablel1=Label(self.frame1, text=city1.title(), font=('Bell MT',15) , bg= '#91CEFF' ,fg="#040405" )
        self.lablel1.place(x= 125, y=30 )
            
            #weather 
        self.userLabel = Label(self.frame1, text='°C'.title(), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
        self.userLabel.place(x =205 , y = 75 )
            
        self.userLabel = Label(self.frame1, text=str(int(self.data1['main']['temp']) - 273), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
        self.userLabel.place(x =170 , y = 75 )
        
            #feels like
        self.userLabel = Label(self.frame1, text='Feels Like -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =50 , y = 240 , width=150 ,height=40)


        self.userLabel = Label(self.frame1, text=str(int(self.data1['main']['feels_like']) - 273) + '°C', bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 240 , width=150 ,height=40)


            #visibility        
        self.userLabel = Label(self.frame1, text='Visibility -'.title(), bg ='#91CEFF',fg='white', font=('    Calbri   ',15,) )
        self.userLabel.place(x =50 , y = 280 , width=150 ,height=40)

        self.userLabel = Label(self.frame1, text=str(int(self.data1['visibility']) // 1000 ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 280 , width=150 ,height=40)


            #humidity
        self.userLabel = Label(self.frame1, text='Humidity -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =50 , y = 320 , width=150 ,height=40)

        
        self.userLabel = Label(self.frame1, text=str(int(self.data1['main']['humidity']) ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 322 , width=150 ,height=40)
        

            #wind
        self.userLabel = Label(self.frame1, text='Wind -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15,) )
        self.userLabel.place(x =50 , y = 360 , width=150 ,height=40)

        
        self.userLabel = Label(self.frame1,text=str(int(self.data1['wind']['speed'])), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 360 , width=150 ,height=40)
        



        #frame 2
        self.data2, self.image2 = self.cityWeathers2(city2)
        self.frame2=Frame (self.root, bg='#91CEFF' )
        self.frame2.place (x=550, y=60 , width='300', height='500')

        self.weathImage1 = ImageTk.PhotoImage(Image.open(self.image2) . resize((100 ,100)))
        self.imageLabel2 = Label(self.frame2, image=self.weathImage1 , bg="#91CEFF")
        self.imageLabel2.place(x = 0, y = 50)

            #location
        
        self.lablel1=Label(self.frame2, text=city2.title(), font=('Bell MT',15) , bg= '#91CEFF' ,fg="#040405" )
        self.lablel1.place(x= 125, y=30 )
        
            
            #weather 
        self.userLabel = Label(self.frame2, text='°C'.title(), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
        self.userLabel.place(x =205 , y = 75 )
        
        self.userLabel = Label(self.frame2, text=str(int(self.data2['main']['temp']) - 273), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
        self.userLabel.place(x =170 , y = 75 )
       

            #feels like
        self.userLabel = Label(self.frame2, text='Feels Like -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =50 , y = 240 , width=150 ,height=40)

        
        self.userLabel = Label(self.frame2, text=str(int(self.data2['main']['feels_like']) - 273) + '°C', bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 240 , width=150 ,height=40)
       


            #visibility        
        self.userLabel = Label(self.frame2, text='Visibility -'.title(), bg ='#91CEFF',fg='white', font=('    Calbri   ',15,) )
        self.userLabel.place(x =50 , y = 280 , width=150 ,height=40)
        
        self.userLabel = Label(self.frame2, text=str(int(self.data2['visibility']) // 1000 ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 280 , width=150 ,height=40)
       

            #humidity
        self.userLabel = Label(self.frame2, text='Humidity -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =50 , y = 320 , width=150 ,height=40)

        
        self.userLabel = Label(self.frame2, text=str(int(self.data2['main']['humidity']) ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 322 , width=150 ,height=40)
       


            #wind
        self.userLabel = Label(self.frame2, text='Wind -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15,) )
        self.userLabel.place(x =50 , y = 360 , width=150 ,height=40)

        
        self.userLabel = Label(self.frame2,text=str(int(self.data2['wind']['speed'])), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 360 , width=150 ,height=40)
       



        self.data3, self.image3 = self.cityWeathers2(city3)

        self.frame3=Frame (self.root, bg='#91CEFF' )
        self.frame3.place (x=1000 , y=60 , width='300', height='500')

        self.weathImage2 = ImageTk.PhotoImage(Image.open(self.image3) . resize((100 ,100)))
        self.imageLabel3 = Label(self.frame3, image=self.weathImage2 , bg="#91CEFF")
        self.imageLabel3.place(x = 0, y = 50)


            #location

        
        self.lablel1=Label(self.frame3, text=city3.title(), font=('Bell MT',15) , bg= '#91CEFF' ,fg="#040405" )
        self.lablel1.place(x= 125, y=30 )
       
            
            #weather 
        self.userLabel = Label(self.frame3, text='°C'.title(), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
        self.userLabel.place(x =205 , y = 75 )
            
               
        self.userLabel = Label(self.frame3, text=str(int(self.data3['main']['temp']) - 273), bg ='#91CEFF' , fg='white', font=('Calbri',22,'bold') )
        self.userLabel.place(x =170 , y = 75 )
       
            #feels like
        self.userLabel = Label(self.frame3, text='Feels Like -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =50 , y = 240 , width=150 ,height=40)

        
        self.userLabel = Label(self.frame3, text=str(int(self.data3['main']['feels_like']) - 273) + '°C', bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 240 , width=150 ,height=40)
       

            #visibility        
        self.userLabel = Label(self.frame3, text='Visibility -'.title(), bg ='#91CEFF',fg='white', font=('    Calbri   ',15,) )
        self.userLabel.place(x =50 , y = 280 , width=150 ,height=40)
        
        self.userLabel = Label(self.frame3, text=str(int(self.data3['visibility']) // 1000 ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 280 , width=150 ,height=40)
       

            #humidity
        self.userLabel = Label(self.frame3, text='Humidity -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =50 , y = 320 , width=150 ,height=40)

        
        self.userLabel = Label(self.frame3, text=str(int(self.data3['main']['humidity']) ), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 322 , width=150 ,height=40)
       

            #wind
        self.userLabel = Label(self.frame3, text='Wind -'.title(), bg ='#91CEFF',fg='white', font=('Calbri',15,) )
        self.userLabel.place(x =50 , y = 360 , width=150 ,height=40)

        
        self.userLabel = Label(self.frame3,text=str(int(self.data3['wind']['speed'])), bg ='#91CEFF',fg='white', font=('Calbri',15 ))
        self.userLabel.place(x =180 , y = 360 , width=150 ,height=40)
       


        self.root.mainloop()

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

    

if __name__== '__main__' :
    obj= addcityadd()
    obj.frames()
   