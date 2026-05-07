import pandas as pd

df = pd.read_csv("energy_log.csv")

print("Energy Log Data:")
print(df)

print("\nAverage consumption by device:")
print(df.groupby("device")["consumption_watt"].mean())

print("\nTotal consumption by device:")
print(df.groupby("device")["consumption_watt"].sum())

print("\nMost consuming device:")
print(df.groupby("device")["consumption_watt"].sum().idxmax())