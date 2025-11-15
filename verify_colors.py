"""
Verify that competitiveness colors are correctly assigned in fl_elections_aggregated.json
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

def get_expected_category(margin_pct):
    """Determine expected category based on margin percentage"""
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

def verify_json_colors():
    """Verify all color assignments in the JSON"""
    print("=" * 80)
    print("VERIFYING COLOR ASSIGNMENTS IN FL_ELECTIONS_AGGREGATED.JSON")
    print("=" * 80)
    
    with open('data/fl_elections_aggregated.json', 'r') as f:
        data = json.load(f)
    
    total_checked = 0
    errors_found = 0
    
    results_by_year = data.get('results_by_year', {})
    
    for year, year_data in results_by_year.items():
        for office_type, contests in year_data.items():
            for contest_key, contest_data in contests.items():
                contest_name = contest_data.get('contest_name', contest_key)
                results = contest_data.get('results', {})
                
                for county, county_data in results.items():
                    total_checked += 1
                    
                    margin_pct = county_data.get('margin_pct', 0)
                    actual_comp = county_data.get('competitiveness', {})
                    actual_code = actual_comp.get('code', '')
                    actual_color = actual_comp.get('color', '')
                    actual_category = actual_comp.get('category', '')
                    actual_party = actual_comp.get('party', '')
                    
                    # Get expected values
                    expected_code, expected_category, expected_party = get_expected_category(margin_pct)
                    expected_color = COLOR_SCHEME.get(expected_code, '')
                    
                    # Check for mismatches
                    if (actual_code != expected_code or 
                        actual_color != expected_color or
                        actual_category != expected_category or
                        actual_party != expected_party):
                        
                        errors_found += 1
                        print(f"\n❌ ERROR in {year} {contest_name} - {county}")
                        print(f"   Margin: {margin_pct:.2f}%")
                        print(f"   Expected: {expected_code} | {expected_category} {expected_party} | {expected_color}")
                        print(f"   Actual:   {actual_code} | {actual_category} {actual_party} | {actual_color}")
    
    print("\n" + "=" * 80)
    print(f"VERIFICATION COMPLETE")
    print(f"Total records checked: {total_checked}")
    print(f"Errors found: {errors_found}")
    
    if errors_found == 0:
        print("✅ ALL COLOR ASSIGNMENTS ARE CORRECT!")
    else:
        print(f"⚠️  Found {errors_found} incorrect color assignments")
    print("=" * 80)

if __name__ == '__main__':
    verify_json_colors()
