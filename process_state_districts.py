import pandas as pd
import geopandas as gpd
import os

def process_state_legislative_districts():
    """Convert state house and senate shapefiles to GeoJSON and CSV"""
    
    # State House Districts
    print("Processing State House Districts...")
    try:
        house_gdf = gpd.read_file('H000H8013/H000H8013.shp')
        
        # Remove duplicate columns
        house_gdf = house_gdf.loc[:, ~house_gdf.columns.duplicated()]
        
        # Save GeoJSON
        house_gdf.to_file('data/fl_state_house_districts.geojson', driver='GeoJSON')
        
        # Extract key data for CSV
        house_data = []
        for _, row in house_gdf.iterrows():
            house_record = {
                'district': int(row['DISTRICT']),
                'longname': row['LONGNAME'],
                'shortname': row['SHORTNAME'], 
                'total_population': int(row['TOTAL']),
                'white_vap_pct': round(float(row['SRWVAP_P']), 2),
                'black_vap_pct': round(float(row['NHBVAP_P']), 2),
                'hispanic_vap_pct': round(float(row['HVAP_P']), 2)
            }
            house_data.append(house_record)
        
        # Save CSV
        house_df = pd.DataFrame(house_data)
        house_df = house_df.sort_values('district')
        house_df.to_csv('data/fl_state_house_districts.csv', index=False)
        print(f"State House: {len(house_df)} districts saved")
        
    except Exception as e:
        print(f"Error processing state house: {e}")
    
    # State Senate Districts  
    print("Processing State Senate Districts...")
    try:
        senate_gdf = gpd.read_file('data/S027S8058/S027S8058.shp')
        
        # Remove duplicate columns
        senate_gdf = senate_gdf.loc[:, ~senate_gdf.columns.duplicated()]
        
        # Save GeoJSON
        senate_gdf.to_file('data/fl_state_senate_districts.geojson', driver='GeoJSON')
        
        # Extract key data for CSV
        senate_data = []
        for _, row in senate_gdf.iterrows():
            senate_record = {
                'district': int(row['DISTRICT']),
                'longname': row['LONGNAME'],
                'shortname': row['SHORTNAME'], 
                'total_population': int(row['TOTAL']),
                'white_vap_pct': round(float(row['SRWVAP_P']), 2),
                'black_vap_pct': round(float(row['NHBVAP_P']), 2),
                'hispanic_vap_pct': round(float(row['HVAP_P']), 2)
            }
            senate_data.append(senate_record)
        
        # Save CSV
        senate_df = pd.DataFrame(senate_data)
        senate_df = senate_df.sort_values('district')
        senate_df.to_csv('data/fl_state_senate_districts.csv', index=False)
        print(f"State Senate: {len(senate_df)} districts saved")
        
    except Exception as e:
        print(f"Error processing state senate: {e}")

if __name__ == "__main__":
    print("Processing Florida State Legislative Districts...")
    process_state_legislative_districts()
    
    print("\nFiles created:")
    print("- data/fl_state_house_districts.geojson")
    print("- data/fl_state_house_districts.csv") 
    print("- data/fl_state_senate_districts.geojson")
    print("- data/fl_state_senate_districts.csv")
