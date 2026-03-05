-- Tasks 19. Rotten tomatoes
-- Script that lists all shows from hbtn_0d_tvshows_rate
-- by their rating
SELECT s.title, SUM(sr.rate) AS rating
FROM tv_shows AS s
JOIN tv_show_ratings AS sr
ON s.id = sr.show_id
GROUP BY title
ORDER BY rating DESC
