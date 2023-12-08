from tkinter import messagebox, Tk
from weather_logic import *
from weather_gui import *
from geopy.geocoders import Nominatim

class WeatherController:
    """
    Controller class for the Weather App.

    Attributes:
        view (WeatherView): The associated view.
        geolocator (Nominatim): The geolocator for obtaining location information.
    """

    def __init__(self, view):
        """
        Initialize the WeatherController.

        Parameters:
            view (WeatherView): The associated view.
        """
        self.view = view
        self.geolocator = Nominatim(user_agent="weather_app")
        self.view.my_search_image.config(command=self.find_weather)

    def find_weather(self):
        """
        Find and display weather information for the specified location.

        Raises:
            Exception: If there is an error during the weather data retrieval or location not found.
        """
        try:
            city_state = f"{self.view.search_box.get()}, {self.view.state_entry.get()}"
            weather_data, error_message = get_weather_data(city_state)

            if error_message:
                raise Exception(error_message)

            location = self.geolocator.geocode(city_state)
            if location is None:
                raise Exception("Location not found. Please enter a valid city and state.")

            self.update_ui(weather_data)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
            return

    def update_ui(self, data):
        """
        Update UI elements using data from the weather model.

        Parameters:
            data (dict): Weather data received from the model.
        """
        # Update UI elements using data from the model
        self.view.name.config(text=f'Current Weather in {data["location"]}')
        self.view.clock.config(text=data["current_time"])

        # Update other labels
        self.view.label_wind.config(text=f"Wind: {mps_to_mph(data['weather_data']['wind']['speed']):.2f} mph")
        self.view.label_humidity.config(text=f"Humidity: {data['weather_data']['main']['humidity']}%")
        self.view.label_description.config(text=f"Description: {data['weather_data']['weather'][0]['description']}")
        self.view.label_feels_like.config(text=f"Feels Like: {kelvin_to_fahrenheit(data['weather_data']['main']['feels_like']):.2f} °F")
        self.view.label_temperature.config(text=f"Temperature: {kelvin_to_fahrenheit(data['weather_data']['main']['temp']):.2f} °F")
        self.view.label_cloud_cover.config(text=f"Cloud Cover: {data['weather_data']['clouds']['all']}%")

if __name__ == "__main__":
    gui = Tk()
    weather_view = WeatherView(gui)
    weather_controller = WeatherController(weather_view)
    gui.mainloop()