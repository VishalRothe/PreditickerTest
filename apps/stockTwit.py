
import streamlit as st
import requests

def app():
	st.write("hello")
	symbol = st.text_input("Symbol")
	if symbol=="":
		r = requests.get("https://api.stocktwits.com/api/2/streams/trending.json")
	else:
		r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")

	data = r.json()

	for message in data['messages']:
		st.image(message['user']['avatar_url'])
		st.write(message['user']['username'])
		st.write(message['created_at'])
		st.write(message['body'])
		
		




	