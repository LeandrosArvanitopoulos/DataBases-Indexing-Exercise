create table airports ( 
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

LOAD DATA INFILE 'airports.csv'
INTO TABLE airports
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

