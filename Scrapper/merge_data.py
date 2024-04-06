import pandas as pd
import os
path = "D:\Mastercourse\Book Scrapper\Quote_Data"
files = [file for file in os.listdir(path) if not file.startswith('.')] 

all_quotes_data = pd.DataFrame()

for file in files:
    current_data = pd.read_csv(path+"/"+file)
    all_quotes_data = pd.concat([all_quotes_data, current_data])
    
all_quotes_data.to_csv("Popular_Quotes.csv", index=False) 

    