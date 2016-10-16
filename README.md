# oanda_get_ohlc
Python Module for obtaining OHLC value from OANDA Restv20 API

get_rates Class

Returns 

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

	get_rates()["time"][n] = time
	get_rates()["openBid"][n] = openBid
	get_rates()["openAsk"][n] = openAsk
	get_rates()["highBid"][n] = highBid
	get_rates()["highAsk"][n] = highAsk
	get_rates()["lowBid"][n] = lowBid
	get_rates()["lowAsk"][n] = lowAsk
	get_rates()["closeBid"][n] = closeBid
	get_rates()["closeAsk"][n] = closeAsk
	get_rates()["volume"][n] = volume

Where "n" is the index of the candle. The latest candle information is at the last index.


Sample Code:

	Get_Rate = Ohlc("EUR_JPY","2","S15")
	print(Get_Rate.get_rates()["openBid"][0],type(test.get_rates()["openBid"][0]))
	print(Get_Rate.get_rates()["openAsk"][0],type(test.get_rates()["openAsk"][0]))
