# Florida Political Realignment Map

An interactive web-based political analysis tool for Florida, visualizing election data across counties, congressional districts, state house, and state senate districts from 2008-2024.

![Florida Political Map](https://img.shields.io/badge/Status-Active-brightgreen) ![Data Years](https://img.shields.io/badge/Data-2008--2024-blue) ![Districts](https://img.shields.io/badge/Districts-4%20Types-orange)

## 🗺️ Features

### **4-Way District Visualization**
- **Counties** (67 total) - Presidential and statewide races
- **Congressional Districts** (28 total) - US House races  
- **State House Districts** (120 total) - State legislative races
- **State Senate Districts** (40 total) - State legislative races

### **Interactive Analysis**
- **Hybrid Interaction**: Hover for quick info, click for detailed analysis
- **Historical Trends**: 2008-2024 election data with margin calculations
- **Political Classification**: 15-category system (Safe R to Safe D)
- **Dynamic Tooltips**: Real-time data display with trend analysis

### **Advanced Features**
- **Mapbox GL JS** integration for smooth performance
- **Responsive design** with collapsible sidebar
- **Contest selection** dropdown for different election types
- **Color-coded visualization** based on political margins

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone [your-repo-url]
   cd FLRealignments
   ```

2. **Open the map**
   ```bash
   # Simply open in your browser
   open ultimate_fl_political_map.html
   ```

3. **Explore the data**
   - Use the 4-way toggle (Counties/Congress/State House/State Senate)
   - Select contests from the dropdown
   - Hover for quick info, click for detailed trends

## 📊 Data Sources

### **Geographic Data**
- **Counties**: Florida Department of Transportation (FDOT)
- **Congressional**: S000C8004 redistricting plan
- **State House**: H000H8013 districts  
- **State Senate**: S027S8058 districts

### **Election Data**
- **Source**: Florida Division of Elections
- **Years**: 2008, 2012, 2016, 2020, 2024 (Presidential)
- **Years**: 2010, 2014, 2018, 2022 (Midterm)
- **Contests**: President, Governor, US House, State Legislature

## 📁 Project Structure

```
FLRealignments/
├── ultimate_fl_political_map.html    # Main interactive map
├── data/                             # Processed data files
│   ├── fl_county_election_results.csv
│   ├── fl_congressional_election_results.csv
│   ├── fl_congressional_districts.geojson
│   ├── fl_state_house_districts.geojson
│   └── fl_state_senate_districts.geojson
├── Election_Data/                    # Raw election data (TSV)
├── H000H8013/                        # State House shapefiles
├── S027S8058/                        # State Senate shapefiles  
├── S000C8004/                        # Congressional shapefiles
└── scripts/                          # Data processing scripts
    ├── process_fl_data_to_csv.py
    ├── process_new_congressional.py
    └── process_state_districts.py
```

## 🛠️ Technical Details

### **Technology Stack**
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Mapping**: Mapbox GL JS v3.0.1
- **Data Processing**: Python with geopandas, pandas
- **Data Formats**: GeoJSON, CSV, TSV

### **Performance Optimizations**
- **Hybrid interaction system** (hover + click)
- **Efficient data loading** with CSV format
- **Mapbox vector rendering** for smooth zooming
- **Responsive design** for multiple screen sizes

### **Classification System**
Political margins classified into 15 categories:
- **Republican**: Annihilation (40%+) → Likely (5.5-10%)
- **Competitive**: Tilt R (1-5.5%) → Tilt D (1-5.5%)  
- **Democratic**: Likely (5.5-10%) → Annihilation (40%+)

## 📈 Data Processing

The project includes Python scripts for processing raw election data:

```bash
# Process election data from TSV to CSV
python process_fl_data_to_csv.py

# Convert shapefiles to web-ready GeoJSON
python process_state_districts.py

# Update congressional districts
python process_new_congressional.py
```

## 🎯 Use Cases

- **Political Analysis**: Examine voting patterns and trends
- **Research**: Academic study of Florida political geography  
- **Redistricting**: Analyze district competitiveness
- **Campaign Planning**: Identify target areas and swing regions
- **Education**: Teach political geography and data visualization

## 📱 Browser Compatibility

- ✅ Chrome 80+
- ✅ Firefox 75+  
- ✅ Safari 13+
- ✅ Edge 80+

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Florida Division of Elections for election data
- Florida Department of Transportation for geographic boundaries
- Mapbox for mapping technology
- Open source contributors and data providers

---

**Live Demo**: [Add your GitHub Pages URL here]
**Contact**: [Your contact information]
**Last Updated**: September 2025
