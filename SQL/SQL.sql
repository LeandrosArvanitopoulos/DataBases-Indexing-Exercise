CREATE TABLE IF NOT EXISTS airports ( 
  id TEXT primary key, 
  ident text, 
  type text, 
  name text, 
  latitude_deg NUMERIC, 
  longitude_deg NUMERIC, 
  elevation_ft INT, 
  continent TEXT, 
  iso_country TEXT
);
