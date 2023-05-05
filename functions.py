from pandas_datareader import data as pdr
import yfinance as yf
import datetime
import json
yf.pdr_override()

def GetLatestTickersPrice(Tickers):
    enddate = datetime.datetime.now()
    startdate = datetime.datetime.today() - datetime.timedelta(days=5)
    data = pdr.get_data_yahoo(Tickers, start=startdate, end=enddate)
    json_obj = data.iloc[data.shape[0]-1,:].to_dict()
    return json_obj

