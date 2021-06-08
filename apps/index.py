import streamlit as st
from .fetch_news import retrieve_business_news
import requests
import pandas as pd
from datetime import date
import yfinance as yf
from yahoo_fin import stock_info as si
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from .fetch_news import retrieve_news
from PIL import Image

import streamlit.components.v1 as components
def app():	
	title = Image.open('title.png')
	st.image(title, caption=' ')
	st.markdown("<hr/>", unsafe_allow_html=True)
	
	stock = yf.Ticker("^NSEI")
	stock = yf.Ticker("^BSESN")
	stock = yf.Ticker("^NSEBANK")
	stock = yf.Ticker("^CNXPSUBANKS")
	stock = yf.Ticker("^CNXMETAL")
	stock = yf.Ticker("^GSPC")
	stock = yf.Ticker("^DJI")
	stock = yf.Ticker("^IXIC")
	stock = yf.Ticker("^NYA")
	stock = yf.Ticker("^XAX")

	st.write(stock.info)
	def load_data(component):
		component_data=si.get_data(component)
		return component_data

	NSEI = load_data("^NSEI")
	BSESN = load_data("^BSESN")
	NSEBANK = load_data("^NSEBANK")
	CNXPSUBANKS = load_data("^CNXPSUBANKS")
	CNXMETAL = load_data("^CNXMETAL")
	GSPC = load_data("^GSPC")
	DJI = load_data("^DJI")
	IXIC = load_data("^IXIC")
	NYA = load_data("^NYA")
	XAX = load_data("^XAX")
	
	
	##st.write(stock)
	
	st.markdown("<hr/>", unsafe_allow_html=True)
	def write_data(component):


		shortname = (str(component['shortName']))
		marketstate = component['marketState']
		regularmarketprice = str(round(component['regularMarketPrice'],2))
		Changepercent = str(round(component['regularMarketChangePercent'],2))
		regularMarketChange = str(round(component['regularMarketChange'],2))

		low = Image.open('low.png')
		##st.image(low, caption=' ',width = 100)

		help = Image.open('help.png')
		


		if component['regularMarketChange'] > 0:
			st.markdown(f"<h style='text-align: center; font-size:20px; color: green; '>**{shortname} {marketstate} {regularmarketprice} {marketstate}**</h>", unsafe_allow_html=True)
			
				
		else:
			st.markdown(f"<h style='text-align: center; font-size:20px; color: red; '>**{shortname} {marketstate} {regularmarketprice} {marketstate}**</h>", unsafe_allow_html=True)  

	write_data(NSEI)
	st.markdown("<hr/>", unsafe_allow_html=True)
	write_data(BSESN)
