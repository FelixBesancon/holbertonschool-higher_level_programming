-- Tasks 20. Best genre
-- Script that lists all genres in the database hbtn_0d_tvshows_rate
-- by their rating
SELECT g.name, SUM(sr.rate) AS rating
FROM tv_genres AS g
JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
JOIN tv_show_ratings AS sr
ON sg.show_id = sr.show_id
GROUP BY name
ORDER BY rating DESC;
