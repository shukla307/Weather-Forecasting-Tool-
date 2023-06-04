import requests
import json
import tkinter as tk

def get_weather(city):
    api_key = "e5e894e064f2d1510b07bd3753ef0649"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = json.loads(response.text)

    if data.get("cod") == 200:
        weather = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        result_text.set(f"Weather in {city}: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%")
    else:
        error_message = data.get("message", "Something went wrong. Please try again.")
        result_text.set(error_message)

def fetch_weather():
    city = city_entry.get()
    get_weather(city)

window = tk.Tk()
window.title("Weather Forecasting Tool")
window.geometry("500x400") 

#Set the background color 
window.configure(bg="#FFFFFF")

frame = tk.Frame(window, bg="#FF0000")
frame.pack(pady=20)


# Created the input label and entry field
city_label = tk.Label(frame, text="Enter a city name:", bg="#FFFFFF", fg="#333333", font=("Arial", 12))
city_label.grid(row=0, column=0, padx=5, pady=5)
city_entry = tk.Entry(frame, font=("Arial", 12))
city_entry.grid(row=0, column=1, padx=5, pady=5)

# (for entering city name) fetching weather button
fetch_button = tk.Button(frame, text="Fetch Weather", command=fetch_weather, bg="#4CAF50", fg="white", font=("Arial", 12), width=15)
fetch_button.grid(row=1, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, bg="#FFFFFF", fg="#333333", font=("Arial", 12))
result_label.pack()

# the GUI event loop start from here
window.mainloop()
