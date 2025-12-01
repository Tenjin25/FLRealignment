import pandas as pd
import json
from pathlib import Path
from collections import defaultdict

# Define election files and their years
election_files = {
    '2000': '11072000Election.txt',
    '2002': '11052002Election.txt',
    '2004': '11042004Election.txt',
    '2006': '11052006Election.txt',
    '2008': '11042008Election.txt',
    '2010': '11022010Election.txt',
    '2012': '11062012Election.txt',
    '2014': '11042014Election.txt',
    '2016': '11082016Election.txt',
    '2018': '11062018Election.txt',
    '2020': '11032020Election.txt',
    '2022': '11082022Election.txt',
    '2024': '11052024Election.txt'
}

# Office name mapping for cleaner keys (statewide offices only)
office_mapping = {
    'President of the United States': 'presidential',
    'United States Senator': 'us_senate',
    'Governor': 'governor',
    'Attorney General': 'attorney_general',
    'Chief Financial Officer': 'cfo',
    'Commissioner of Agriculture': 'agriculture_commissioner'
}

# Statewide offices to include (filter out district-level races)
statewide_offices = {
    'President of the United States',
    'United States Senator', 
    'Governor',
    'Attorney General',
    'Chief Financial Officer',
    'Commissioner of Agriculture'
}

# Statewide offices to include (filter out district-level races)
statewide_offices = {
    'President of the United States',
    'United States Senator', 
    'Governor',
    'Attorney General',
    'Chief Financial Officer',
    'Commissioner of Agriculture'
}

# First name lookup for Presidential and Governor candidates
candidate_first_names = {
    # Presidential candidates
    'Obama': 'Barack Obama',
    'McCain': 'John McCain',
    'Romney': 'Mitt Romney',
    'Clinton': 'Hillary Clinton',
    'Trump': 'Donald Trump',
    'Biden': 'Joe Biden',
    'Harris': 'Kamala Harris',
    # Florida Governor candidates
    'Scott': 'Rick Scott',
    'Sink': 'Alex Sink',
    'Crist': 'Charlie Crist',
    'DeSantis': 'Ron DeSantis',
    'Gillum': 'Andrew Gillum',
}

def get_competitiveness(margin_pct, winner):
    """Calculate competitiveness category based on margin"""
    abs_margin = abs(margin_pct)
    
    if abs_margin >= 40:
        category, code = "Annihilation", "ANNIHILATION"
        color = "#67000d" if winner == "REP" else "#08306b"
    elif abs_margin >= 30 and abs_margin <= 39.99:
        category, code = "Dominant", "DOMINANT"
        color = "#a50f15" if winner == "REP" else "#08519c"
    elif abs_margin >= 20 and abs_margin <= 29.99:
        category, code = "Stronghold", "STRONGHOLD"
        color = "#cb181d" if winner == "REP" else "#3182bd"
    elif abs_margin >= 10 and abs_margin <= 19.99:
        category, code = "Safe", "SAFE"
        color = "#ef3b2c" if winner == "REP" else "#6baed6"
    elif abs_margin >= 5.51 and abs_margin <= 9.99:
        category, code = "Likely", "LIKELY"
        color = "#fb6a4a" if winner == "REP" else "#9ecae1"
    elif abs_margin >= 1 and abs_margin <= 5.50:
        category, code = "Lean", "LEAN"
        color = "#fcae91" if winner == "REP" else "#c6dbef"
    elif abs_margin >= 0.51 and abs_margin <= 0.99:
        category, code = "Tilt", "TILT"
        color = "#fee8c8" if winner == "REP" else "#e1f5fe"
    else:
        category, code = "Tossup", "TOSSUP"
        color = "#f7f7f7"
    
    party = "Republican" if winner == "REP" else "Democratic" if winner == "DEM" else "Tossup"
    
    return {
        "category": category,
        "party": party,
        "code": f"{winner}_{code}" if winner in ["REP", "DEM"] else code,
        "color": color
    }

def normalize_office_name(office):
    """Normalize office names for consistent keys"""
    for full_name, short_name in office_mapping.items():
        if full_name.lower() in office.lower():
            return short_name
    return office.lower().replace(' ', '_')

def process_election_file(file_path, year):
    """Process a single election file and aggregate by county (statewide offices only)"""
    df = pd.read_csv(file_path, sep='\t', encoding='latin-1')
    
    # Filter for statewide offices only
    df = df[df['OfficeDesc'].isin(statewide_offices)]
    
    # Group by office and county
    results_by_office = defaultdict(lambda: defaultdict(dict))
    
    for office in df['OfficeDesc'].unique():
        office_df = df[df['OfficeDesc'] == office]
        office_key = normalize_office_name(office)
        
        for county in office_df['CountyName'].unique():
            county_df = office_df[office_df['CountyName'] == county]
            
            # Aggregate votes by party
            party_votes = {}
            candidates = {}
            
            for _, row in county_df.iterrows():
                party = row['PartyCode']
                votes = int(row['CanVotes'])
                # Presidential and Governor races have running mates in the name fields
                # Format varies by year!
                # Other offices: use FirstName LastName
                if 'President' in office:
                    # Presidential: Format changed between years
                    # 2008, 2020, 2024: CanNameFirst has president's last name, CanNameLast has VP
                    # 2012, 2016: CanNameLast has president's last name, CanNameFirst has first/middle name
                    if year in ['2008', '2020', '2024']:
                        last_name = str(row['CanNameFirst']).strip()
                    else:
                        last_name = str(row['CanNameLast']).strip()
                    candidate = candidate_first_names.get(last_name, last_name)
                elif 'Governor' in office:
                    # Governor: Format varies by year
                    # 2010, 2022: CanNameFirst has governor's last name, CanNameLast has Lt. Gov
                    # 2014, 2018: CanNameLast has governor's last name, CanNameFirst has first name
                    if year in ['2010', '2022']:
                        last_name = str(row['CanNameFirst']).strip()
                    else:
                        last_name = str(row['CanNameLast']).strip()
                    candidate = candidate_first_names.get(last_name, last_name)
                else:
                    # Other offices (Senate, AG, CFO, Agriculture): Use FirstName LastName
                    first_name = str(row['CanNameFirst']).strip()
                    last_name = str(row['CanNameLast']).strip()
                    candidate = f"{first_name} {last_name}"
                
                if party in party_votes:
                    party_votes[party] += votes
                else:
                    party_votes[party] = votes
                    
                if party not in candidates:
                    candidates[party] = candidate
            
            # Calculate totals and margins
            dem_votes = party_votes.get('DEM', 0)
            rep_votes = party_votes.get('REP', 0)
            other_votes = sum(v for k, v in party_votes.items() if k not in ['DEM', 'REP'])
            total_votes = sum(party_votes.values())
            two_party_total = dem_votes + rep_votes
            
            if two_party_total > 0:
                margin = rep_votes - dem_votes
                margin_pct = (margin / two_party_total) * 100
                winner = "REP" if margin > 0 else "DEM" if margin < 0 else "TIE"
            else:
                margin = 0
                margin_pct = 0
                winner = "TIE"
            
            # Create contest key
            contest_key = f"{office_key}_{year}"
            
            # Store county results
            county_upper = county.upper()
            results_by_office[office_key][contest_key][county_upper] = {
                "county": county_upper,
                "contest": office,
                "year": year,
                "dem_candidate": candidates.get('DEM', ''),
                "rep_candidate": candidates.get('REP', ''),
                "dem_votes": dem_votes,
                "rep_votes": rep_votes,
                "other_votes": other_votes,
                "total_votes": total_votes,
                "two_party_total": two_party_total,
                "margin": margin,
                "margin_pct": round(margin_pct, 2),
                "winner": winner,
                "competitiveness": get_competitiveness(margin_pct, winner),
                "all_parties": party_votes
            }
    
    return results_by_office

def aggregate_all_elections():
    """Aggregate all election files into a single JSON structure"""
    base_path = Path(r'C:\Users\Shama\OneDrive\Documents\Course_Materials\CPT-236\Side_Projects\FLRealignments\Election_Data')
    
    final_structure = {
        "metadata": {
            "state": "Florida",
            "years": list(election_files.keys()),
            "generated": "2025-11-13",
            "source": "Florida Division of Elections"
        },
        "results_by_year": {}
    }
    
    for year, filename in election_files.items():
        file_path = base_path / filename
        if file_path.exists():
            print(f"Processing {year}...")
            results = process_election_file(file_path, year)
            
            # Organize by year -> office type -> contest -> results
            final_structure["results_by_year"][year] = {}
            
            for office_key, contests in results.items():
                final_structure["results_by_year"][year][office_key] = {}
                
                for contest_key, county_results in contests.items():
                    final_structure["results_by_year"][year][office_key][contest_key] = {
                        "contest_name": list(county_results.values())[0]["contest"],
                        "results": county_results
                    }
            
            print(f"  ✓ Processed {len(results)} office types for {year}")
        else:
            print(f"  ✗ File not found: {filename}")
    
    # Save to JSON
    output_path = base_path.parent / 'data' / 'fl_elections_aggregated.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_structure, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Aggregated data saved to: {output_path}")
    print(f"Total years processed: {len(final_structure['results_by_year'])}")
    
    return final_structure

if __name__ == "__main__":
    result = aggregate_all_elections()
