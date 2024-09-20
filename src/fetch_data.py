import requests
import pandas as pd
import os

def fetchData(apiKey, symbol ='SPY', function= 'TIME_SERIES_DAILY'):
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={apiKey}'

    try: 
        response = requests.get(url)
        data = response.json()

        if 'Time Series (Daily)' in data:
             df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
             df = df.apply(pd.to_numeric)  
             df.index = pd.to_datetime(df.index)

             #check
             os.makedirs(os.path.join('data','raw'),exist_ok= True)

             df.to_csv(os.path.join('data', 'raw', 'sp500_data.csv'))
             #print(df.head())
             print('Data fetched and saved')
        else:
            print('error fetching data:', data.get('Error Message'))        
    except requests.RequestException as e:
        print(f'reqeust error: {e}')
    except Exception as e:
        print(f'error: {e}')

def main():
    API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')  
    if not API_KEY:
        print('API key is not set')
        return 
    fetchData(API_KEY)

if __name__ == '__main__':
    main()