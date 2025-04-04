import requests


class Wx1Fetcher:
    def __init__(self, location):
        self.location = location

    def get_weather(self):
        url = f"https://wttr.in/{self.location}?format=%l+%C+%t+%f+%h+%w+%P+%p+%u+%S+%s"
        response = requests.get(url)
        if response.status_code == 200:
            response_text = response.text.replace("Partly ", "")
            response_text = response_text.replace("Light ", "")
            response_text = response_text.replace(" shower", "")
            wx1_info = response_text.split()
            location = wx1_info[0].strip()
            condition = wx1_info[1].strip()
            temperature = wx1_info[2].strip()
            temperature = wx1_info[3].strip()
            Humidity = wx1_info[4].strip()
            wind = wx1_info[5].strip()
            Precipitation = wx1_info[7].strip()
            Pressure = wx1_info[6].strip()
            dawn = wx1_info[-2].strip()
            sunset = wx1_info[-1].strip()

            emojis = {
                "☁️": ["Cloudy", "Overcast", "cloudy"],
                "🌤️": ["Partly", "Partly cloudy"],
                "": ["Sunny", "Clear"],
                "🌧️": [
                    "Rain",
                    "rain",
                    "Light rain",
                    "Drizzle",
                    "Light shower rain",
                    "Rain shower",
                ],
                "🌩️": ["Thunderstorm"],
                "❄": ["Snow", "Light snow", "Light shower snow"],
                "🌨️": ["Snow shower", "Shower snow"],
                "🌬️": ["Windy"],
                "🌫️": ["Mist", "Fog"],
            }

            selected_emoji = next(
                (
                    emoji
                    for emoji, conditions in emojis.items()
                    if condition in conditions
                ),
                None,
            )
            output = f"{location}\n"
            output += f"{selected_emoji} {condition}\n"
            output += f"temperature🌡️ {temperature}\n"
            output += f"feels like🌡️ {temperature}\n"
            output += f"humidity🌡️ {Humidity}\n"
            output += f"wind speed 💨 {wind}\n"
            output += f"rainfall 🌨️ {Precipitation}\n"
            output += f"pressure ⏲  {Pressure}\n"
            output += f"dawn 🌞 {dawn}\n"
            output += f"sunset 🌛 {sunset}\n"
            return output
        else:
            return "Failed to fetch weather data."


# Example usage:
 #location = "Swansea"
# weather_fetcher = Wx1Fetcher(location)
# weather_data = weather_fetcher.get_weather()
#print(weather_data)
