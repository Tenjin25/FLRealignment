import json

# Load the election data
with open('data/fl_elections_aggregated.json', 'r') as f:
    data = json.load(f)

def calculate_county_margin(year, county_name):
    """Calculate presidential margin for a specific county and year"""
    try:
        contests = data['results_by_year'][str(year)]
        
        # Find presidential contest
        pres_contest = None
        for contest_key, contest_data in contests.items():
            for sub_key, sub_data in contest_data.items():
                if 'results' in sub_data:
                    pres_contest = sub_data
                    break
            if pres_contest:
                break
        
        if not pres_contest:
            return None
        
        # Find county results
        county_results = None
        for precinct_key, precinct_data in pres_contest['results'].items():
            if precinct_data['county'] == county_name:
                county_results = precinct_data
                break
        
        if not county_results:
            return None
        
        dem_votes = county_results.get('dem_votes', 0)
        rep_votes = county_results.get('rep_votes', 0)
        other_votes = county_results.get('other_votes', 0)
        total_votes = dem_votes + rep_votes + other_votes
        
        if total_votes == 0:
            return None
        
        dem_pct = (dem_votes / total_votes) * 100
        rep_pct = (rep_votes / total_votes) * 100
        margin = rep_pct - dem_pct
        
        return {
            'dem_votes': dem_votes,
            'rep_votes': rep_votes,
            'other_votes': other_votes,
            'total_votes': total_votes,
            'dem_pct': round(dem_pct, 2),
            'rep_pct': round(rep_pct, 2),
            'margin': round(margin, 2)
        }
    except Exception as e:
        print(f"Error calculating {county_name} {year}: {e}")
        return None

# Counties mentioned in research findings
counties_to_verify = [
    'Miami-Dade',
    'Broward',
    'Palm Beach',
    'Hillsborough',
    'Orange',
    'Osceola',
    'Seminole',
    'Polk',
    'Volusia'
]

years = [2020, 2024]

print("=" * 80)
print("COUNTY MARGIN VERIFICATION")
print("=" * 80)

for county in counties_to_verify:
    print(f"\n{county.upper()}")
    print("-" * 80)
    
    results_2020 = calculate_county_margin(2020, county)
    results_2024 = calculate_county_margin(2024, county)
    
    if results_2020:
        if results_2020['margin'] > 0:
            print(f"  2020: R+{results_2020['margin']:.2f}% (Trump {results_2020['rep_pct']:.2f}%, Biden {results_2020['dem_pct']:.2f}%)")
        else:
            print(f"  2020: D+{abs(results_2020['margin']):.2f}% (Biden {results_2020['dem_pct']:.2f}%, Trump {results_2020['rep_pct']:.2f}%)")
    
    if results_2024:
        if results_2024['margin'] > 0:
            print(f"  2024: R+{results_2024['margin']:.2f}% (Trump {results_2024['rep_pct']:.2f}%, Harris {results_2024['dem_pct']:.2f}%)")
        else:
            print(f"  2024: D+{abs(results_2024['margin']):.2f}% (Harris {results_2024['dem_pct']:.2f}%, Trump {results_2024['rep_pct']:.2f}%)")
    
    if results_2020 and results_2024:
        swing = results_2024['margin'] - results_2020['margin']
        print(f"  SWING: {'R' if swing > 0 else 'D'}+{abs(swing):.2f} points")

# Calculate Miami Metro aggregate
print("\n" + "=" * 80)
print("MIAMI METRO AGGREGATE (Miami-Dade + Broward + Palm Beach)")
print("=" * 80)

metro_counties = ['Miami-Dade', 'Broward', 'Palm Beach']

for year in years:
    total_dem = 0
    total_rep = 0
    total_other = 0
    
    for county in metro_counties:
        results = calculate_county_margin(year, county)
        if results:
            total_dem += results['dem_votes']
            total_rep += results['rep_votes']
            total_other += results['other_votes']
    
    total_votes = total_dem + total_rep + total_other
    dem_pct = (total_dem / total_votes) * 100
    rep_pct = (total_rep / total_votes) * 100
    margin = rep_pct - dem_pct
    
    if margin > 0:
        print(f"{year}: R+{margin:.2f}% (Trump {rep_pct:.2f}%, {'Biden' if year == 2020 else 'Harris'} {dem_pct:.2f}%)")
    else:
        print(f"{year}: D+{abs(margin):.2f}% ({'Biden' if year == 2020 else 'Harris'} {dem_pct:.2f}%, Trump {rep_pct:.2f}%)")

print("\n" + "=" * 80)
