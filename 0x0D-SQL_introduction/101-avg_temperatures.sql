-- Import in hbtn_0c_0 database from temoeartures
SELECT city, AVG(value) AS avg_temp GROUP BY city ORDER BY avg_temp DESC;
