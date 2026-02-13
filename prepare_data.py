import pandas as pd

# Read original data, keeping all values as strings to preserve formatting
df = pd.read_csv('diabetic_data.csv', dtype=str, keep_default_na=False)

# Replace "?" with empty string (SAS interprets empty CSV fields as missing)
df = df.replace('?', '')

# Save cleaned version
df.to_csv('diabetic_data_clean.csv', index=False)

print(f"Cleaned {len(df)} rows. Output: diabetic_data_clean.csv")
