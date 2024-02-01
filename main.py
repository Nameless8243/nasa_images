import streamlit as st
import requests
import os

api_key = "dhItL2ttrmYCnJGRko23iYmQlCFcEBv3VlxY3gfe"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

request = requests.get(url)
content = request.json()

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)
title = content.get("title")
explanation = content.get("explanation")
url = content.get("url")

with col1:
    st.write("")

with col2:
    st.title(title)
    st.image(url)
    st.write(explanation)

with col3:
    st.write("")
