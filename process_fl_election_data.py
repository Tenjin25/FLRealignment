#!/usr/bin/env python3
"""
Process Florida election TSV files into JSON format for the political map.
"""

import pandas as pd
import json
import os
from collections import defaultdict

def parse_year_from_filename(filename):
    """Extract year from filename like '11052024Election.txt' -> '2024'"""
    date_part = filename.replace('Election.txt', '')
    return date_part[4:8]

def normalize_county_name(county_name):
    """Normalize county names to match GeoJSON"""
    # Handle common variations
    name = county_name.strip()
    if name == 'Miami-Dade' or name == 'Dade':
        return 'Miami-Dade'
    return name

def process_election_files():
    """Process all election TSV files in Election_Data folder"""
    
    results_by_year = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    
    # Get all election files
    election_files = [f for f in os.listdir('Election_Data') if f.endswith('Election.txt')]
    print(f"Found {len(election_files)} election files")
    
    for filename in election_files:
        year = parse_year_from_filename(filename)
        print(f"Processing {filename} -> {year}")
        
        try:
            # Read TSV file, handling encoding issues
            try:
                df = pd.read_csv(f'Election_Data/{filename}', sep='\t', encoding='utf-8')
            except UnicodeDecodeError:
                try:
                    df = pd.read_csv(f'Election_Data/{filename}', sep='\t', encoding='latin-1')
                except UnicodeDecodeError:
                    df = pd.read_csv(f'Election_Data/{filename}', sep='\t', encoding='cp1252')
            print(f"  Loaded {len(df)} rows")
            
            # Group by race code
            for race_code, race_df in df.groupby('RaceCode'):
                office_desc = race_df['OfficeDesc'].iloc[0]
                contest_key = f"{race_code.lower()}_{year}_1"
                
                print(f"  Processing {race_code}: {office_desc}")
                
                # Aggregate by county (since this is county-level data)
                county_results = {}
                
                for county_code, county_df in race_df.groupby('CountyCode'):
                    county_name = normalize_county_name(county_df['CountyName'].iloc[0])
                    
                    # Create a synthetic precinct ID for this county
                    precinct_id = f"{county_name}_{county_code}_{race_code}"
                    
                    dem_votes = 0
                    rep_votes = 0
                    dem_candidate = ""
                    rep_candidate = ""
                    
                    # Sum votes by party
                    for _, row in county_df.iterrows():
                        if row['PartyCode'] == 'DEM':
                            dem_votes += row['CanVotes']
                            if not dem_candidate:
                                dem_candidate = f"{row['CanNameFirst']} {row['CanNameLast']}"
                        elif row['PartyCode'] == 'REP':
                            rep_votes += row['CanVotes']
                            if not rep_candidate:
                                rep_candidate = f"{row['CanNameFirst']} {row['CanNameLast']}"
                    
                    county_results[precinct_id] = {
                        'precinct': precinct_id,
                        'county': county_name,
                        'dem_votes': dem_votes,
                        'rep_votes': rep_votes,
                        'total_votes': dem_votes + rep_votes,
                        'dem_candidate': dem_candidate,
                        'rep_candidate': rep_candidate
                    }
                
                # Store results
                results_by_year[year][race_code.lower()][contest_key] = {
                    'results': county_results
                }
                
                print(f"    Added {len(county_results)} county results")
        
        except Exception as e:
            print(f"  Error processing {filename}: {e}")
            continue
    
    # Convert to regular dict for JSON serialization
    election_data = {
        'results_by_year': {
            year: {
                contest_type: dict(contests) 
                for contest_type, contests in year_data.items()
            }
            for year, year_data in results_by_year.items()
        }
    }
    
    return election_data

if __name__ == "__main__":
    print("Processing Florida election data...")
    
    # Process the data
    election_data = process_election_files()
    
    # Save to JSON
    output_file = 'data/fl_election.json'
    with open(output_file, 'w') as f:
        json.dump(election_data, f, indent=2)
    
    print(f"\nSaved election data to {output_file}")
    print(f"Years: {list(election_data['results_by_year'].keys())}")
    
    # Print summary
    for year, year_data in election_data['results_by_year'].items():
        print(f"  {year}: {list(year_data.keys())}")
