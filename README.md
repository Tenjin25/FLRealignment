

# Florida Political Realignment Map: A Case Study

## Florida’s Political Realignment: Case Study Overview

### 1. Historical Battleground Status
Florida was the nation’s ultimate swing state from 2008–2016, with razor-thin margins and intense competition.

### 2. The DeSantis Factor (2018 and Beyond)
- **2018 Governor Election:** Ron DeSantis narrowly defeats Andrew Gillum, setting the stage for dramatic change.
- **COVID Response:** DeSantis emphasizes personal freedom, rapid reopening, and opposes extended lockdowns.
- **Policy Impact:** Conservative policies on education, public health, and business regulation attract national attention and migration.
- **2022 Landslide & Supermajority:** DeSantis wins re-election by a landslide; Republicans gain and maintain a legislative supermajority through 2024.

### 3. Population & Migration Shifts
- **Lockdown State Refugees:** Florida’s population surges as residents from states like California and New York move for more freedom and opportunity.
- **Migration Impact:** Influx of conservative-leaning migrants accelerates the shift.

### 4. Key Trends & Insights
- **Presidential Margin Surge:** Florida shifts from 1–2 point margins to a 13-point GOP win in 2024 (Trump: +3 in 2020, +13 in 2024).
- **Voter Registration:** Republicans overtake Democrats for the first time.
- **County-Level Shifts:** Miami-Dade, Palm Beach, and other counties see dramatic margin changes and flips.
- **Hispanic/Latino Realignment:** Cuban, Venezuelan, and Puerto Rican communities move right.
- **National Implications:** Florida’s transformation changes presidential campaign strategies and party priorities.

### 5. Presidential Election Margins in Florida (2008–2024)

| Year | Republican Candidate | Democratic Candidate | GOP Margin |
|------|---------------------|---------------------|------------|
| 2008 | John McCain         | Barack Obama        | -2.8%      |
| 2012 | Mitt Romney         | Barack Obama        | -0.9%      |
| 2016 | Donald Trump        | Hillary Clinton     | +1.2%      |
| 2020 | Donald Trump        | Joe Biden           | +3.4%      |
| 2024 | Donald Trump        | (Dem. Nominee)      | +13%       |

*Negative margin indicates Democratic win. 2024 margin is illustrative for case study purposes.*

This map visualizes the data behind this transformation, allowing users to explore county, congressional, and legislative trends in detail.

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
   open index.html
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
├── index.html                        # Main interactive map
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

**🔗 Live Demo**: https://tenjin25.github.io/FLRealignment/
**📧 Contact**: [Your contact information]
**📅 Last Updated**: September 2025
