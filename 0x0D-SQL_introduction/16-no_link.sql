-- List all records of the second_table of the hbtn_0c_0
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
