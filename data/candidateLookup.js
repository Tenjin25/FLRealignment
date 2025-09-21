// candidateLookup.js
//
// To use in your GitHub repo:
// 1. Commit this file to your repository.
// 2. Make sure your main HTML file includes:
//    <script src="candidateLookup.js"></script>
// 3. Push your changes to GitHub.
// Your deployed site will automatically use the updated candidate names.
const candidateLookup = {
  // Attorney General (selected years)
  "2010|Attorney General|Democrat": "Dan Gelber",
  "2010|Attorney General|No Party Affiliation": "Jim Lewis",
  "2010|Attorney General|Republican": "Pam Bondi",
  "2014|Attorney General|Democrat": "George Sheldon",
  "2014|Attorney General|Libertarian Party of Florida": "Bill Wohlsifer",
  "2014|Attorney General|Republican": "Pam Bondi",
  "2018|Attorney General|Democrat": "Sean Shaw",
  "2018|Attorney General|No Party Affiliation": "Jeffrey Marc Siskind",
  "2018|Attorney General|Republican": "Ashley Moody",
  "2022|Attorney General|Democrat": "Aramis Ayala",
  "2022|Attorney General|Republican": "Ashley Moody",
  // Chief Financial Officer (CFO)
  "2010|Chief Financial Officer|Democrat": "Loranne Ausley",
  "2010|Chief Financial Officer|No Party Affiliation": "Ken Mazzie",
  "2010|Chief Financial Officer|Republican": "Jeff Atwater",
  "2014|Chief Financial Officer|Democrat": "William 'Will' Rankin",
  "2014|Chief Financial Officer|Republican": "Jeff Atwater",
  "2018|Chief Financial Officer|Democrat": "Jeremy Ring",
  "2018|Chief Financial Officer|Republican": "Jimmy Patronis",
  "2018|Chief Financial Officer|Write-In": "Richard Paul Dembinsky",
  "2022|Chief Financial Officer|Democrat": "Adam Hattersley",
  "2022|Chief Financial Officer|Republican": "Jimmy Patronis",
  // Commissioner of Agriculture
  "2010|Commissioner of Agriculture|Democrat": "Scott Maddox",
  "2010|Commissioner of Agriculture|No Party Affiliation": "Thad Hamilton",
  "2010|Commissioner of Agriculture|Republican": "Adam H. Putnam",
  "2010|Commissioner of Agriculture|Tea Party": "Ira Chester",
  "2014|Commissioner of Agriculture|Democrat": "Thaddeus Thad Hamilton",
  "2014|Commissioner of Agriculture|Republican": "Adam Putnam",
  "2014|Commissioner of Agriculture|Write-In": "Jeffrey M. Obos",
  "2018|Commissioner of Agriculture|Democrat": "Nicole 'Nikki' Fried",
  "2018|Commissioner of Agriculture|Republican": "Matt Caldwell",
  "2022|Commissioner of Agriculture|Democrat": "Naomi Esther Blemur",
  "2022|Commissioner of Agriculture|Republican": "Wilton Simpson",
  "2008|President of the United States|Democrat": " Barack Obama / Joe Biden",
  "2008|President of the United States|Republican": "John McCain / Sarah Palin",
  "2010|Governor|Democrat": "Alex Sink / Rod Smith",
  "2010|Governor|Republican": "Rick Scott / Jennifer Carroll",
  "2012|President of the United States|Democrat": "Barack Obama",
  "2012|President of the United States|Republican": "Mitt Romney",
  "2016|President of the United States|Democrat": "Hillary Rodham Clinton",
  "2016|President of the United States|Republican": "Donald J. Trump",
  "2018|Governor|Democrat": "Andrew Gillum",
  "2018|Governor|Republican": "Ron DeSantis",
  "2020|President of the United States|Democrat": "Joe Biden / Kamala Harris",
  "2020|President of the United States|Republican": "Trump / Pence",
  "2022|Governor|Democrat": "Charlie Crist / Karla Hernández",
  "2022|Governor|Republican": "Ron DeSantis / Jeanette Nuñez",
  "2024|President of the United States|Democrat": "Kamala Harris / Tim Walz",
  "2024|President of the United States|Republican": "Donald J. Trump / JD Vance"
  // ...add more as needed from candidate_lookup.csv
  // 2014 Governor
  ,"2014|Governor|Democrat": "Charlie Crist"
  ,"2014|Governor|Libertarian Party of Florida": "Adrian Wyllie"
  ,"2014|Governor|No Party Affiliation": "Farid Khavari"
  ,"2014|Governor|Republican": "Rick Scott"
  ,"2014|Governor|Write-In": "Piotr Blass"
  // US Senate (all years)
  ,"2010|United States Senator|Democrat": "Kendrick B. Meek"
  ,"2010|United States Senator|Republican": "Marco Rubio"
  ,"2010|United States Senator|Constitution Party of Florida": "Bernie DeCastro"
  ,"2010|United States Senator|Libertarian": "Alexander Andrew Snitker"
  ,"2010|United States Senator|No Party Affiliation": "Sue Askeland"
  ,"2010|United States Senator|Write-In": "Piotr Blass"
  ,"2012|United States Senator|Democrat": "Bill Nelson"
  ,"2012|United States Senator|Republican": "Connie Mack"
  ,"2012|United States Senator|No Party Affiliation": "Bill Gaylor"
  ,"2012|United States Senator|Write-In": "Piotr Blass"
  ,"2016|United States Senator|Democrat": "Patrick Murphy"
  ,"2016|United States Senator|Republican": "Marco Rubio"
  ,"2016|United States Senator|Libertarian Party of Florida": "Paul Stanton"
  ,"2016|United States Senator|No Party Affiliation": "Tony Khoury"
  ,"2016|United States Senator|Write-In": "Robert Samuel Kaplan"
  ,"2018|United States Senator|Democrat": "Bill Nelson"
  ,"2018|United States Senator|Republican": "Rick Scott"
  ,"2018|United States Senator|Write-In": "Lateresa L.A. Jones"
  ,"2022|United States Senator|Democrat": "Val Demings"
  ,"2022|United States Senator|Republican": "Marco Rubio"
  ,"2022|United States Senator|Libertarian Party of Florida": "Dennis Misigoy"
  ,"2022|United States Senator|No Party Affiliation": "Steven B. Grant"
  ,"2022|United States Senator|Write-In": "Uloma Uma Ekpete"
  ,"2024|United States Senator|Democrat": "Debbie Mucarsel-Powell"
  ,"2024|United States Senator|Republican": "Rick Scott"
  ,"2024|United States Senator|Libertarian Party of Florida": "Feena Bonoan"
  ,"2024|United States Senator|No Party Affiliation": "Tuan TQ Nguyen"
  ,"2024|United States Senator|Write-In": "Howard Knepper"
};
