SELECT  * FROM  innehall.tabelldata t 


WITH 
	date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
	date_total AS (SELECT * FROM datum.totalt OFFSET 1)
SELECT 
	STRFTIME('%Y-%m-%d', tot.datum), 
	tot.visningar,
	tab.visningar,
	tab."visningstid (timmar)"
FROM date_total as tot
LEFT JOIN date_table as tab 
ON tot.datum = tab.datum;


SELECT Enhetstyp, count(*) total_rows, sum(Visningar) as total_visningar 
from 
enhetstyp.diagramdata group by Enhetstyp ;

select * from enhetstyp.diagramdata d ;

SELECT * EXCLUDE (Innehåll) FROM  innehall.tabelldata ORDER BY "Visningstid (timmar)" DESC OFFSET 1 LIMIT 5;

SELECT * FROM  innehall.diagramdata;-- ORDER BY "Visningstid (timmar)";

SELECT STRFTIME('%Y-%m-%d', Datum), Visningar FROM innehall.totalt;

-- visar antalet visningar, visningstis och genomsnittlig längd
SELECT * FROM  datum.tabelldata;

SELECT  * FROM geografi.tabelldata;

SELECT * FROM  geografi.diagramdata; -- kollar över geografidatan

-- Show the sum of the views for each country, SE, IN, MT
SELECT

	Geografi,
	SUM(visningar)
FROM
	geografi.diagramdata
GROUP BY
	Geografi
ORDER BY
	SUM(visningar);



SELECT * FROM  enhetstyp.diagramdata; --shows Unit and the amout of views + duration

-- shows the amount of views from each unit
SELECT
	enhetstyp,
	SUM (visningar)
FROM
	enhetstyp.diagramdata
GROUP BY
	Enhetstyp
ORDER BY
	SUM (Visningar)
	
--shows the unit and amount of views
SELECT
	Enhetstyp, 
	SUM(visningar)
FROM
	enhetstyp.diagramdata 
WHERE 
	Enhetstyp = 'Surfplatta'

GROUP BY 
	Enhetstyp

ORDER BY 
	SUM(visningar);

SELECT * FROM operativsystem.tabelldata t ;

-- shows the OS and views between two specific dates
SELECT operativsystem, SUM(visningar) as visningar
FROM operativsystem.diagramdata 
WHERE Datum BETWEEN '2024-08-19' AND '2024-09-07'
GROUP BY Operativsystem 
ORDER BY SUM(Visningar) ;


SELECT  * FROM geografi.tabelldata t ;

SELECT * FROM innehall.totalt t ;

SELECT * FROM prenumerationskalla.diagramdata d ;

SELECT * FROM tittare.tabelldata_alder ta 

SELECT  * FROM  tittare.tabelldata_kon tk ;

SELECT * FROM stader.totalt t ;

SELECT  * FROM  stader.tabelldata t ;
