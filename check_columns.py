import pandas as pd

# Read the latest election data
encodings = ['utf-8', 'latin-1', 'cp1252']
df = None

for enc in encodings:
    try:
        df = pd.read_csv('Election_Data/11052024Election.txt', sep='\t', encoding=enc, low_memory=False)
        print(f'Successfully read with {enc}')
        break
    except:
        continue

if df is not None:
    print(f'Columns in file: {list(df.columns)}')
    print(f'Shape: {df.shape}')
    print(f'\nFirst few rows:')
    print(df.head(3).to_string())
