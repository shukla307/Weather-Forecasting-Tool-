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
window.geometry("600x400") 


window.configure(bg="#D3E7F0")

frame = tk.Frame(window, bg="#D3E7F0")
frame.pack(pady=20)


city_label = tk.Label(frame, text="Enter a city name:", bg="#D3E7F0", fg="#333333", font=("Arial", 14))
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(frame, font=("Arial", 14))
city_entry.grid(row=0, column=1, padx=10, pady=10)

fetch_button = tk.Button(frame, text="Fetch Weather", command=fetch_weather, bg="#4CAF50", fg="white", font=("Arial", 14), width=15)
fetch_button.grid(row=1, column=0, columnspan=2, pady=20)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, bg="#D3E7F0", fg="#333333", font=("Arial", 14))
result_label.pack()

window.mainloop()

