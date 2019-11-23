import requests
import tkinter as tk
def action():
    entered=city.get()
    def getcurrent(city):
        try:
            key='4df617f8ecb4be7c7faefb23c470f8ed'
            url='https://api.openweathermap.org/data/2.5/weather'
            para={'APPID':key,'q':city,'units':'Metric'}
            response=requests.get(url,params=para)
            currentWeather=response.json()
            print(currentWeather)
            list=[1,currentWeather['name'],(currentWeather['weather'][0]['description']).capitalize(),currentWeather['main']['temp'],str(currentWeather['main']['humidity']),str(currentWeather['wind']['speed']),"Thank You!"]
        except:
            list=[0,"There is problem in retrieving result!","Please:","1: Check your Internet Connection","2: Cannot Find City, Enter Correct City"]
        return list
    current=getcurrent(entered)
    print(current)
    if current[0]==0:
        label1=tk.Label(frame1,text=current[1],bg='#669999',width=40)
        label2=tk.Label(frame1,text=current[2],bg='#669999',width=40)
        label3=tk.Label(frame1,text="   "+current[3],bg='#669999',width=40)
        label4=tk.Label(frame1,text="   "+current[4],bg='#669999',width=40)
        label5=tk.Label(frame1,bg='#669999',width=45)
        label6=tk.Label(frame1,text="Sorry! For the inconvinience.",bg='brown',width=45)

        label1.place(x=0,y=0)
        label2.place(x=0,y=30)
        label3.place(x=0,y=60)
        label4.place(x=0,y=90)
        label5.place(x=0,y=120)
        label6.place(x=0,y=180)

    else:
        canvs=tk.Canvas(frame1,bg='#669999',width=500,height=500)
        label1=tk.Label(frame1,text='City: '+current[1],bg='#669999',width=40)
        label2=tk.Label(frame1,text='Condition: '+current[2],bg='#669999',width=40)
        label3=tk.Label(frame1,text='Temperature: '+str(current[3])+' celsius',bg='#669999',width=40)
        label4=tk.Label(frame1,text='Humidity: '+current[4]+'%',bg='#669999',width=40)
        label5=tk.Label(frame1,text='Wind Speed: '+current[5]+'m/s',bg='#669999',width=40)
        label6=tk.Label(frame1,text=current[6],width=45,bg="brown",fg='light yellow')

        label1.place(x=0,y=0)
        label2.place(x=0,y=30)
        label3.place(x=0,y=60)
        label4.place(x=0,y=90)
        label5.place(x=0,y=120)
        label6.place(x=0,y=180)

root=tk.Tk()
root.title("Check Current Weather ")
root.minsize(400,400)
root.maxsize(400,400)
canvas=tk.Canvas(root,bg="#0066cc",width=1080,height=1080).place(x=0,y=0)

frame=tk.Frame(root,bg='#669999')
frame.place(relx=0.5, rely=0.1,relwidth=0.75,relheight=0.15,anchor='n')

lable=tk.Label(frame,text="Enter name of city :",bg='#669999')
lable.place(relx=0.1,rely=0.10,relwidth=.85)
lab=tk.Label(lable,text="Hello, Please",bg='#669999')
lab.place(relx=0,rely=-.10)

city=tk.StringVar()

entry=tk.Entry(lable,textvariable=city)
entry.place(relx=.75,rely=.10)

button=tk.Button(frame,text="Get Weather",command=action, bg="light green")
button.place(relx=0.73,rely=0.70,relwidth=0.25,relheight=0.25)

frame1=tk.Frame(root,bg='#669999')
frame1.place(relx=0.13,rely=.35,relwidth=.75,relheight=0.75)

root.mainloop()
