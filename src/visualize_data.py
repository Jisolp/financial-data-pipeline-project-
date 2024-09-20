import pandas as pd
import matplotlib.pyplot as plt 
import os

def loadData(filePath):
    if os.path.exists(filePath):
        df = pd.read_csv(filePath, index_col=0, parse_dates= True)
        print(f'data loaded')
        return df
    else:
        return None

def plotTime(df):
    plt.figure(figsize=(10,6))
    plt.plot(df.index, df['1. open'], label='Opening Prices', color = 'green')
    plt.plot(df.index, df['4. close'], label ='Closing Prices',color='yellow')

    plt.title('S&P 500 Opening and Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('USD Prices')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plotPath = os.path.join('visualizations','time_plot.png')
    os.makedirs(os.path.dirname(plotPath),exist_ok= True)
    plt.savefig(plotPath)
    plt.show()
    print('Plot created and saved')

def main():
    processedDataPath = os.path.join('data','processed','processed_sp500_data.csv')
    df = loadData(processedDataPath)

    if df is not None:
        plotTime(df)
if __name__ == '__main__':
    main()