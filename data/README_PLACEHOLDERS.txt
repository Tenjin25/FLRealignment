Place your Florida data files here with these suggested names:

- fl_counties.geojson  -> county boundaries GeoJSON (properties should include County or NAME)
- fl_precincts.geojson -> precinct boundaries (optional)
- fl_election.json     -> comprehensive election JSON matching structure used by the app (see sample_fl_election.json)

If your property names differ, open ultimate_fl_political_map.html and update buildCountyNameMapFromGeoJSON() to pull the correct property (for example: feature.properties.NAME_2).
