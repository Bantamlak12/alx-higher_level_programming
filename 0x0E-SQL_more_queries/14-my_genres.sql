-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- use the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT g.name
FROM tv_genres AS g INNER JOIN tv_show_genres AS t
ON g.id = t.genre_id
INNER JOIN tv_shows AS s
ON s.id = t.show_id
WHERE s.title = "Dexter"
ORDER BY g.name
