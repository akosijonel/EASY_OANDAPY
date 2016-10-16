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

			timeValue = self.response["json"]["candles"][candle_iter]["time"]
			openBidValue = float(self.response["json"]["candles"][candle_iter]["openBid"])
			openAskValue = float(self.response["json"]["candles"][candle_iter]["openAsk"])
			highBidValue = float(self.response["json"]["candles"][candle_iter]["highBid"])
			highAskValue = float(self.response["json"]["candles"][candle_iter]["highAsk"])
			lowBidValue = float(self.response["json"]["candles"][candle_iter]["lowBid"])
			lowAskValue = float(self.response["json"]["candles"][candle_iter]["lowAsk"])
			closeBidValue = float(self.response["json"]["candles"][candle_iter]["closeBid"])
			closeAskValue = float(self.response["json"]["candles"][candle_iter]["closeAsk"])
			volumeValue = self.response["json"]["candles"][candle_iter]["volume"]

			AskBodyValue = self.Pips(openAskValue,closeAskValue,highAskValue,lowAskValue)["body"]
			AskTopValue = self.Pips(openAskValue,closeAskValue,highAskValue,lowAskValue)["top"]
			AskBottomValue = self.Pips(openAskValue,closeAskValue,highAskValue,lowAskValue)["bottom"]

			BidBodyValue = self.Pips(openBidValue,closeBidValue,highBidValue,lowBidValue)["body"]
			BidTopValue = self.Pips(openBidValue,closeBidValue,highBidValue,lowBidValue)["top"]
			BidBottomValue = self.Pips(openBidValue,closeBidValue,highBidValue,lowBidValue)["bottom"]


			time.insert(candle_length,timeValue)
			openBid.insert(candle_length,openBidValue)
			openAsk.insert(candle_length,openAskValue)
			highBid.insert(candle_length,highBidValue)
			highAsk.insert(candle_length,highAskValue)
			lowBid.insert(candle_length,lowBidValue)
			lowAsk.insert(candle_length,lowAskValue)
			closeBid.insert(candle_length,closeBidValue)
			closeAsk.insert(candle_length,closeAskValue)
			volume.insert(candle_length,volumeValue)
			AskBody.insert(candle_length,AskBodyValue)
			AskTop.insert(candle_length,AskTopValue)
			AskBottom.insert(candle_length,AskBottomValue)
			BidBody.insert(candle_length,BidBodyValue)
			BidTop.insert(candle_length,BidTopValue)
			BidBottom.insert(candle_length,BidBottomValue)

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
		ohlc_values["AskBody"] = AskBody
		ohlc_values["AskTop"] = AskTop
		ohlc_values["AskBottom"] = AskBottom
		ohlc_values["BidBody"] = BidBody
		ohlc_values["BidTop"] = BidTop
		ohlc_values["BidBottom"] = BidBottom

		return ohlc_values



	def Pips(self,openValue,closeValue,HighValue,LowValue):
		PipValue = {}
		if openValue < closeValue:
			PipValue["body"] = (closeValue - openValue) / 0.01
			PipValue["top"] = (HighValue - closeValue) / 0.01
			PipValue["bottom"] = (openValue - LowValue) / 0.01

		elif openValue > closeValue:
			PipValue["body"] = (openValue - closeValue) / 0.01
			PipValue["top"] = (HighValue - openValue) / 0.01
			PipValue["bottom"] = (closeValue - LowValue) / 0.01

		elif openValue == closeValue:
			PipValue["body"] = 0
			PipValue["top"] = (HighValue - closeValue) / 0.01
			PipValue["bottom"] = (openValue - LowValue) / 0.01

		return PipValue


