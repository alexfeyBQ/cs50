-- 12. Titles of all of movies in which both Jennifer Lawrence and Bradley Cooper starred
SELECT movies.title FROM movies
JOIN stars s1 ON s1.movie_id = movies.id
JOIN people p1 ON p1.id = s1.person_id
JOIN stars s2 ON s2.movie_id = movies.id
JOIN people p2 ON p2.id = s2.person_id
WHERE p1.name = 'Jennifer Lawrence' AND p2.name = 'Bradley Cooper';
