import requests
import json

response = {}

class Ohlc:
	def __init__(self,instrument,count,time):
		#Instruments - Currency pair <Currency1>_<Currency2>
		#Count - Number of Candle information
		#Time - Time Alignment. Check for http://developer.oanda.com/rest-live/rates/
		self.instrument = instrument
		self.count = count
		self.time = time
		self.response = {}
		self.response["raw"] = requests.get('https://api-fxtrade.oanda.com/v1/candles?instrument={}&count={}&candleFormat=bidask&granularity={}'.format(self.instrument,self.count,self.time))
		self.response["json"] = self.response["raw"].json()


	def get_rates(self):
		ohlc_values = {}
		candle_length = len(self.response["json"]["candles"])
		time,openBid,openAsk,highBid,highAsk,lowBid,lowAsk,closeBid,closeAsk,volume,AskBody,AskTop,AskBottom,BidBody,BidTop,BidBottom = ([] for i in range(16))
		for candle_iter in range(candle_length):
			time.insert(candle_length,self.response["json"]["candles"][candle_iter]["time"])
			openBid.insert(candle_length,float(self.response["json"]["candles"][candle_iter]["openBid"]))
			openAsk.insert(candle_length,float(self.response["json"]["candles"][candle_iter]["openAsk"]))
			highBid.insert(candle_length,float(self.response["json"]["candles"][candle_iter]["highBid"]))
			highAsk.insert(candle_length,float(self.response["json"]["candles"][candle_iter]["highAsk"]))
			lowBid.insert(candle_length,float(self.response["json"]["candles"][candle_iter]["lowBid"]))
			lowAsk.insert(candle_length,float(self.response["json"]["candles"][candle_iter]["lowAsk"]))
			closeBid.insert(candle_length,float(self.response["json"]["candles"][candle_iter]["closeBid"]))
			closeAsk.insert(candle_length,float(self.response["json"]["candles"][candle_iter]["closeAsk"]))
			volume.insert(candle_length,int(self.response["json"]["candles"][candle_iter]["volume"]))
			ohlc_values["time"] = time
			ohlc_values["openBid"] = openBid
			ohlc_values["openAsk"] = openAsk
			ohlc_values["highBid"] = highBid
			ohlc_values["highAsk"] = highAsk
			ohlc_values["lowBid"] = lowBid
			ohlc_values["lowAsk"] = lowAsk
			ohlc_values["closeBid"] = closeBid
			ohlc_values["closeAsk"] = closeAsk
			ohlc_values["volume"] = volume
		return ohlc_values



