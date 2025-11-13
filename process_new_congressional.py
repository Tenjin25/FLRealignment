#!/usr/bin/env python3
"""
Process the new congressional district shapefile (S000C8004) for Florida
Replaces the previous congressional districts with the correct plan
"""

import geopandas as gpd
import pandas as pd
import json
import os

def process_new_congressional_districts():
    """Process the new S000C8004 congressional district shapefile"""
    
    print("🗺️  Processing new congressional districts (S000C8004)...")
    
    # Read the new congressional districts shapefile
    shapefile_path = "./data/S000C8004/S000C8004.shp"
    
    try:
        # Read shapefile - first let's read without geometry to see columns
        temp_df = gpd.read_file(shapefile_path, ignore_geometry=True)
        columns = list(temp_df.columns)
        
        # Handle the duplicate TARGET_DEV columns by dropping one
        if columns.count('TARGET_DEV') > 1:
            print(f"🔧 Found duplicate TARGET_DEV columns, handling...")
            # Read the full shapefile
            gdf = gpd.read_file(shapefile_path)
            # Drop duplicate columns by selecting unique column names
            unique_cols = []
            seen = set()
            for col in gdf.columns:
                if col not in seen or col == 'geometry':
                    unique_cols.append(col)
                    seen.add(col)
                elif col == 'TARGET_DEV' and col in seen:
                    continue  # Skip duplicate TARGET_DEV
            gdf = gdf[unique_cols]
        else:
            gdf = gpd.read_file(shapefile_path)
        
        print(f"✅ Loaded shapefile with {len(gdf)} districts")
        print(f"📊 Columns: {list(gdf.columns)}")
        print(f"🔍 Sample data:\n{gdf.head()}")
        
        # Show coordinate system
        print(f"📍 CRS: {gdf.crs}")
        
        # Convert to WGS84 for web mapping
        if gdf.crs != 'EPSG:4326':
            print("🔄 Converting to WGS84...")
            gdf = gdf.to_crs('EPSG:4326')
        
        # Create output directory if it doesn't exist
        os.makedirs('./data', exist_ok=True)
        
        # Export to GeoJSON (replace existing)
        geojson_path = './data/fl_congressional_districts.geojson'
        gdf.to_file(geojson_path, driver='GeoJSON')
        print(f"✅ Saved GeoJSON: {geojson_path}")
        
        # Create district info CSV
        district_info = []
        for _, row in gdf.iterrows():
            # Extract district info - check what fields are available
            district_data = {
                'district': row.get('DISTRICT', row.get('District', row.get('CD', 'Unknown'))),
                'longname': row.get('LONGNAME', row.get('NAME', f"District {row.get('DISTRICT', 'Unknown')}")),
                'shortname': row.get('SHORTNAME', row.get('SHORT', f"D{row.get('DISTRICT', 'Unknown')}")),
            }
            
            # Add demographic fields if available
            demo_fields = ['TOTAL', 'TOTALPOP', 'TOTAL_POP', 'total_population', 'TOT_POP']
            for field in demo_fields:
                if field in row and pd.notna(row[field]):
                    district_data['total_population'] = int(row[field])
                    break
            else:
                district_data['total_population'] = 769221  # Default FL average
            
            # VAP fields based on the actual columns we saw
            vap_fields = [
                ('white_vap_pct', ['SRWVAP_P', 'WHITE_VAP_PCT', 'WHITEVAP_PCT', 'WHT_VAP_PCT']),
                ('black_vap_pct', ['BVAP_P', 'BLACK_VAP_PCT', 'BLACKVAP_PCT', 'BLK_VAP_PCT']),
                ('hispanic_vap_pct', ['HVAP_P', 'HISPANIC_VAP_PCT', 'HISPVAP_PCT', 'HISP_VAP_PCT'])
            ]
            
            for output_field, possible_fields in vap_fields:
                for field in possible_fields:
                    if field in row and pd.notna(row[field]):
                        district_data[output_field] = round(float(row[field]), 2)
                        break
                else:
                    # Default values if not found
                    district_data[output_field] = 0.0
            
            district_info.append(district_data)
        
        # Create DataFrame and save CSV
        df = pd.DataFrame(district_info)
        csv_path = './data/fl_congressional_districts.csv'
        df.to_csv(csv_path, index=False)
        print(f"✅ Saved district info CSV: {csv_path}")
        print(f"📊 District info preview:\n{df.head()}")
        
        print("\n🎉 New congressional districts processed successfully!")
        print(f"📍 {len(gdf)} districts converted")
        print(f"📁 Files updated:")
        print(f"   - {geojson_path}")
        print(f"   - {csv_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing congressional districts: {e}")
        return False

if __name__ == "__main__":
    process_new_congressional_districts()
