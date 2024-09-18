SELECT * FROM  youtube;

SELECT DISTINCT (category) FROM youtube;

SELECT COUNT (*) FROM  youtube;

-- how many in each category
SELECT
	category,
	COUNT(*) AS Number
from
	youtube
GROUP BY
	category
ORDER BY
	number DESC

	

