import pandas as pd

#sample data create 
data={
    "name":["ram","sam","none","raja"],
    "age":[25,none,30,22]
}

df=pd.dataframe(data)
print("original data:")
print(df)

df_clean=df.dropna()

print("\ncleaned data:")
print(df_clean)