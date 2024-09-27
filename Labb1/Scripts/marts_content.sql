desc;

SELECT
	*
FROM
	information_schema.schemata
WHERE
	catalog_name = 'youtube_data';
	
CREATE SCHEMA IF NOT EXISTS marts;

CREATE TABLE IF NOT EXISTS marts.geography_overview AS (
SELECT
	Geografi,
	visningar,
	"visningstid (timmar)",
	"genomsnittlig visningslängd"
FROM
	geografi.tabelldata t);

SELECT * FROM  information_schema.tables WHERE table_schema = 'marts';


