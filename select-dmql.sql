SELECT * from train;
select * from train_class;
select * from train_seat;
select * from line;
select * from track;
select * from trackline;
select * from route;
select * from operator;
select * from railway_road;
select * from station;


--q1--
SELECT track_name
FROM track
WHERE track_name LIKE '% %' 
and track_name!='Yard Line' 
and track_name != 'Great Neck 2 to 1';

select  distinct track_name from track where track_name = 'NaN';


--q2
SELECT l.line_id, l.line_name, t.track_id, t.track_name, 
t.track_right_class, tl.tl_id 
FROM line l 
JOIN trackline tl ON l.line_id = tl.line_id 
JOIN track t ON tl.track_id = t.track_id 
WHERE t.track_name = 'NaN'
GROUP BY l.line_id, l.line_name, t.track_id, t.track_name,
 tl.tl_id;



--q3
select  t.track_name, count(l.line_name)  , 
sum(tl.tl_id)
from public.trackline tl
join public.line l
on tl.line_id=l.line_id 
join public.track t
on tl.track_id = t.track_id
group by t.track_name 
order by t.track_name

--q4
select t.train_id, t.train_name, tc.train_class_id, tc.train_class_name 
from train t join train_class tc on t.train_id=tc.train_id;


select distinct parent_company from operator;
select count(*) from operator where parent_company = 'NaN';
--q5
select count(route_id), track_name from route, track 
group by track_name

select count(route_id), track_id, track_name from route, track 
group by track_id

--q6
select parent_company , count(*) from operator group by parent_company order by count(*) desc;
 
select * from station;
