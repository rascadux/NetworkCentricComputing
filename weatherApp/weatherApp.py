from tkinter import *
from PIL import Image
import requests
import time

class Window(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.click = True
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.frame = Frame(self.master, bg='white', highlightbackground='deep pink', highlightthickness=2)
        self.frame.grid(columnspan=3, row=0, sticky='nsew', padx=5, pady=5)
        self.frame2 = Frame(self.master, bg='SeaGreen1', highlightbackground='dark violet', highlightthickness=2)
        self.frame2.grid(column=0, row=1, sticky='nsew', padx=5, pady=5)
        self.frame3 = Frame(self.master, bg='turquoise', highlightbackground='dark violet', highlightthickness=2)
        self.frame3.grid(column=1, row=1, sticky='nsew', padx=5, pady=5)
        self.frame4 = Frame(self.master, bg='tomato', highlightbackground='dark violet', highlightthickness=2)
        self.frame4.grid(column=2, row=1, sticky='nsew', padx=5, pady=5)
        self.frame5 = Frame(self.master, bg='cyan2', highlightbackground='dark violet', highlightthickness=2)
        self.frame5.grid(column=0, row=2, sticky='nsew', padx=5, pady=5)
        self.frame6 = Frame(self.master, bg='lightslategrey', highlightbackground='dark violet', highlightthickness=2)
        self.frame6.grid(column=1, row=2, sticky='nsew', padx=5, pady=5)
        self.frame7 = Frame(self.master, bg='sky blue', highlightbackground='dark violet', highlightthickness=2)
        self.frame7.grid(column=2, row=2, sticky='nsew', padx=5, pady=5)

        self.widgets()

    def animation(self):
        self.frame.config(highlightbackground='red')
        self.frame2.config(highlightbackground='red')
        self.frame3.config(highlightbackground='red')
        self.frame4.config(highlightbackground='red')
        self.frame5.config(highlightbackground='red')
        self.frame6.config(highlightbackground='red')
        self.frame7.config(highlightbackground='red')
        self.getTime()
        self.master.update()
        '''gif = Image.open('search.png')
        frames = gif.n_frames
        if self.click == True:
            for i in range(1, frames):
                self.init = PhotoImage(file = 'search.png', format = 'gif -index %i' %(i))
                self.bt_init['image'] = self.init
                time.sleep(0.04)
                self.master.update()
                self.click = False
                if i + 1 == frames:
                    self.click = True'''

    def getTime(self):
            city = self.set_City.get()
            #key = 'a273872490d48a1c7e015db72d38217f'

            #API current weather = 'api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'

            #API 5 day / 3 hour = 'api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}'

            #API Weather Map = 'https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={API key}'

            #{layer} = 'clouds_new', 'precipitation_new', 'pressure_new', 'wind_new', 'temp_new'

            API = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=a273872490d48a1c7e015db72d38217f'

            try:
                json_data = requests.get(API).json()
                self.temp['text'] = str(int(json_data['main']['temp'] - 273.15)) + ' °C'
                self.temp_min['text'] = str(int(json_data['main']['temp_min'] - 273.15)) + ' °C'
                self.temp_max['text'] = str(int(json_data['main']['temp_max'] - 273.15)) + ' °C'
                self.pressure['text'] = str(json_data['main']['pressure']) + ' hPa'
                self.humidity['text'] = str(json_data['main']['humidity']) + ' %'
                self.wind['text'] = str(int(json_data['wind']['speed'])*18/5) + ' km/h'
                self.place['text'] = str(json_data['name']) + ' - ' + json_data['sys']['country']
            except:
                self.warning['text'] = 'Error :('
                self.temp['text'] = ':  ('
                self.temp_min['text'] = ':  ('
                self.temp_max['text'] = ':  ('
                self.pressure['text'] = ':  ('
                self.humidity['text'] = ':  ('
                self.wind['text'] = ':  ('
                self.master.update()
                time.sleep(1)
                self.warning['text'] = ''
                self.place['text'] = ''

    def widgets(self): 
        self.init = PhotoImage(file = 'search.png')
        self.image_temp = PhotoImage(file = 'temperatura.png')
        self.image_temp_min = PhotoImage(file = 'temp_min.png')
        self.image_temp_max = PhotoImage(file = 'temp_max.png')
        self.image_pressure = PhotoImage(file = 'presion.png')
        self.image_humidity = PhotoImage(file = 'humedad.png')
        self.image_wind = PhotoImage(file = 'viento.png')

        self.bt_init = Button(self.frame, image=self.init, bg='red', highlightthickness=0, activebackground='white', bd=0, command=self.animation)
        self.bt_init.grid(column=0, row=0, padx=2, pady=2)
        self.set_City = Entry(self.frame, font=('Comic Sans MS', 12), highlightbackground='DarkOrchid1', highlightcolor= 'green2', highlightthickness=2)
        self.set_City.grid(column=1, row=0)
        Label(self.frame, text='City', fg='gray55',font=('Comic Sans MS', 10), bg='white').grid(column=2, row=0, padx=5)
        self.warning = Label(self.frame, fg='red2', font=('Comic Sans MS', 12), bg='white')
        self.warning.grid(column=3, row=0, padx=5)
        self.place = Label(self.frame, fg='magenta', font=('Arial', 12, 'bold'), bg='white')
        self.place.grid(column=4, row=0, padx=5)

        Label(self.frame2, text = 'Temperature', bg='SeaGreen1', fg='black').pack(expand=True)
        Label(self.frame3, text = 'Temperature Min', bg='turquoise', fg='black').pack(expand=True)
        Label(self.frame4, text = 'Temperature Max', bg='tomato', fg='black').pack(expand=True)
        Label(self.frame5, text = 'Pressure', bg='cyan2', fg='black').pack(expand=True)
        Label(self.frame6, text = 'Humidity', bg='lightslategrey', fg='black').pack(expand=True)
        Label(self.frame7, text = 'Wind Speed', bg='sky blue', fg='black').pack(expand=True)

        Label(self.frame2, image=self.image_temp, bg='SeaGreen1').pack(expand=True, side='left')
        Label(self.frame3, image=self.image_temp_min, bg='turquoise').pack(expand=True, side='left')
        Label(self.frame4, image=self.image_temp_max, bg='tomato').pack(expand=True, side='left')
        Label(self.frame5, image=self.image_pressure, bg='cyan2').pack(expand=True, side='left')
        Label(self.frame6, image=self.image_humidity, bg='lightslategrey').pack(expand=True, side='left')
        Label(self.frame7, image=self.image_wind, bg='sky blue').pack(expand=True, side='left')

        self.temp = Label(self.frame2, font=('Impact', 20), bg='SeaGreen1')
        self.temp.pack(expand=True, side='right')
        self.temp_min = Label(self.frame3, font=('Impact', 20), bg='turquoise')
        self.temp_min.pack(expand=True, side='right')
        self.temp_max = Label(self.frame4, font=('Impact', 20), bg='tomato')
        self.temp_max.pack(expand=True, side='right')
        self.pressure = Label(self.frame5, font=('Impact', 20), bg='cyan2')
        self.pressure.pack(expand=True, side='right')
        self.humidity = Label(self.frame6, font=('Impact', 20), bg='lightslategrey')
        self.humidity.pack(expand=True, side='right')
        self.wind = Label(self.frame7, font=('Impact', 20), bg='sky blue')
        self.wind.pack(expand=True, side='right')

if __name__ == '__main__':
    window = Tk()
    window.title('Weather')
    window.config(bg='white')
    window.minsize(height=600, width=1000)
    window.call('wm', 'iconphoto', window._w, PhotoImage(file='temperatura.png'))
    window.geometry('500x300+180+80')
    app = Window(window)
    app.mainloop()






