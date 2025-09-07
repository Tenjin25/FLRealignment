// Loads and parses the candidate CSV, and provides a lookup function for candidate names by contest, year, county, and party.
// This file is loaded before the main map logic in index.html.

window.FL_CANDIDATE_LOOKUP = (function() {
  let candidateMap = {};
  let loaded = false;

  function normalizeCountyCode(code) {
    // Accepts 3-letter county codes, returns uppercase
    return (code || '').toUpperCase();
  }

  function normalizeContestType(type) {
    // Accepts PRE, GOV, etc. Returns uppercase.
    return (type || '').toUpperCase();
  }

  function normalizeParty(party) {
    // Accepts DEM, REP, etc. Returns uppercase.
    return (party || '').toUpperCase();
  }

  function loadCSV(url, callback) {
    Papa.parse(url, {
      download: true,
      header: false,
      skipEmptyLines: true,
      complete: function(results) {
        // CSV columns: contest, year, county_code, party, candidate
        results.data.forEach(row => {
          if (row.length < 5) return;
          const [contest, year, county, party, candidate] = row;
          const key = [normalizeContestType(contest), year, normalizeCountyCode(county), normalizeParty(party)].join('|');
          candidateMap[key] = candidate;
        });
        loaded = true;
        if (callback) callback();
      }
    });
  }

  function getCandidate(contest, year, county, party) {
    const key = [normalizeContestType(contest), String(year), normalizeCountyCode(county), normalizeParty(party)].join('|');
    return candidateMap[key] || null;
  }

  function isLoaded() { return loaded; }

  // Expose API
  return {
    loadCSV,
    getCandidate,
    isLoaded
  };
})();
