ALTER TABLE test_data
ADD COLUMN the_geom geometry(POINT, 4326);

UPDATE test_data 
SET the_geom = ST_SetSRID(ST_MakePoint(latitude,longitude), 4326);
