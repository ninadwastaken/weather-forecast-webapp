import requests
import streamlit

API_KEY = "6c113b952afccad18e5bbb5f79be4b41"

def get_data(place, days, option):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    try:
        data = response.json()["list"][: 8 * days]
        return data

    except KeyError:
        streamlit.info("please enter valid city name.")

    # if option == "temperature":
    #     filtered_data = [instance["main"]["temp"] for instance in data]
    # elif option == "sky":
    #     filtered_data = [instance["weather"][0]["main"] for instance in data]

if __name__ == "__main__":
    print(get_data(place="Bangalor", days=4, option="sky"))

