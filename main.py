import streamlit as st
import plotly.express as px
from backend import get_data

# st.set_page_config(layout="wide")
st.title("Weather Forecast for upcoming Days".lower())
place = st.text_input("place:")
days = st.slider("forecast days", min_value=1, max_value=5,
                 help="select the number of days that appear in graph.")
option = st.selectbox("select data", ("temperature", "sky"))

if place == "":
    st.subheader("please enter the desired city "
                 "for which weather forecast will be done!")
elif days == 1:
    st.subheader(f"{option} for the next day in {place.lower()}:")
else:
    st.subheader(f"{option} for the next {days} days in {place.lower()}:")

if place:
    data = get_data(place, days, option)
    if data:
        if option == "temperature":
            temperatures = [instance["main"]["temp"] / 10 for instance in data]
            dates = [instance["dt_txt"] for instance in data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "date", "y": "temperature (in C)"})
            st.plotly_chart(figure)


        elif option == "sky":
            images = {"Clear": "sky_images/clear.png", "Clouds": "sky_images/cloud.png",
                      "Snow": "sky_images/snow.png", "Rain": "sky_images/rain.png"}
            weathers = [instance["weather"][0]["main"] for instance in data]
            links = [images[weather] for weather in weathers]
            st.image(links, width=200)

