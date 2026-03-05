-- Tasks 18. No Comedy tonight!
-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT s.title
FROM tv_shows AS s
WHERE s.id NOT IN (
    SELECT sg.show_id
    FROM tv_show_genres AS sg
    JOIN tv_genres AS g
    ON sg.genre_id = g.id
    WHERE g.name = 'Comedy'
)
ORDER BY title;
