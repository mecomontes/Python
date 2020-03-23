import pandas as pd 
url = pd.read_html('https://www.rexegg.com/regex-quickstart.html')
df = url[0]
df.head(2)
s=[1,1,2,3,4,5,6]
df.iloc[2]
