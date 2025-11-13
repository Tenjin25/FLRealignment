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
    contests = df['ContestName'].unique()
    print(f'\nTotal contests: {len(contests)}')
    
    # Look for congressional contests
    congressional_terms = ['representative', 'house', 'congressional', 'district']
    cong_contests = [c for c in contests if any(term in c.lower() for term in congressional_terms)]
    
    print(f'\nFound {len(cong_contests)} congressional contests:')
    for c in cong_contests[:10]:
        print(f' - {c}')
    
    # Check if we have district numbers
    if cong_contests:
        sample_contest = cong_contests[0]
        sample_data = df[df['ContestName'] == sample_contest].head(3)
        print(f'\nSample data for: {sample_contest}')
        print(sample_data[['CountyName', 'ContestName', 'ChoiceName', 'VoteCount']].to_string())
