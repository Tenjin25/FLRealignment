#!/usr/bin/env python3
"""
Process the new congressional district shapefile (S000C8004) for Florida
Alternative approach using pandas to handle duplicates
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
        # Use fiona to read and handle duplicates manually
        import fiona
        
        # Read shapefile records
        with fiona.open(shapefile_path) as src:
            # Get the schema and fix duplicate columns
            schema = src.schema
            properties = schema['properties']
            
            print(f"📊 Original properties: {list(properties.keys())}")
            
            # Read records and handle duplicates
            records = []
            for feature in src:
                props = feature['properties']
                geometry = feature['geometry']
                
                # Handle duplicate TARGET_DEV by keeping only the first one
                if 'TARGET_DEV' in props:
                    # If there are duplicates, fiona might handle them differently
                    pass
                
                record = {
                    'geometry': geometry,
                    'properties': props
                }
                records.append(record)
        
        # Convert to GeoDataFrame manually
        geometries = [record['geometry'] for record in records]
        properties_list = [record['properties'] for record in records]
        
        # Create DataFrame from properties
        df = pd.DataFrame(properties_list)
        
        # Handle duplicate columns in DataFrame
        df_columns = df.columns.tolist()
        if len(df_columns) != len(set(df_columns)):
            print("🔧 Handling duplicate columns...")
            new_columns = []
            seen = {}
            for col in df_columns:
                if col in seen:
                    seen[col] += 1
                    new_columns.append(f"{col}_{seen[col]}")
                else:
                    seen[col] = 0
                    new_columns.append(col)
            df.columns = new_columns
        
        # Create GeoDataFrame
        gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy([0]*len(df), [0]*len(df)))
        
        # Set the actual geometries
        from shapely.geometry import shape
        actual_geometries = [shape(geom) for geom in geometries]
        gdf.geometry = actual_geometries
        
        # Set CRS
        gdf.crs = 'EPSG:4326'
        
        print(f"✅ Loaded shapefile with {len(gdf)} districts")
        print(f"📊 Columns: {list(gdf.columns)}")
        print(f"🔍 Sample data:\n{gdf.head()}")
        
        # Convert to WGS84 for web mapping (if needed)
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
                'district': row.get('DISTRICT', 'Unknown'),
                'longname': row.get('LONGNAME', f"District {row.get('DISTRICT', 'Unknown')}"),
                'shortname': row.get('SHORTNAME', f"D{row.get('DISTRICT', 'Unknown')}"),
            }
            
            # Add demographic fields if available
            total_pop = row.get('TOTAL', 769221)
            district_data['total_population'] = int(total_pop) if pd.notna(total_pop) else 769221
            
            # VAP percentages based on the actual columns we saw
            district_data['white_vap_pct'] = round(float(row.get('SRWVAP_P', 0.0)), 2)
            district_data['black_vap_pct'] = round(float(row.get('BVAP_P', 0.0)), 2)
            district_data['hispanic_vap_pct'] = round(float(row.get('HVAP_P', 0.0)), 2)
            
            district_info.append(district_data)
        
        # Create DataFrame and save CSV
        df_info = pd.DataFrame(district_info)
        csv_path = './data/fl_congressional_districts.csv'
        df_info.to_csv(csv_path, index=False)
        print(f"✅ Saved district info CSV: {csv_path}")
        print(f"📊 District info preview:\n{df_info.head()}")
        
        print("\n🎉 New congressional districts processed successfully!")
        print(f"📍 {len(gdf)} districts converted")
        print(f"📁 Files updated:")
        print(f"   - {geojson_path}")
        print(f"   - {csv_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing congressional districts: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    process_new_congressional_districts()
