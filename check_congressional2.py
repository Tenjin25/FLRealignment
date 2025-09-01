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
    # Get unique office descriptions
    offices = df['OfficeDesc'].unique()
    print(f'All offices ({len(offices)}):')
    for office in sorted(offices):
        print(f' - {office}')
    
    # Look for congressional races
    congressional_offices = [office for office in offices if any(term in office.lower() for term in ['representative', 'house', 'congress', 'district'])]
    
    print(f'\nCongressional offices found: {len(congressional_offices)}')
    for office in congressional_offices:
        print(f' - {office}')
        
    # If we found congressional races, check if they have district info
    if congressional_offices:
        cong_office = congressional_offices[0]
        cong_data = df[df['OfficeDesc'] == cong_office]
        print(f'\nSample data for {cong_office}:')
        print(cong_data[['CountyName', 'OfficeDesc', 'Juris1num', 'Juris2num', 'CanNameLast', 'CanVotes']].head(5).to_string())
