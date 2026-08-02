import requests
from config import API_KEY

def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("cod") == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            
            print(f"\n--- Weather in {city_name.title()} ---")
            print(f"Temperature : {temp}°C")
            print(f"Condition   : {description.capitalize()}")
            print(f"Humidity    : {humidity}%\n")
        else:
            print(f"\nError: {data.get('message', 'City not found.')}\n")
            
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")

if __name__ == "__main__":
    print("=== Command-Line Weather App ===")
    city = input("Enter a city name (e.g., New Delhi): ").strip()
    if city:
        get_weather(city)
    else:
        print("City name cannot be empty!")