# oanda_get_ohlc
Python Module for obtaining OHLC value from OANDA Restv20 API

Installation and Usage:

	Install Request

		pip install requests

	Clone Repository

		https://github.com/akosijonel/oanda_get_ohlc.git

	Import Class

		from OHLC import Ohlc

	Use get_rates Class


		Get_Rate = Ohlc("EUR_JPY","2","S15")


Parameters:
	
	Instrument: What Currency Pair to be queried.
		Format: currency1_currency2
		Data Type: String
		Sample: EUR_JPY

	Candle Count: How may candles will be queried. The last index will be the latest candle for the given period.
		Format: "Number"
		Data Type: String
		Sample: 2


	Period
		Sample Period: http://developer.oanda.com/rest-live/rates/


Data Available:

	get_rates()["time"][n] = time || Returns DateTime
	get_rates()["openBid"][n] = openBid || Returns Float
	get_rates()["openAsk"][n] = openAsk || Returns Float
	get_rates()["highBid"][n] = highBid || Returns Float
	get_rates()["highAsk"][n] = highAsk || Returns Float
	get_rates()["lowBid"][n] = lowBid || Returns Float
	get_rates()["lowAsk"][n] = lowAsk || Returns Float
	get_rates()["closeBid"][n] = closeBid || Returns Float
	get_rates()["closeAsk"][n] = closeAsk || Returns Float
	get_rates()["volume"][n] = volume || Returns Int

Where "n" is the index of the candle. The latest candle information is at the last index.

Sample Code:

	Get_Rate = Ohlc("EUR_JPY","2","S15")
	print(Get_Rate.get_rates()["openBid"][0],type(test.get_rates()["openBid"][0]))
	print(Get_Rate.get_rates()["openAsk"][0],type(test.get_rates()["openAsk"][0]))
