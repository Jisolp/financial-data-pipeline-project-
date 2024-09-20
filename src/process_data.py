import pandas as pd
import os 

def loadData(filePath):
    return pd.read_csv(filePath, index_col= 0, parse_dates = True)

def cleanData(df):
    df = df.dropna()
    return df

def processData(df):
    return df[df.index >= pd.Timestamp.today() - pd.DateOffset(months=6)]

def saveData(df, outputPath):
    df.to_csv(outputPath)
    print("processed data saved")

def main():
    rawDataPath = os.path.join('data','raw','sp500_data.csv')
    processedDataPath = os.path.join('data','processed','processed_sp500_data.csv')

    #make sure the dir exists 
    os.makedirs(os.path.dirname(processedDataPath),exist_ok=True)

    df = loadData(rawDataPath)
    df = cleanData(df)
    df = processData(df)
    saveData(df,processedDataPath)

if __name__ == '__main__':
    main()