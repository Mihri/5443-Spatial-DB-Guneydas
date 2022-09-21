--query for primary roads
SELECT *,geom::json FROM p_roads
LIMIT 5;

--query for rails
SELECT *,geom::json FROM rails
LIMIT 5;

--query for states
SELECT *,geom::json FROM states
LIMIT 5;

--query for mil
SELECT *,geom::json FROM mil
LIMIT 5;

--query for zone
SELECT *,geom::json FROM zone
LIMIT 5;

--query for airports
SELECT *,geom::json FROM airports
LIMIT 5;
