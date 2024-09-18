SELECT * FROM chess;
-- Find out the possible categories for winner column.

SELECT Winner FROM chess;

-- Find out the possible categories for victory_status column.
SELECT  victory_status FROM chess;

--Check total number of games represented in the dataset

SELECT
	COUNT(*) as total_matches
FROM
	chess;
	
-- Get statistics on the number draws, the number of white wins and number of black wins.
SELECT
	victory_status, COUNT(*) as number_draws
FROM
	chess
GROUP BY
	victory_status
HAVING victory_status = 'draw';

-- Check the top 10 most popular openings

SELECT
	opening_name,
	COUNT(*) as popular_moves
FROM
	chess
GROUP BY
	opening_name ORDER BY popular_moves DESC ; 

--Which whiteside player has the highest ranking?
SELECT
	MAX (white_rating) as highest_rating,
	white_id, 
FROM
	chess
GROUP BY white_id ORDER BY highest_rating DESC;

--Which blackside player has the highest ranking?

SELECT
	MAX(black_rating) as highest_rating,
	black_id
FROm
	chess
GROUP BY
	black_id
ORDER BY
	highest_rating DESC;


