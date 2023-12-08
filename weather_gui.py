from tkinter import *
from typing import Optional, Dict, Tuple
class WeatherView:
    def __init__(self, master):
        """
        Initialize the WeatherView class.

        Parameters:
            master (Tk): The Tkinter root window.
        """
        self.master = master
        self.master.title('Weather')
        self.master.geometry('700x700+300+200')
        self.master.resizable(False, False)

        # Labels and Entry Widgets
        self.name = Label(self.master, font=('Comic Sans', 12, 'bold'))
        self.name.place(x=100, y=100)
        self.clock = Label(self.master, font=('Comic Sans', 20))
        self.clock.place(x=100, y=130)

        # Search
        self.search_image = PhotoImage(file='search.png')
        self.my_search_image = Label(image=self.search_image)
        self.my_search_image.place(x=20, y=20)

        self.search_frame = Frame(self.master, bg='#404040')
        self.search_frame.place(x=50, y=40)

        self.search_box = Entry(self.search_frame, justify='center', width=17, font=('Comic Sans', 20, "bold"), bg='#404040', border=0, fg='white')
        self.search_box.pack(side='left')
        self.search_box.focus()

        # State entry
        self.state_entry = Entry(self.search_frame, justify='center', width=10, font=('Comic Sans', 15), bg='#404040', border=0, fg='white')
        self.state_entry.pack(side='right')

        self.logo_image = PhotoImage(file='sunny_s_cloudy.png')
        self.logo = Label(image=self.logo_image)
        self.logo.place(x=20, y=100)

        self.enter_icon = PhotoImage(file='search_icon.png')
        self.my_search_image = Button(image=self.enter_icon, borderwidth=0, cursor='hand2', bg='#404040', command=None)  # command will be set in the controller
        self.my_search_image.place(x=400, y=34)

        self.label_wind = Label(self.master, text='Wind', font=('Comic Sans', 15, 'bold'), fg='white', bg='#1ab5ef')
        self.label_wind.place(x=20, y=350)

        self.label_humidity = Label(self.master, text='Humidity', font=('Comic Sans', 15, 'bold'), fg='white', bg='#1ab5ef')
        self.label_humidity.place(x=20, y=400)

        self.label_description = Label(self.master, text='Description', font=('Comic Sans', 15, 'bold'), fg='white', bg='#1ab5ef')
        self.label_description.place(x=20, y=300)

        self.label_feels_like = Label(self.master, text='Feels Like', font=('Comic Sans', 15, 'bold'), fg='white', bg='#1ab5ef')
        self.label_feels_like.place(x=20, y=250)

        self.label_temperature = Label(self.master, text='Temperature', font=('Comic Sans', 15, 'bold'), fg='white', bg='#1ab5ef')
        self.label_temperature.place(x=20, y=200)

        self.label_cloud_cover = Label(self.master, text='Cloud Cover', font=('Comic Sans', 15, 'bold'), fg='white', bg='#1ab5ef')
        self.label_cloud_cover.place(x=20, y=450)

        self.t = Label(self.master, font=('Comic Sans', 20, 'bold'), fg='black')
        self.t.place(x=30, y=500)

