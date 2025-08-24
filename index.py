import pandas as pd

# Load the CSV file from data/5minjan_aug/5min_6aug_23aug.csv
csv_path = 'data/5minjan_aug/5min_6aug_23aug.csv'
df = pd.read_csv(csv_path)
print(df)

print("Hello, World!")