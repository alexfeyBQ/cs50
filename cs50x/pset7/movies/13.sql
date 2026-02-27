-- 13. Names of all people who starred in a movie in which Kevin Bacon also starred
SELECT DISTINCT p1.name FROM stars s1
JOIN people p1 ON p1.id = s1.person_id
JOIN stars s2 ON s2.movie_id = s1.movie_id
JOIN people p2 ON p2.id = s2.person_id
WHERE p2.name = 'Kevin Bacon' AND p1.name != 'Kevin Bacon';
