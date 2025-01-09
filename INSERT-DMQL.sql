INSERT INTO public.operator(
	operator_id, operator_name, parent_company,  created_at)
	VALUES (7949, 'CN', 'NY_PARENT_CO',CURRENT_TIMESTAMP);
	
INSERT INTO public.RAILWAY_ROAD(
	RAILWAY_ROAD_TYPE_id, RAILWAY_ROAD_TYPE_NAME,  created_at)
	VALUES (7949, 'C2',CURRENT_TIMESTAMP);
	
--SELECT * FROM STATION;--
	
ALTER TABLE STATION Drop COLUMN GISCODE;

DELETE FROM STATION WHERE GEOM_ACC='NaN';
-- select * from operator order by operator_id desc; --

-- SELECT * FROM RAILWAY_ROAD ORDER BY RAILWAY_ROAD_TYPE_ID DESC; --