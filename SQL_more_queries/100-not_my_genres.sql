-- Tasks 17. Not my genre
-- Script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres AS g
WHERE g.id NOT IN (
    SELECT sg.genre_id
    FROM tv_show_genres AS sg
    JOIN tv_shows AS t
    ON sg.show_id = t.id
    WHERE t.title = 'Dexter'
)
GROUP BY name
ORDER BY name;
