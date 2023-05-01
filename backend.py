import requests



API_KEY = "6c113b952afccad18e5bbb5f79be4b41"

def get_data(place, days, option):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()["list"][: 8 * days]

    if option == "temperature":
        filtered_data = [instance["main"]["temp"] for instance in data]
    elif option == "sky":
        filtered_data = [instance["weather"][0]["main"] for instance in data]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Bangalore", days=4, option="sky"))

