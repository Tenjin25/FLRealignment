FL Political Map - Starter (skeleton)

What this is
- A minimal, runnable HTML + tiny sample election JSON that demonstrates how to load county GeoJSON and an election JSON, then color counties by aggregated county results.

Files created
- `ultimate_fl_political_map.html` — main viewer. Update `CONFIG.paths` and `CONFIG.mapboxToken` to point at your real FL files and Mapbox token.
- `data/sample_fl_election.json` — a tiny example showing the expected structure: `results_by_year -> YEAR -> contestType -> contestKey -> { results: { precinctId: { county, dem_votes, rep_votes, total_votes }}}`.
- `data/` — place your FL GeoJSON files here:
    - `fl_counties.geojson` (expected property with county name: `County`, `NAME`, or `name`)
    - `fl_precincts.geojson` (optional)

How to test locally
1. Update `CONFIG.mapboxToken` in `ultimate_fl_political_map.html` with a valid Mapbox token.
2. Replace paths in `CONFIG.paths` to point at your actual FL files if they differ.
3. Start a local HTTP server from the project root (Mapbox fetches need http):

```powershell
# from the project folder
python -m http.server 8000
# open http://localhost:8000/ultimate_fl_political_map.html
```

Next steps I can do for you
- Auto-generate the contest dropdown from your real FL election JSON (I already do this in the skeleton; if your JSON structure differs, paste a sample and I'll adapt).
- Adapt precinct matching logic if your precinct/county field names differ.
- Replace the sample data with your real FL files and test in-browser; I can patch the HTML to point to exact filenames.

Tell me which FL files you have available (county GeoJSON name, precinct GeoJSON name, election JSON path or sample), and I'll wire them in and validate."
