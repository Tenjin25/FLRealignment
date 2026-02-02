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

#### County-Level Margin Shifts (2016–2024)

| County        | 2016 Margin (Clinton vs Trump) | 2020 Margin (Biden vs Trump) | 2024 Margin (Harris vs Trump) | Shift      |
|--------------|-------------------------------|-----------------------------|-------------------------------|------------|
| Miami-Dade   | +30.4% (Clinton)              | +7.4% (Biden)               | -11.5% (Trump)                | -41.9 pts  |
| Broward      | +35.2% (Clinton)              | +29.9% (Biden)              | +17.0% (Harris)                | -18.2 pts  |
| Palm Beach   | +27.0% (Clinton)              | +13.9% (Biden)              | +0.8% (Harris)                | -26.2 pts  |
| Hillsborough | +7.1% (Clinton)               | +7.0% (Biden)               | -3.1% (Trump)                 | -10.2 pts  |
| Pinellas     | -1.2% (Trump)                 | +0.2% (Biden)               | -5.3% (Trump)                 | -4.1 pts   |
| Polk         | -14.6% (Trump)                | -14.6% (Trump)              | -20.9% (Trump)                | -6.3 pts   |
| Osceola      | +25.7% (Clinton)              | +20.4% (Biden)              | -1.4% (Trump)                 | -27.1 pts  |
| Orange       | +25.6% (Clinton)              | +23.3% (Biden)              | +13.8% (Harris)               | -11.8 pts  |
| Seminole     | +2.0% (Clinton)               | +2.8% (Biden)               | -3.6% (Trump)                 | -5.6 pts   |
| Volusia      | -13.4% (Trump)                | -14.2% (Trump)              | -22.0% (Trump)                | -8.6 pts   |
| St. Lucie    | -2.5% (Trump)                 | -1.5% (Trump)               | -9.2% (Trump)                 | -6.7 pts   |
| Manatee      | -17.6% (Trump)                | -17.1% (Trump)              | -24.8% (Trump)                | -7.2 pts   |
| Sarasota     | -11.6% (Trump)                | -12.1% (Trump)              | -18.3% (Trump)                | -6.7 pts   |
| Brevard      | -20.6% (Trump)                | -16.6% (Trump)              | -21.0% (Trump)                | -0.4 pts   |
| Lee          | -21.1% (Trump)                | -19.5% (Trump)              | -28.6% (Trump)                | -7.5 pts   |

*Margins are calculated as (Democratic votes − Republican votes) / (Democratic + Republican votes). Positive = Democratic win, Negative = GOP win. Candidate percentages shown for clarity. 2024 assumes Harris as the Democratic nominee for illustration.*

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
- **Historical Trends**: 1978-2024 election data with margin calculations (24 election cycles)
- **Political Classification**: 15-category system with refined thresholds (Tilt 0.51-0.99%, Lean 1-5.5%, Likely 5.51-9.99%)
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
- **Counties**: 2020 Census TIGER/Line shapefiles (tl_2020_12_county20.geojson)
- **Congressional**: S000C8004 redistricting plan
- **State House**: H000H8013 districts  
- **State Senate**: S027S8058 districts

### **Election Data**
- **Source**: Florida Division of Elections
- **Format**: Aggregated JSON with hierarchical structure (fl_elections_aggregated.json)
- **Years**: 1978-2024 (47 years of historical data covering 24 election cycles)
- **Contests**: President (16 elections), Governor (12 elections), US Senate, Attorney General, CFO, Agriculture Commissioner
- **Candidate Names**: Full names with proper formatting and Bush family differentiation (George H.W. Bush, George W. Bush, Jeb Bush)

## 📁 Project Structure

```
FLRealignments/
├── index.html                        # Main interactive map
├── data/                             # Processed data files
│   ├── tl_2020_12_county20.geojson   # 2020 Census county boundaries
│   ├── fl_elections_aggregated.json  # Hierarchical election results
│   ├── fl_congressional_districts.geojson
│   ├── fl_state_house_districts.geojson
│   └── fl_state_senate_districts.geojson
├── Election_Data/                    # Raw election data (TSV)
├── H000H8013/                        # State House shapefiles
├── S027S8058/                        # State Senate shapefiles  
├── S000C8004/                        # Congressional shapefiles
└── scripts/                          # Data processing scripts
    ├── aggregate_fl_elections.py     # Main election data aggregation
    ├── process_fl_data_to_csv.py     # Legacy CSV processor
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
Political margins classified into 15 categories based on party performance:

#### **Republican Categories** (Red Shades)
- **Annihilation** (R+40%+): #67000d - Deepest red
- **Dominant** (R+30-39.99%): #a50f15 - Very dark red
- **Stronghold** (R+20-29.99%): #cb181d - Dark red
- **Safe** (R+10-19.99%): #ef3b2c - Red
- **Likely** (R+5.51-9.99%): #fb6a4a - Light red
- **Lean** (R+1-5.5%): #fcae91 - Very light red
- **Tilt** (R+0.51-0.99%): #fee8c8 - Pale red

#### **Competitive**
- **Tossup** (±0.5%): #f7f7f7 - Light gray

#### **Democratic Categories** (Blue Shades)
- **Tilt** (D+0.51-0.99%): #e1f5fe - Pale blue
- **Lean** (D+1-5.5%): #c6dbef - Very light blue
- **Likely** (D+5.51-9.99%): #9ecae1 - Light blue
- **Safe** (D+10-19.99%): #6baed6 - Blue
- **Stronghold** (D+20-29.99%): #3182bd - Dark blue
- **Dominant** (D+30-39.99%): #08519c - Very dark blue
- **Annihilation** (D+40%+): #08306b - Deepest blue

*Full categorization details available in fl_elections_aggregated.json metadata*

## 📈 Data Processing

The project includes Python scripts for processing raw election data:

```bash
# Aggregate election data with proper candidate name formatting
python aggregate_fl_elections.py

# Legacy: Process election data from TSV to CSV
python process_fl_data_to_csv.py

# Convert shapefiles to web-ready GeoJSON
python process_state_districts.py

# Update congressional districts
python process_new_congressional.py
```

### **Data Pipeline**
1. Raw TSV files from Florida Division of Elections (Election_Data/)
2. Python script aggregates by county with proper candidate name formatting
3. Output: Hierarchical JSON (fl_elections_aggregated.json)
4. Frontend flattens JSON for compatibility with existing visualization code

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
**📧 Contact**: [Shamard415@gmail.com]

## 🆕 Recent Updates (September 23, 2025)

- **Bug Fixes:**
   - Resolved issues with counties not displaying colors and contest selector not loading correctly.

- **Accessibility Improvements:**
   - Improved color contrast and sidebar responsiveness for better accessibility.

- **Documentation Updates:**
   - Enhanced inline code comments and updated guides for easier project onboarding.

- **Data Updates:**
   - Refreshed and expanded election data for accuracy.
   - Successfully implemented manual overrides for candidate names, allowing for more accurate display and corrections.

- **Mobile Responsiveness:**
   - Improved map and sidebar layout for mobile devices.

- **Error Handling:**
   - Added better error messages and fallback logic for missing or incomplete data.

- **Statewide Results Card Overhaul:**
   - The statewide results section now uses a thermometer-style bar (like the Georgia map) to visually show Democratic and Republican percentages and votes.
   - Margin, winner, and competitiveness label are displayed with improved clarity and color logic.

- **Competitiveness Color Logic:**
   - The color for the 'Competitiveness' label in statewide results now matches the county analysis sidebar, ensuring consistent color coding for all categories (e.g., Lean Democratic, Lean Republican).

- **Contest Selector Improvements:**
   - The contest selector dropdown is optimized for performance and displays contests as flat options with clear labels (e.g., 'President (2008)'), making it easier to view all data for a contest at once.
   - Added a loading spinner and placeholder for better user feedback.

- **Sidebar and UI/UX Enhancements:**
   - Floating sidebar button added for minimized mode.
   - Sidebar minimized ruleset confirmed and improved for better responsiveness.

- **County Name Normalization and Color Logic:**
   - Robust normalization for county names ensures correct color mapping, fixing issues for counties like St Johns and St Lucie.
   - Map coloring logic refactored for accuracy and consistency.

## 🆕 Recent Updates (September 24, 2025)

- **Contest Controls UX & Accessibility:**
   - Contest controls panel now uses a floating toggle button on mobile, keeping desktop layout unchanged.
   - Contest selector dropdown and accessibility (♿) button are grouped for better visibility and context.
   - Accessibility button toggles color blindness mode and is placed next to the contest dropdown for easy access.
   - Improved mobile experience: contest controls are hidden by default and can be opened with the toggle button.

## ♿ Accessibility: Color Blindness Mode

This app includes a color blindness accessibility mode to help users with color vision deficiencies distinguish map and legend colors more easily.

- To activate, click the ♿ button next to the "Contest Type" dropdown in the contest controls panel.
- The mode updates legend colors and styles for high contrast and clarity.
- You can toggle the mode on/off at any time.

This feature is available on both desktop and mobile layouts.

- **Performance Optimizations:**
   - Contest selector population logic profiled and optimized to reduce delay.
   - Efficient dropdown population using document fragments and precomputed contest/year pairs.

**📅 Last Updated**: November 13, 2025

## 🆕 Recent Updates (November 13, 2025)

- **Data Format Improvements:**
   - Fixed year-specific candidate name extraction for inconsistent data formats
   - Presidential: 2008, 2020, 2024 use CanNameFirst; 2012, 2016 use CanNameLast
   - Governor: 2010, 2022 use CanNameFirst; 2014, 2018 use CanNameLast
   - All years now display correct candidate names (not running mates)

- **County Name Normalization:**
   - Fixed all normalization functions to preserve hyphens (Miami-Dade)
   - Fixed all normalization functions to preserve periods (St. Lucie, St. Johns)
   - Updated 8 different normalization functions across the codebase
   - County data now displays correctly for all counties including Miami-Dade
   - Switched to 2020 Census TIGER/Line shapefile (tl_2020_12_county20.geojson) for county boundaries
   - New GeoJSON includes NAME20 and NAMELSAD20 fields for proper county name handling

- **County Label Improvements:**
   - County labels now prioritize NAME20 field from 2020 Census data
   - Added explicit visibility settings to ensure labels display by default
   - Labels display correctly on map load

- **County Search Functionality:**
   - Completely reimplemented with NC Map logic for robustness
   - Uses NAME20 field for clean county names (without "County" suffix)
   - Custom dropdown with dynamic filtering (limits to 10 results)
   - Supports exact and partial matches (e.g., "Miami" finds "Miami-Dade")
   - Visual feedback: green border flash on selection
   - Uses turf.bbox for proper county boundary calculation
   - Includes diagnostic logging for troubleshooting
   - Fixed timing issue by calling setupCountySearch() after counties load
   - Search bar now fully functional with proper zoom and details display

- **Third Party Vote Display:**
   - Statewide temperature bar now shows three segments when third parties exist
   - Democratic (blue) / Republican (red) / Other (gray #6b7280)
   - Breakdown row displays D/R/Other vote counts and percentages
   - Conditional display: two segments when no third party votes
   - Statewide totals now include all parties, not just DEM+REP
   - Fixed percentages to match Wikipedia and official results

- **Contest Dropdown Organization:**
   - Added optgroup organization by office type
   - Groups: Presidential, US Senate, Governor, Attorney General, CFO, Agriculture Commissioner
   - Reordered to show federal offices (President, US Senate) before state offices
   - Easier navigation with clear category headers

- **Data Verification:**
   - Confirmed aggregated results match raw election data perfectly
   - Verified: 2024 Presidential Alachua (Trump 52,939 / Harris 81,578)
   - Verified: 2022 Governor Miami-Dade (DeSantis 393,532 / Crist 312,972)
   - Verified: 2024 Presidential statewide (Trump 6,110,125 / Harris 4,683,038 / Total 10,893,752)

- **Bug Fixes:**
   - Fixed leftover County field references in zoomToCounty function
   - Fixed sidebar going blank when no contest selected
   - Fixed Miami-Dade not showing colors on map
   - Fixed 2022 governor showing incorrect candidates (was Nuñez/Hernandez, now DeSantis/Crist)
   - Fixed 2020 and 2024 presidential showing VP names instead of presidential candidates
   - Fixed search bar not working by storing counties globally (window.countiesData)
   - Fixed search initialization timing issue

**📅 Last Updated**: November 13, 2025

## 🆕 Recent Updates (November 30, 2025)

- **Historical Data Expansion:**
   - Integrated 24 years of Florida election data (1978-2024)
   - Added 16 presidential elections from 1980-2024
   - Added 12 gubernatorial elections from 1978-2022
   - Comprehensive coverage of statewide races across nearly five decades

- **Candidate Name Accuracy:**
   - Fixed presidential candidate extraction for varying data formats across years
   - Implemented Bush family differentiation logic:
     - George H.W. Bush (1988, 1992 presidential)
     - George W. Bush (2000, 2004 presidential)
     - Jeb Bush (1994, 1998 gubernatorial)
   - Year-specific extraction patterns for different field formats (CanNameFirst vs CanNameLast)
   - Fixed gubernatorial races showing lieutenant governor names instead of governor names

- **Competitiveness Threshold Refinements:**
   - Updated margin thresholds for cleaner breakpoints:
     - Tilt: 0.51-0.99% (was 0.5-1%)
     - Lean: 1-5.5% (was 1-5.5%)
     - Likely: 5.51-9.99% (was 5.5-10%)
     - Safe: 10-19.99% (was 10-20%)
     - Stronghold: 20-29.99% (was 20-30%)
     - Dominant: 30-39.99% (was 30-40%)
   - Changed threshold logic from >= to > for 0.99% and 5.5% boundaries to handle rounding edge cases
   - Fixed Jefferson County 2018 Senate displaying as Tossup instead of Lean R (actual margin: 0.9966%)
   - Updated legend labels to use .99 endings for consistency

- **UI/UX Improvements:**
   - Fixed sidebar toggle button not responding to clicks by consolidating duplicate event handlers
   - Resolved CSS conflict with duplicate .sidebar style blocks preventing proper positioning
   - Fixed pointer-events issue preventing clicks on minimized sidebar button
   - Sidebar toggle now works correctly to expand/minimize County Analysis panel
   - Float button now always visible and changes text between + and −
   - Restored research findings to original font size (14-17px) with bullet points and red shading
   - County sidebar set to display by default for immediate information access
   - Updated Lean category label to 1-5.50% for consistency with other .99/.50 endings

- **Data Processing Enhancements:**
   - Updated aggregate_fl_elections.py to handle 24 election files (1978-2024)
   - Added historical Florida Cabinet positions: Secretary of State, Treasurer, Commissioner of Education, Comptroller (1978-2002)
   - Added office mapping for "President and Vice President of the United States"
   - Added office mapping for "Governor and Lieutenant Governor"
   - Implemented year-based candidate extraction logic for different data format variations
   - Enhanced candidate lookup dictionary with historical figures (Carter, Reagan, Mondale, Dukakis, etc.)
   - Fixed Dade → Miami-Dade county name normalization for 1996 election data
   - Fixed competitiveness thresholds: changed from >= 1 to >= 1.0 so 0.99% margins correctly categorize as "Tilt" instead of "Lean"

- **Map Interface Improvements:**
   - Added county label toggle button (Aa) to show/hide county names on map
   - Button dims when labels are hidden, full opacity when visible
   - Historical Cabinet offices now appear in dropdown with (Historic: 1978-2002) labels
   - Updated all competitiveness logic to use corrected 1.0% threshold

**📅 Last Updated**: February 1, 2026
