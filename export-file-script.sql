COPY (SELECT * FROM line) TO 'C:\Program Files\PostgreSQL\16\data\line.csv' WITH CSV HEADER;

COPY (SELECT * FROM line) TO 'C:\Program Files\PostgreSQL\16\data\operator.csv' WITH CSV HEADER;


COPY (SELECT * FROM line) TO 'C:\Program Files\PostgreSQL\16\data\railway_road.csv' WITH CSV HEADER;


COPY (SELECT * FROM line) TO 'C:\Program Files\PostgreSQL\16\data\route.csv' WITH CSV HEADER;


COPY (SELECT * FROM line) TO 'C:\Program Files\PostgreSQL\16\data\station.csv' WITH CSV HEADER;


COPY (SELECT * FROM line) TO 'C:\Program Files\PostgreSQL\16\data\track.csv' WITH CSV HEADER;

COPY (SELECT * FROM line) TO 'C:\Program Files\PostgreSQL\16\data\trackline.csv' WITH CSV HEADER;

COPY (SELECT * FROM line) TO 'C:\Program Files\PostgreSQL\16\data\train.csv' WITH CSV HEADER;

COPY (SELECT * FROM line) TO 'C:\Program Files\PostgreSQL\16\data\train_class.csv' WITH CSV HEADER;

COPY (SELECT * FROM line) TO 'C:\Program Files\PostgreSQL\16\data\train_seat.csv' WITH CSV HEADER;
