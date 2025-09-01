import pandas as pd
import geopandas as gpd
import os
from collections import defaultdict

def process_election_data_to_csv():
    """Process all FL election data and convert to CSV format like NC"""
    
    # Election files
    election_files = [
        'Election_Data/11022010Election.txt',
        'Election_Data/11032020Election.txt', 
        'Election_Data/11042008Election.txt',
        'Election_Data/11042014Election.txt',
        'Election_Data/11052024Election.txt',
        'Election_Data/11062012Election.txt',
        'Election_Data/11062018Election.txt',
        'Election_Data/11082016Election.txt',
        'Election_Data/11082022Election.txt'
    ]
    
    # Year mapping
    year_mapping = {
        '11022010Election.txt': '2010',
        '11032020Election.txt': '2020',
        '11042008Election.txt': '2008', 
        '11042014Election.txt': '2014',
        '11052024Election.txt': '2024',
        '11062012Election.txt': '2012',
        '11062018Election.txt': '2018',
        '11082016Election.txt': '2016',
        '11082022Election.txt': '2022'
    }
    
    # Office code mapping
    office_mapping = {
        'PRE': 'president',
        'USS': 'us_senate', 
        'USR': 'us_house',
        'GOV': 'governor',
        'SEN': 'state_senate',
        'REP': 'state_house'
    }
    
    all_county_data = []
    all_congressional_data = []
    
    for file_path in election_files:
        if not os.path.exists(file_path):
            continue
            
        year = year_mapping[os.path.basename(file_path)]
        print(f"Processing {year}...")
        
        # Try different encodings
        df = None
        for encoding in ['utf-8', 'latin-1', 'cp1252']:
            try:
                df = pd.read_csv(file_path, sep='\t', encoding=encoding, low_memory=False)
                break
            except:
                continue
                
        if df is None:
            print(f"Could not read {file_path}")
            continue
            
        # Process county-level data
        county_results = defaultdict(lambda: defaultdict(lambda: {'dem': 0, 'rep': 0, 'total': 0}))
        
        # Process congressional district data  
        congressional_results = defaultdict(lambda: defaultdict(lambda: {'dem': 0, 'rep': 0, 'total': 0}))
        
        for _, row in df.iterrows():
            county = row['CountyName']
            office_desc = row['OfficeDesc']
            party = row['PartyCode']
            votes = int(row['CanVotes']) if pd.notna(row['CanVotes']) else 0
            
            # Map office types
            office_type = None
            if 'President' in office_desc:
                office_type = 'president'
            elif 'United States Senator' in office_desc:
                office_type = 'us_senate'
            elif 'United States Representative' in office_desc:
                office_type = 'us_house'
                # Also process congressional district data
                district = int(row['Juris1num']) if pd.notna(row['Juris1num']) else None
                if district:
                    if party == 'DEM':
                        congressional_results[district][office_type]['dem'] += votes
                    elif party == 'REP':
                        congressional_results[district][office_type]['rep'] += votes
                    congressional_results[district][office_type]['total'] += votes
            elif 'Governor' in office_desc:
                office_type = 'governor'
            elif 'State Representative' in office_desc:
                office_type = 'state_house'
            elif 'State Senator' in office_desc:
                office_type = 'state_senate'
            
            if office_type:
                # County level aggregation
                if party == 'DEM':
                    county_results[county][office_type]['dem'] += votes
                elif party == 'REP':
                    county_results[county][office_type]['rep'] += votes
                county_results[county][office_type]['total'] += votes
        
        # Convert county results to records
        for county, offices in county_results.items():
            county_record = {
                'year': year,
                'county': county,
                'president_dem': offices['president']['dem'],
                'president_rep': offices['president']['rep'], 
                'president_total': offices['president']['total'],
                'governor_dem': offices['governor']['dem'],
                'governor_rep': offices['governor']['rep'],
                'governor_total': offices['governor']['total'],
                'us_senate_dem': offices['us_senate']['dem'],
                'us_senate_rep': offices['us_senate']['rep'],
                'us_senate_total': offices['us_senate']['total'],
                'us_house_dem': offices['us_house']['dem'],
                'us_house_rep': offices['us_house']['rep'],
                'us_house_total': offices['us_house']['total'],
                'state_senate_dem': offices['state_senate']['dem'],
                'state_senate_rep': offices['state_senate']['rep'],
                'state_senate_total': offices['state_senate']['total'],
                'state_house_dem': offices['state_house']['dem'],
                'state_house_rep': offices['state_house']['rep'],
                'state_house_total': offices['state_house']['total']
            }
            all_county_data.append(county_record)
            
        # Convert congressional results to records
        for district, offices in congressional_results.items():
            cong_record = {
                'year': year,
                'district': district,
                'us_house_dem': offices['us_house']['dem'],
                'us_house_rep': offices['us_house']['rep'],
                'us_house_total': offices['us_house']['total']
            }
            all_congressional_data.append(cong_record)
    
    # Save county data
    county_df = pd.DataFrame(all_county_data)
    county_df.to_csv('data/fl_county_election_results.csv', index=False)
    print(f"Saved county election data: {len(county_df)} records")
    
    # Save congressional data
    if all_congressional_data:
        congressional_df = pd.DataFrame(all_congressional_data)
        congressional_df.to_csv('data/fl_congressional_election_results.csv', index=False)
        print(f"Saved congressional election data: {len(congressional_df)} records")
    
    return county_df, congressional_df if all_congressional_data else None

def process_congressional_districts_to_csv():
    """Convert congressional district shapefile to CSV with basic info"""
    try:
        # Remove duplicate columns and convert to CSV
        gdf = gpd.read_file('data/S035C8060/S035C8060.shp')
        
        # Remove duplicate columns
        gdf = gdf.loc[:, ~gdf.columns.duplicated()]
        
        # Extract key demographic data for CSV
        district_data = []
        for _, row in gdf.iterrows():
            district_record = {
                'district': int(row['DISTRICT']),
                'longname': row['LONGNAME'],
                'shortname': row['SHORTNAME'], 
                'total_population': int(row['TOTAL']),
                'white_vap_pct': round(float(row['SRWVAP_P']), 2),
                'black_vap_pct': round(float(row['NHBVAP_P']), 2),
                'hispanic_vap_pct': round(float(row['HVAP_P']), 2)
            }
            district_data.append(district_record)
        
        # Save district info
        district_df = pd.DataFrame(district_data)
        district_df = district_df.sort_values('district')
        district_df.to_csv('data/fl_congressional_districts.csv', index=False)
        print(f"Saved congressional district data: {len(district_df)} districts")
        
        # Also save the GeoJSON (fix duplicate columns issue)
        gdf.to_file('data/fl_congressional_districts.geojson', driver='GeoJSON')
        print("Saved congressional districts GeoJSON")
        
        return district_df
        
    except Exception as e:
        print(f"Error processing congressional districts: {e}")
        return None

if __name__ == "__main__":
    print("Processing Florida election data to CSV format...")
    
    # Process election data
    county_df, congressional_df = process_election_data_to_csv()
    
    # Process congressional districts
    district_df = process_congressional_districts_to_csv()
    
    print("\nSummary:")
    print(f"County election data: {len(county_df)} records across {county_df['year'].nunique()} years")
    if congressional_df is not None:
        print(f"Congressional election data: {len(congressional_df)} records")
    if district_df is not None:
        print(f"Congressional districts: {len(district_df)} districts")
        
    print("\nFiles created:")
    print("- data/fl_county_election_results.csv")
    print("- data/fl_congressional_election_results.csv") 
    print("- data/fl_congressional_districts.csv")
    print("- data/fl_congressional_districts.geojson")
