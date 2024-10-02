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


CREATE TABLE IF NOT EXISTS marts.city_overview AS 
SELECT
	Städer,
	ort,
	visningar,
	"visningstid (timmar)"
	
FROM
	stader.tabelldata t ;


CREATE TABLE IF NOT EXISTS marts.viewer_sex_distribution AS (
SELECT
	"Tittarnas kön",
	"Visningar (%)",
	"Genomsnittlig visningslängd",
	"Visningstid (timmar) (%)"
FROM
	tittare.tabelldata_alder tk);


CREATE TABLE IF NOT EXISTS marts.viewer_age_distribution AS(
SELECT
	"Tittarnas ålder",
	"Visningar (%)",
	"Genomsnittlig visningslängd",
	"Visningstid (timmar) (%)"
FROM
	tittare.tabelldata_kon tk);

SELECT * FROM marts.city_overview co ;

DROP TABLE marts.viewer_sex_distribution; 

SELECT * FROM marts.viewer_age_distribution vad ;
SELECT * FROM marts.viewer_sex_distribution vsd ;

SELECT * FROM  information_schema.tables WHERE table_schema = 'marts';

CREATE TABLE IF NOT EXISTS marts.subscription_overview AS(
SELECT
	Prenumerationsstatus,
	visningar,
	"visningstid (timmar)",
	"Genomsnittlig visningslängd"
FROM
	prenumerationsstatus.tabelldata t);




