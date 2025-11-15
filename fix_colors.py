"""
Fix color assignment errors in fl_elections_aggregated.json
Corrects tossup classifications to remove party labels
"""
import json

# Color scheme from the map
COLOR_SCHEME = {
    'REP_ANNIHILATION': '#67000d',    # R+40%+
    'REP_DOMINANT': '#a50f15',        # R+30-40%
    'REP_STRONGHOLD': '#cb181d',      # R+20-30%
    'REP_SAFE': '#ef3b2c',            # R+10-20%
    'REP_LIKELY': '#fb6a4a',          # R+5.5-10%
    'REP_LEAN': '#fcae91',            # R+1-5.5%
    'REP_TILT': '#fee8c8',            # R+0.5-1%
    'TOSSUP': '#f7f7f7',              # ±0.5%
    'DEM_TILT': '#e1f5fe',            # D+0.5-1%
    'DEM_LEAN': '#c6dbef',            # D+1-5.5%
    'DEM_LIKELY': '#9ecae1',          # D+5.5-10%
    'DEM_SAFE': '#6baed6',            # D+10-20%
    'DEM_STRONGHOLD': '#3182bd',      # D+20-30%
    'DEM_DOMINANT': '#08519c',        # D+30-40%
    'DEM_ANNIHILATION': '#08306b'     # D+40%+
}

def get_correct_category(margin_pct):
    """Determine correct category based on margin percentage"""
    abs_margin = abs(margin_pct)
    
    if margin_pct > 0:  # Republican win
        if abs_margin >= 40:
            return 'REP_ANNIHILATION', 'Annihilation', 'Republican'
        elif abs_margin >= 30:
            return 'REP_DOMINANT', 'Dominant', 'Republican'
        elif abs_margin >= 20:
            return 'REP_STRONGHOLD', 'Stronghold', 'Republican'
        elif abs_margin >= 10:
            return 'REP_SAFE', 'Safe', 'Republican'
        elif abs_margin >= 5.5:
            return 'REP_LIKELY', 'Likely', 'Republican'
        elif abs_margin >= 1:
            return 'REP_LEAN', 'Lean', 'Republican'
        elif abs_margin >= 0.5:
            return 'REP_TILT', 'Tilt', 'Republican'
        else:
            return 'TOSSUP', 'Tossup', 'Tossup'
    else:  # Democratic win
        if abs_margin >= 40:
            return 'DEM_ANNIHILATION', 'Annihilation', 'Democratic'
        elif abs_margin >= 30:
            return 'DEM_DOMINANT', 'Dominant', 'Democratic'
        elif abs_margin >= 20:
            return 'DEM_STRONGHOLD', 'Stronghold', 'Democratic'
        elif abs_margin >= 10:
            return 'DEM_SAFE', 'Safe', 'Democratic'
        elif abs_margin >= 5.5:
            return 'DEM_LIKELY', 'Likely', 'Democratic'
        elif abs_margin >= 1:
            return 'DEM_LEAN', 'Lean', 'Democratic'
        elif abs_margin >= 0.5:
            return 'DEM_TILT', 'Tilt', 'Democratic'
        else:
            return 'TOSSUP', 'Tossup', 'Tossup'

def fix_json_colors():
    """Fix all color assignments in the JSON"""
    print("=" * 80)
    print("FIXING COLOR ASSIGNMENTS IN FL_ELECTIONS_AGGREGATED.JSON")
    print("=" * 80)
    
    with open('data/fl_elections_aggregated.json', 'r') as f:
        data = json.load(f)
    
    fixes_made = 0
    
    results_by_year = data.get('results_by_year', {})
    
    for year, year_data in results_by_year.items():
        for office_type, contests in year_data.items():
            for contest_key, contest_data in contests.items():
                contest_name = contest_data.get('contest_name', contest_key)
                results = contest_data.get('results', {})
                
                for county, county_data in results.items():
                    margin_pct = county_data.get('margin_pct', 0)
                    actual_comp = county_data.get('competitiveness', {})
                    actual_code = actual_comp.get('code', '')
                    actual_color = actual_comp.get('color', '')
                    actual_category = actual_comp.get('category', '')
                    actual_party = actual_comp.get('party', '')
                    
                    # Get correct values
                    correct_code, correct_category, correct_party = get_correct_category(margin_pct)
                    correct_color = COLOR_SCHEME.get(correct_code, '')
                    
                    # Check for mismatches
                    if (actual_code != correct_code or 
                        actual_color != correct_color or
                        actual_category != correct_category or
                        actual_party != correct_party):
                        
                        fixes_made += 1
                        print(f"\n✏️  Fixing {year} {contest_name} - {county}")
                        print(f"   Margin: {margin_pct:.2f}%")
                        print(f"   Before: {actual_code} | {actual_category} {actual_party} | {actual_color}")
                        print(f"   After:  {correct_code} | {correct_category} {correct_party} | {correct_color}")
                        
                        # Apply fix
                        county_data['competitiveness'] = {
                            'category': correct_category,
                            'party': correct_party,
                            'code': correct_code,
                            'color': correct_color
                        }
    
    # Save the fixed JSON
    if fixes_made > 0:
        with open('data/fl_elections_aggregated.json', 'w') as f:
            json.dump(data, f, indent=2)
        
        print("\n" + "=" * 80)
        print(f"✅ FIXES COMPLETE - {fixes_made} records corrected")
        print(f"Updated file: data/fl_elections_aggregated.json")
        print("=" * 80)
    else:
        print("\n" + "=" * 80)
        print("✅ NO FIXES NEEDED - All color assignments are correct!")
        print("=" * 80)

if __name__ == '__main__':
    fix_json_colors()
