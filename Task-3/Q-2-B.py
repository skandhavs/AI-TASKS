import pandas as pd
df = pd.DataFrame( 
[("33, Mumbai    Maharashtra"), 
("44, Chennai    Tamil Nadu"), 
("40, Vishakapatnam    Telengana"), 
("80, Bangalore    Karnataka")], columns=(['STDCitystate']))
print(df)
print("\nDataframe after splitting the column\n")
df[['STD','Temp']]=df.STDCitystate.str.split(",",expand=True)
df[['City','State']]=df.Temp.str.split("    ",expand=True)
del df['STDCitystate']
del df['Temp']
print(df)