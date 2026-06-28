from src.data.load_data import load_data 


df = load_data(r"data\raw\email_spam_dataset.csv")

print(df.head())
print(df.columns)
print(df["Category"].value_counts())
