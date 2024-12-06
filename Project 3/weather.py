import requests
from tkinter import Tk, Label, Entry, Button, StringVar

# Function to fetch weather data
def fetch_weather():
    city = city_var.get()
    api_key = "8c226e550d58b0ed840af69ecd9ee183"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            city_name = data["name"]
            temperature = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            result = (
                f"City: {city_name}\n"
                f"Temperature: {temperature}°C\n"
                f"Weather: {weather_desc.capitalize()}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
        else:
            result = "City not found. Please try again!"

    except Exception as e:
        result = "Error fetching data. Check your internet connection!"

    result_var.set(result)


# GUI Setup
root = Tk()
root.title("Weather Dashboard")
root.geometry("400x300")
root.resizable(False, False)

# Input field and labels
Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_var = StringVar()
Entry(root, textvariable=city_var, font=("Arial", 12), width=30).pack(pady=5)

Button(root, text="Get Weather", command=fetch_weather, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

result_var = StringVar()
Label(root, textvariable=result_var, font=("Arial", 12), justify="left", wraplength=350).pack(pady=20)

# Start the GUI loop
root.mainloop()
