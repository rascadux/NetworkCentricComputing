from tkinter import Frame, PhotoImage, Label, Tk
from tkmacosx import Button
import webview
from PIL import Image
import requests
import time

class Window(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.click = True
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.frame = Frame(self.master, bg='white', highlightbackground='deep pink', highlightthickness=0)
        self.frame.grid(columnspan=4, row=0, sticky='nsew', padx=0, pady=0)
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
        
        self.cityChosen=''
        
        self.widgets()


    def getWeather(self, city, map):

            key = 'a273872490d48a1c7e015db72d38217f'

            if map == 'current':
                API = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + key

            if map == 'forecast' and city == 'Maribor':
                webview.create_window('Forecast Maribor', height=600, width=1000, url='https://openweathermap.org/city/3196359')
                webview.start()
                return

            if map == 'forecast' and city == 'La Coruña':
                webview.create_window('Forecast La Coruña', height=600, width=1000, url='https://openweathermap.org/city/3119841')
                webview.start()
                return

            if map == 'precipitation':
                webview.create_window('Precipitation', height=600, width=1000, url='https://openweathermap.org/weathermap?basemap=map&cities=false&layer=radar&lat=46&lon=15&zoom=4')
                webview.start()
                return

            if map == 'temperature':
                webview.create_window('temperature', height=600, width=1000, url='https://openweathermap.org/weathermap?basemap=map&cities=false&layer=temperature&lat=46&lon=15&zoom=4')
                webview.start()
                return

            if map == 'pressure':
                webview.create_window('pressure', height=600, width=1000, url='https://openweathermap.org/weathermap?basemap=map&cities=false&layer=pressure&lat=46&lon=15&zoom=4')
                webview.start()
                return

            if map == 'wind':
                webview.create_window('wind', height=600, width=1000, url='https://openweathermap.org/weathermap?basemap=map&cities=false&layer=windspeed&lat=46&lon=15&zoom=4')
                webview.start()
                return

            if map == 'clouds':
                webview.create_window('clouds', height=600, width=1000, url='https://openweathermap.org/weathermap?basemap=map&cities=false&layer=clouds&lat=46&lon=15&zoom=4')
                webview.start()
                return
            
            

            try:
                json_data = requests.get(API).json()
                self.temp['text'] = str(int(json_data['main']['temp'] - 273.15)) + ' °C'
                self.temp_min['text'] = str(int(json_data['main']['temp_min'] - 273.15)) + ' °C'
                self.temp_max['text'] = str(int(json_data['main']['temp_max'] - 273.15)) + ' °C'
                self.pressure['text'] = str(json_data['main']['pressure']) + ' hPa'
                self.humidity['text'] = str(json_data['main']['humidity']) + ' %'
                self.wind['text'] = str(int(json_data['wind']['speed'])*18/5) + ' km/h'
                #self.place['text'] = str(json_data['name']) + ' - ' + json_data['sys']['country']
                
                
            except:
                #self.warning['text'] = 'Error :('
                self.temp['text'] = 'Choose a location first!'
                self.temp_min['text'] = ':  ('
                self.temp_max['text'] = ':  ('
                self.pressure['text'] = ':  ('
                self.humidity['text'] = ':  ('
                self.wind['text'] = ':  ('
                self.master.update()
                time.sleep(1)
                #self.warning['text'] = ''
                #self.place['text'] = ''
                

    def setCity(self, city):
        self.cityChosen = city


    def widgets(self):
        #self.init = PhotoImage(file = 'search.png')
        self.image_temp = PhotoImage(file = 'temperatura.png')
        self.image_temp_min = PhotoImage(file = 'temp_min.png')
        self.image_temp_max = PhotoImage(file = 'temp_max.png')
        self.image_pressure = PhotoImage(file = 'presion.png')
        self.image_humidity = PhotoImage(file = 'humedad.png')
        self.image_wind = PhotoImage(file = 'viento.png')

        #self.bt_city1 = Button(self.frame, text='Maribor', bg='red', highlightthickness=0, activebackground='white', bd=0, command=self.animation)
        #self.bt_city1.grid(column=0, row=0, padx=2, pady=2)
        #self.bt_city2 = Button(self.frame, text='A Coruña', bg='red', highlightthickness=0, activebackground='white', bd=0, command=self.animation)
        #self.bt_city1.grid(column=1, row=0)

            
        
        self.bt_city1 = Button(self.frame, padx=5, width=200 ,height=30, bg='#ABF979', activebackground='grey', font=('Copperplate', 15), text='Maribor', highlightthickness=0, bd=0, command=lambda: self.setCity('Maribor'))
        self.bt_city1.grid(column=0, row=0, padx=(3, 80), pady=3)
        self.bt_city2 = Button(self.frame, padx=5, width=200, height=30, bg='#F99079', activebackground='grey', font=('Copperplate', 15), text='La Coruña', highlightthickness=0, bd=0, command=lambda: self.setCity('La Coruña'))
        self.bt_city2.grid(column=0, row=1, padx=(3, 80), pady=0)


        self.bt_current = Button(self.frame, width=170, height=30, bg='grey', activebackground='grey', font=('Copperplate', 15), text='Current Weather', highlightthickness=0, bd=0, command=lambda: self.getWeather(self.cityChosen, 'current'))
        self.bt_current.grid(column=1, row=0, padx=3, pady=3)
        self.bt_forecast  = Button(self.frame, width=170, height=30, bg='grey', activebackground='grey', font=('Copperplate', 15), text='5 day / 3h Forecast', highlightthickness=0, bd=0, command=lambda: self.getWeather(self.cityChosen, 'forecast'))
        self.bt_forecast.grid(column=1, row=1, padx=3, pady=3)
        self.bt_precipitationMap = Button(self.frame, width=170, height=30, bg='grey', activebackground='grey', font=('Copperplate', 15), text='Precipitation Map', highlightthickness=0, bd=0, command=lambda: self.getWeather('', 'precipitation'))
        self.bt_precipitationMap.grid(column=2, row=0, padx=3, pady=1)
        self.bt_temperatureMap = Button(self.frame, width=170, height=30, bg='grey', activebackground='grey', font=('Copperplate', 15), text='Temperature Map', highlightthickness=0, bd=0, command=lambda: self.getWeather('', 'temperature'))
        self.bt_temperatureMap.grid(column=2, row=1, padx=3, pady=3)
        self.bt_pressureMap = Button(self.frame, width=170, height=30, bg='grey', activebackground='grey', font=('Copperplate', 15), text='Pressure Map', highlightthickness=0, bd=0, command=lambda: self.getWeather('', 'pressure'))
        self.bt_pressureMap.grid(column=3, row=0, padx=3, pady=1)
        self.bt_windMap = Button(self.frame, width=170, height=30, bg='grey', activebackground='grey', font=('Copperplate', 15), text='Wind Map', highlightthickness=0, bd=0, command=lambda: self.getWeather('', 'wind'))
        self.bt_windMap.grid(column=3, row=1, padx=3, pady=3)
        self.bt_cloudMap = Button(self.frame, width=170, height=30, bg='grey', activebackground='grey', font=('Copperplate', 15), text='Cloud Map', highlightthickness=0, bd=0, command=lambda: self.getWeather('', 'clouds'))
        self.bt_cloudMap.grid(column=4, row=0, padx=3, pady=1)


        self.lb_temp = Label(self.frame2, text = 'Temperature', bg='SeaGreen1', fg='black')
        self.lb_temp.pack(expand=True)
        self.lb_min_temp = Label(self.frame3, text = 'Min Temperature', bg='turquoise', fg='black')
        self.lb_min_temp.pack(expand=True)
        self.lb_max_temp = Label(self.frame4, text = 'Max Temperature', bg='tomato', fg='black')
        self.lb_max_temp.pack(expand=True)
        self.lb_pressure = Label(self.frame5, text = 'Pressure', bg='cyan2', fg='black')
        self.lb_pressure.pack(expand=True)
        self.lb_humidity = Label(self.frame6, text = 'Humidity', bg='lightslategrey', fg='black')
        self.lb_humidity.pack(expand=True)
        self.lb_wind = Label(self.frame7, text = 'Wind Speed', bg='sky blue', fg='black')
        self.lb_wind.pack(expand=True)

        self.imageTemp = Label(self.frame2, image=self.image_temp, bg='SeaGreen1')
        self.imageTemp.pack(expand=True, side='left')
        self.imageTempMin = Label(self.frame3, image=self.image_temp_min, bg='turquoise')
        self.imageTempMin.pack(expand=True, side='left')
        self.imageTempMax = Label(self.frame4, image=self.image_temp_max, bg='tomato')
        self.imageTempMax.pack(expand=True, side='left')
        self.imagePressure = Label(self.frame5, image=self.image_pressure, bg='cyan2')
        self.imagePressure.pack(expand=True, side='left')
        self.imageHumidity = Label(self.frame6, image=self.image_humidity, bg='lightslategrey')
        self.imageHumidity.pack(expand=True, side='left')
        self.imageWind = Label(self.frame7, image=self.image_wind, bg='sky blue')
        self.imageWind.pack(expand=True, side='left')

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
    window.geometry('500x300+250+80')
    app = Window(window)
    app.mainloop()






