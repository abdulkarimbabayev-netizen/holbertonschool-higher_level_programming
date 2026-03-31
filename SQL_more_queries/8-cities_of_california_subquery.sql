-- Lists all cities of California from hbtn_0d_usa using a subquery
-- Select cities where state_id matches California's id
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
