from  tkinter import * 
import tkinter as tk
from tkinter import ttk,messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import requests 

root = Tk()
root.title('weather App')
root.geometry("900x500+300+200")
root.resizable(False,False)

#fun of weather get 

def getweather():
    
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent='geoapiexercise')
        location =geolocator.geocode(city)
        obj =TimezoneFinder()
        result =obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
        home  = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time =local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        ttime.config(text="CURRENT WEATHER")
    
        #weather
        api= "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=4525d75c477010e4dc948acc20b48dc1"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description= json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity =json_data['main']['humidity']
        wind =json_data['wind']['speed']
    
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    
        w.config(text=wind)
        h.config(text=humidity)
        D.config(text=description)
        p.config(text=pressure)
        
    except Exception as e:
        messagebox.showerror('weather App','invalid Entry!!')
         
    
    
#search box 

search_imgae = PhotoImage(file='Copy of search.png')
my_image = Label(image=search_imgae)
my_image.place(x=20,y=20)

# text area 

textfield = tk.Entry(root,justify='center',width=17,font=('poppins',17,'bold'),border=0,bg= "#404040",fg='white')
textfield.place(x=50,y=40)
textfield.focus()

# search icons 

search_iocns = PhotoImage(file='copy of search_icon.png')
icons_image = Button(image=search_iocns,borderwidth=0,cursor="hand2",bg='#404040',command=getweather)
icons_image.place(x=400,y=34)


# logo 
logo_image = PhotoImage(file='copy of logo.png')
my_logo_image = Label(image=logo_image)
my_logo_image.place(x=150,y=100) 

#button box 
but_box = PhotoImage(file='copy of box.png')
but_my_box =Label(image=but_box)
but_my_box.pack(padx=5,pady=5,side=BOTTOM)

# time 
ttime = Label(root,font=('arial',15,'bold'))
ttime.place(x=30,y=100)
clock = Label(root,font=("helvetica",20))
clock.place(x=30,y=130)

# label wind
Label1 =Label(root,text='WIND',font=("Helvetica",15,'bold'),fg='white',bg="#1ab5ef")
Label1.place(x=120,y=400)

# humidity
label2 = Label(root,text="humidity",font=('helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label2.place(x=250,y=400)

# descripiton
label3 = Label(root,text="Description",font=('helvetica',15,'bold'),fg="white",bg='#1ab5ef')
label3.place(x=430,y=400)

#presure
label4 = Label(root,text='Pressure',font=("helvetica",15,'bold'),fg='white',bg="#1ab5ef")
label4.place(x=650,y=400)

# inside blue box ex wind , desc,humi,pre, input space 

t = Label(font=('arial',70,'bold'),fg='#ee666d')
t.place(x=400,y=150)

c = Label(font=('arial',15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=('arial',20,'bold'),bg='#1ab5ef')
w.place(x=120,y=430)

h=Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef')
h.place(x=280,y=430)

D=Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef')
D.place(x=450,y=430)

p=Label(text='...',font=('arial',20,'bold'),bg='#1ab5ef')
p.place(x=670,y=430)

root.mainloop()