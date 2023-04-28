import streamlit as st


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
