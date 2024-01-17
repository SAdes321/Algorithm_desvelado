import datetime
from pymongo import MongoClient
import pandas as pd

'''Timestamp inputs input should be given as seconds 
    since UNIX epoch wherever required'''

def getHistData1Min(timestamp, symbol,conn = None):
    '''Used to fetch data for a single symbol at a 
        particular time, returns data as a dictionary'''
    
    if not conn:
        conn = MongoClient()
        '''Provide the connection object else the code 
            will try to connect to MongoDB running on localhost'''
    
    db = conn['OHLC_MINUTE_1']
    collection = db.Data
    rec = collection.find_one(
            {'$and':[{'sym':symbol},
            {"ti": timestamp}]})
    
    if rec:
        return rec
    else:
        raise Exception (f"Data not found for {symbol} at {datetime.datetime.fromtimestamp(timestamp)}")

def getBackTestData1Min(startDateTime, endDateTime, symbol, conn = None ):
    '''Used to fetch data for a single symbol 
        for a given date range, returns data as 
        a pandas dataframe'''
    
    if not conn:
        conn = MongoClient()
        '''Provide the connection object else the code 
            will try to connect to MongoDB running on localhost'''
    
    db = conn['OHLC_MINUTE_1']
    collection = db.Data
    
    rec = collection.find(
            {'$and':
            [
                {'sym':symbol},
                {"ti":{'$gte':startDateTime,'$lte':endDateTime}}
            ]
            })
    
    if rec:
        df = pd.DataFrame(list(rec))
        return df
    else:
        raise Exception (f"Data not found for {symbol} in range {datetime.datetime.fromtimestamp(startDateTime)} to {datetime.datetime.fromtimestamp(endDateTime)}")

def getCurrentExpiry(timestamp):
    
    ''' Used to get the option expiry for a particular date'''
    
    testDate = datetime.datetime.fromtimestamp(timestamp)
    
    date = int(testDate.strftime('%d'))
    month = int(testDate.strftime('%m'))
    year = int(testDate.strftime('%Y'))
    if datetime.date(year, month, date) <= datetime.date(2020, 3, 5):
        return '05MAR20'
    if datetime.date(year, month, date) <= datetime.date(2020, 3, 12):
        return '12MAR20'
    if datetime.date(year, month, date) <= datetime.date(2020, 3, 19):
        return '19MAR20'
    if datetime.date(year, month, date) <= datetime.date(2020, 3, 26):
        return '26MAR20'
    if datetime.date(year, month, date) <= datetime.date(2020, 4, 1):
        return '01APR20'
    if datetime.date(year, month, date) <= datetime.date(2020, 4, 9):
        return '09APR20'
    if datetime.date(year, month, date) <= datetime.date(2020, 4, 16):
        return '16APR20'
    if datetime.date(year, month, date) <= datetime.date(2020, 4, 23):
        return '23APR20'
    if datetime.date(year, month, date) <= datetime.date(2020, 4, 30):
        return '30APR20'
    if datetime.date(year, month, date) <= datetime.date(2020, 5, 7):
        return '07MAY20'
    if datetime.date(year, month, date) <= datetime.date(2020, 5, 14):
        return '14MAY20'
    if datetime.date(year, month, date) <= datetime.date(2020, 5, 21):
        return '21MAY20'
    if datetime.date(year, month, date) <= datetime.date(2020, 5, 28):
        return '28MAY20'
    if datetime.date(year, month, date) <= datetime.date(2020, 6, 4):
        return '04JUN20'
    if datetime.date(year, month, date) <= datetime.date(2020, 6,11):
        return '11JUN20'
    if datetime.date(year, month, date) <= datetime.date(2020, 6,18):
        return '18JUN20'
    if datetime.date(year, month, date) <= datetime.date(2020, 6,25):
        return '25JUN20'
    if datetime.date(year, month, date) <= datetime.date(2020, 7,2):
        return '02JUL20'
    if datetime.date(year, month, date) <= datetime.date(2020, 7,9):
        return '09JUL20'
    if datetime.date(year, month, date) <= datetime.date(2020, 7,16):
        return '16JUL20'
    if datetime.date(year, month, date) <= datetime.date(2020, 7,23):
        return '23JUL20'
    if datetime.date(year, month, date) <= datetime.date(2020, 7,30):
        return '30JUL20'
    if datetime.date(year, month, date) <= datetime.date(2020, 8,6):
        return '06AUG20'
    if datetime.date(year, month, date) <= datetime.date(2020,8,13):
        return '13AUG20'
    if datetime.date(year, month, date) <= datetime.date(2020,8,20):
        return '20AUG20'
    if datetime.date(year, month, date) <= datetime.date(2020,8,27):
        return '27AUG20'
    if datetime.date(year, month, date) <= datetime.date(2020,9,3):
        return '03SEP20'
    if datetime.date(year, month, date) <= datetime.date(2020,9,10):
        return '10SEP20'
    if datetime.date(year, month, date) <= datetime.date(2020,9,17):
        return '17SEP20'
    if datetime.date(year, month, date) <= datetime.date(2020,9,24):
        return '24SEP20'
    if datetime.date(year, month, date) <= datetime.date(2020,10,1):
        return '01OCT20'
    if datetime.date(year, month, date) <= datetime.date(2020,10,8):
        return '08OCT20'
    if datetime.date(year, month, date) <= datetime.date(2020,10,15):
        return '15OCT20'
    if datetime.date(year, month, date) <= datetime.date(2020,10,22):
        return '22OCT20'
    if datetime.date(year, month, date) <= datetime.date(2020,10,29):
        return '29OCT20'
    if datetime.date(year, month, date) <= datetime.date(2020,11,5):
        return '05NOV20'
    if datetime.date(year, month, date) <= datetime.date(2020,11,12):
        return '12NOV20'
    if datetime.date(year, month, date) <= datetime.date(2020,11,19):
        return '19NOV20'
    if datetime.date(year, month, date) <= datetime.date(2020,11,26):
        return '26NOV20'
    if datetime.date(year, month, date) <= datetime.date(2020,12,3):
        return '03DEC20'
    if datetime.date(year, month, date) <= datetime.date(2020,12,10):
        return '10DEC20'
    if datetime.date(year, month, date) <= datetime.date(2020,12,17):
        return '17DEC20'
    if datetime.date(year, month, date) <= datetime.date(2020,12,24):
        return '24DEC20'
    if datetime.date(year, month, date) <= datetime.date(2020,12,31):
        return '31DEC20'
    if datetime.date(year, month, date) <= datetime.date(2021,1,7):
        return '07JAN21'
    if datetime.date(year, month, date) <= datetime.date(2021,1,14):
        return '14JAN21'
    if datetime.date(year, month, date) <= datetime.date(2021,1,21):
        return '21JAN21'
    if datetime.date(year, month, date) <= datetime.date(2021,1,28):
        return '28JAN21'
    if datetime.date(year, month, date) <= datetime.date(2021,2,4):
        return '04FEB21'
    if datetime.date(year, month, date) <= datetime.date(2021,2,11):
        return '11FEB21'
    if datetime.date(year, month, date) <= datetime.date(2021,2,18):
        return '18FEB21'
    if datetime.date(year, month, date) <= datetime.date(2021,2,25):
        return '25FEB21'
    if datetime.date(year, month, date) <= datetime.date(2021,3,4):
        return '04MAR21'
    if datetime.date(year, month, date) <= datetime.date(2021,3,10):
        return '10MAR21'
    if datetime.date(year, month, date) <= datetime.date(2021,3,18):
        return '18MAR21'
    if datetime.date(year, month, date) <= datetime.date(2021,3,25):
        return '25MAR21'
    if datetime.date(year, month, date) <= datetime.date(2021,4,1):
        return '01APR21'
    if datetime.date(year, month, date) <= datetime.date(2021,4,8):
        return '08APR21'
    if datetime.date(year, month, date) <= datetime.date(2021,4,15):
        return '15APR21'
    if datetime.date(year, month, date) <= datetime.date(2021,4,22):
        return '22APR21'
    if datetime.date(year, month, date) <= datetime.date(2021,4,29):
        return '29APR21'
    if datetime.date(year, month, date) <= datetime.date(2021,5,6):
        return '06MAY21'
    if datetime.date(year, month, date) <= datetime.date(2021,5,12):
        return '12MAY21'
    if datetime.date(year, month, date) <= datetime.date(2021,5,20):
        return '20MAY21'
    if datetime.date(year, month, date) <= datetime.date(2021,5,27):
        return '27MAY21'
    if datetime.date(year, month, date) <= datetime.date(2021,6,3):
        return '03JUN21'
    if datetime.date(year, month, date) <= datetime.date(2021,6,10):
        return '10JUN21'
    if datetime.date(year, month, date) <= datetime.date(2021,6,17):
        return '17JUN21'
    if datetime.date(year, month, date) <= datetime.date(2021,6,24):
        return '24JUN21'
    if datetime.date(year, month, date) <= datetime.date(2021,7,1):
        return '01JUL21'
    if datetime.date(year, month, date) <= datetime.date(2021,7,8):
        return '08JUL21'
    if datetime.date(year, month, date) <= datetime.date(2021,7,15):
        return '15JUL21'
    if datetime.date(year, month, date) <= datetime.date(2021,7,22):
        return '22JUL21'
    if datetime.date(year, month, date) <= datetime.date(2021,7,29):
        return '29JUL21'
        
    if datetime.date(year, month, date) <= datetime.date(2021,8,5):
        return '05AUG21'
    if datetime.date(year, month, date) <= datetime.date(2021,8,12):
        return '12AUG21'
    if datetime.date(year, month, date) <= datetime.date(2021,8,18):
        return '18AUG21'
    if datetime.date(year, month, date) <= datetime.date(2021,8,26):
        return '26AUG21'

    if datetime.date(year, month, date) <= datetime.date(2021,9,2):
        return '02SEP21'
    
    if datetime.date(year, month, date) <= datetime.date(2021,9,9):
        return '09SEP21'
    
    if datetime.date(year, month, date) <= datetime.date(2021,9,16):
        return '16SEP21'

    if datetime.date(year, month, date) <= datetime.date(2021,9,23):
        return '23SEP21'

    if datetime.date(year, month, date) <= datetime.date(2021,9,30):
        return '30SEP21'

    raise Exception(f'Expiry not found, add data!')

if __name__ == "__main__":
    
    '''Sample code for using the functions'''
    
    conn = MongoClient()

    data = getHistData1Min(datetime.datetime(2021,9,9,9,20,0).timestamp(),
                            'NIFTY 50',conn)

    print(f'Data fetched is {data}')

    dataDF = getBackTestData1Min(datetime.datetime(2021,9,9,9,20,0).timestamp(),
                                datetime.datetime(2021,9,9,15,20,0).timestamp(),
                                'NIFTY 50',conn)
   
    print(f'Data fetched is \n {dataDF.to_string()}')

    '''Get current weekly Expiry for a particular day'''

    print(f'Weekly Option expiry for the day {datetime.datetime(2021,9,9,9,20,0)} is {getCurrentExpiry(datetime.datetime(2021,9,9,9,20,0).timestamp())}')
