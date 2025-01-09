import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine,text
from datetime import datetime


def create_table_load_data():
    dbname = 'postgres'
    user = 'postgres'
    password = 'root'
    host = "127.0.0.1"
    port = "5432"
    connection_string = f"postgresql://{user}:{password}@{host}/{dbname}"
    engine = create_engine(connection_string)
    df = pd.read_csv('new-york-state-railroad-dmql.csv')
    df['CLASS'].head()
    conn = psycopg2.connect(
        dbname = 'postgres',
        user = 'postgres',
        password = 'root',
        host = "127.0.0.1",
        port = "5432")
    cur = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Train (
        train_id SERIAL PRIMARY KEY,
        train_name VARCHAR(20) NOT NULL,
        created_at TIMESTAMP NOT NULL
    );

    CREATE INDEX IF NOT EXISTS idx_train_train_name ON Train (train_name);
    """

    cur.execute(create_table_query)
    conn.commit()
    cols_to_load = ['Train_NAME']
    df = pd.read_csv('new-york-state-railroad-dmql.csv', usecols=cols_to_load)
    df.columns = ['train_name']

    current_time = datetime.now()

    for index, row in df.iterrows():
        cur.execute(
            "INSERT INTO Train (train_name, created_at) VALUES (%s, %s)",
            (row['train_name'], current_time)
        )

    conn.commit()
    create_railway_road_table = """
    CREATE TABLE IF NOT EXISTS Railway_Road (
        railway_road_type_id SERIAL PRIMARY KEY,
        railway_road_type_name VARCHAR(100),
        created_at TIMESTAMP NOT NULL
    );

    CREATE INDEX IF NOT EXISTS idx_railway_road_type_name ON Railway_Road (railway_road_type_name);
    """

    cur.execute(create_railway_road_table)
    conn.commit()


    cols_to_load = ['RR_TYPE1']
    df = pd.read_csv('new-york-state-railroad-dmql.csv', usecols=cols_to_load)
    current_time = datetime.now()

    for index, row in df.iterrows(): 
        cur.execute(
            "INSERT INTO Railway_Road (railway_road_type_name, created_at) VALUES (%s, %s)",
            (row['RR_TYPE1'], current_time)
        )


    conn.commit()
    create_operator_table = """
    CREATE TABLE IF NOT EXISTS Operator (
        operator_id SERIAL PRIMARY KEY,
        operator_name VARCHAR(100),
        parent_company VARCHAR(100),
        created_at TIMESTAMP NOT NULL
    );


    CREATE INDEX IF NOT EXISTS idx_operator_name ON Operator (operator_name);
    """

    cur.execute(create_operator_table)
    conn.commit()
    cols_to_load = ['OPERATOR','PARENT_CO']
    df = pd.read_csv('new-york-state-railroad-dmql.csv', usecols=cols_to_load)
    created_at = datetime.now()
    df.columns = ['operator_name','parent_company']
    df.head()
    # Insert data into the "Train_Class" table
    for index, row in df.iterrows():
        #print(row['operator_name'],row['parent_company'], created_at)
        cur.execute(
            "INSERT INTO Operator (operator_name, parent_company, created_at) VALUES (%s, %s, %s)",
            (row['operator_name'],row['parent_company'], created_at)
        )
        

    conn.commit()
    create_train_class_table = """
    CREATE TABLE IF NOT EXISTS Train_Class (
        train_class_id SERIAL PRIMARY KEY,
        train_id INTEGER REFERENCES Train(train_id),
        train_class_name VARCHAR(20),
        created_at TIMESTAMP NOT NULL
    );

    CREATE INDEX IF NOT EXISTS idx_train_class_name ON Train_Class (train_class_name);
    """

    cur.execute(create_train_class_table)
    conn.commit()


    cols_to_load = ['CLASS', 'Train_NAME']
    df = pd.read_csv('new-york-state-railroad-dmql.csv', usecols=cols_to_load)
    df.columns = ['train_class_name', 'train_name'] 
    created_at = datetime.now()

    for index, row in df.iterrows():
        train_name = row['train_name']
        cur.execute("SELECT train_id FROM Train WHERE train_name = %s", (train_name,))
        train_id = cur.fetchone()
        if train_id:
            cur.execute(
                "INSERT INTO Train_Class ( train_id, train_class_name, created_at) VALUES ( %s, %s, %s)",
                (train_id[0], row['train_class_name'], created_at)
            )
        else:
            print(f"Train '{train_name}' not found in Train table.")


    conn.commit()
    create_track_query = """
    CREATE TABLE IF NOT EXISTS Track (
        track_id SERIAL PRIMARY KEY,
        track_name VARCHAR(100) ,
        track_right_class VARCHAR(100),
        electrification VARCHAR(100),
        haul_right VARCHAR(100),
        created_at TIMESTAMP NOT NULL
    );
    CREATE INDEX IF NOT EXISTS idx_track_name ON Track (track_name);
    CREATE INDEX IF NOT EXISTS idx_track_right_class ON Track (track_right_class);
    CREATE INDEX IF NOT EXISTS idx_electrification ON Track (electrification);
    CREATE INDEX IF NOT EXISTS idx_haul_right ON Track (haul_right);
    """

    cur.execute(create_track_query)
    conn.commit()


    cols_to_load = ['Trk_Name','TRACK_RIGH','ELECTRIFIC','HAUL_RIGHT']
    df = pd.read_csv('new-york-state-railroad-dmql.csv', usecols=cols_to_load)
    df.columns = ['track_name','track_right_class','electrification','haul_right']

    current_time = datetime.now()
    for index, row in df.iterrows():
        cur.execute(
            "INSERT INTO Track(track_name,track_right_class,electrification,haul_right, created_at) VALUES (%s, %s, %s, %s, %s)",
            (row['track_name'], row['track_right_class'], row['electrification'], row['haul_right'], current_time)
        )

    conn.commit()

    create_station_query = """
        CREATE TABLE IF NOT EXISTS Station (
        station_id SERIAL PRIMARY KEY,
        station_to VARCHAR(100) ,
        station_from VARCHAR(100),
        geom_acc VARCHAR(100) ,
        giscode VARCHAR(100),
        state VARCHAR(100),
        shape_length VARCHAR(100),
        created_at TIMESTAMP NOT NULL
    );
    
    CREATE INDEX IF NOT EXISTS idx_station_to ON Station (station_to);
    CREATE INDEX IF NOT EXISTS idx_station_from ON Station (station_from);
    CREATE INDEX IF NOT EXISTS idx_giscode ON Station (giscode);
    CREATE INDEX IF NOT EXISTS idx_state ON Station (state);
    """
    
    cur.execute(create_station_query)
    conn.commit()
    
    
    cols_to_load = ['Station_To','Station_F','GEOM_ACC','GISCODE','STATE', 'Shape_Length']
    df = pd.read_csv('new-york-state-railroad-dmql.csv', usecols=cols_to_load)
    df.columns = ['station_to','station_f','geom_acc','giscode','state','shape_length']
    
    current_time = datetime.now()
    
    for index, row in df.iterrows():
        cur.execute(
            "INSERT INTO Station (station_to,station_from,geom_acc,giscode,state, shape_length, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row['station_to'],row['station_f'],row['geom_acc'],row['giscode'],row['state'],row['shape_length'], current_time)
        )
    
    conn.commit()
    
    create_route_query = """
    CREATE TABLE IF NOT EXISTS Route (
        route_id SERIAL PRIMARY KEY,
        route_name VARCHAR(20),
        created_at TIMESTAMP NOT NULL
    );
    
    -- Add index to improve query performance
    CREATE INDEX IF NOT EXISTS idx_route_name ON Route (route_name);
    """
    
    cur.execute(create_route_query)
    conn.commit()
    
    
    cols_to_load = ['Route']
    df = pd.read_csv('new-york-state-railroad-dmql.csv', usecols=cols_to_load)
    df.columns = ['route']
    
    current_time = datetime.now()
    
    for index, row in df.iterrows():
        cur.execute(
            "INSERT INTO Route (route_name, created_at) VALUES (%s, %s)",
            (row['route'], current_time)
        )
    
    conn.commit()
    
    create_line_query = """
    CREATE TABLE IF NOT EXISTS Line (
        line_id SERIAL PRIMARY KEY,
        line_name VARCHAR(100) NOT NULL,
        created_at TIMESTAMP NOT NULL
    );
    CREATE INDEX IF NOT EXISTS idx_line_name ON Line (line_name);
    """
    
    cur.execute(create_line_query)
    conn.commit()
    
    
    cols_to_load = ['LINE_NAME']
    df = pd.read_csv('new-york-state-railroad-dmql.csv', usecols=cols_to_load)
    df.columns = ['line_name']
    
    current_time = datetime.now()
    
    for index, row in df.iterrows():
        cur.execute(
            "INSERT INTO Line(line_name, created_at) VALUES (%s, %s)",
            (row['line_name'], current_time)
        )
    
    conn.commit()
    
    create_trackline_query = """
    CREATE TABLE IF NOT EXISTS TrackLine (
        tl_id SERIAL PRIMARY KEY,
        track_id INTEGER REFERENCES Track(track_id),
        line_id INTEGER REFERENCES LINE(line_id),
        created_at TIMESTAMP NOT NULL
    );
    
    CREATE INDEX IF NOT EXISTS idx_trackline_track_id ON TrackLine (track_id);
    CREATE INDEX IF NOT EXISTS idx_trackline_line_id ON TrackLine (line_id);
    """
    
    cur.execute(create_trackline_query)
    conn.commit()
    
    rows = cur.fetchall()
    created_at = datetime.now()
    
    for row in rows:
        track_id, line_id = row
        cur.execute(
            "INSERT INTO TrackLine (track_id, line_id, created_at) VALUES ( %s, %s, %s)",
            ( track_id, line_id, created_at)
        )
    
    conn.commit()
    
    cur.close()
    conn.close()
    
    cur = conn.cursor()
    
    
    create_train_seat_table = """
    CREATE TABLE IF NOT EXISTS Train_Seat (
        train_seat_id SERIAL PRIMARY KEY,
        train_id INTEGER REFERENCES Train(train_id),
        train_seat_name VARCHAR(200) not null,
        created_at TIMESTAMP NOT NULL
    );
    """
    
    cur.execute(create_train_seat_table)
    conn.commit()
    
    
    
    
    
    cols_to_load = ['SEAT_NAME','Train_NAME']
    df = pd.read_csv('new-york-state-railroad_dmql.csv', usecols=cols_to_load)
    df.columns = ['train_seat_name', 'train_name'] 
    created_at = datetime.now()
    
    for index, row in df.iterrows():
        train_name = row['train_name']
        cur.execute("SELECT train_id FROM Train WHERE train_name = %s", (train_name,))
        train_id = cur.fetchone()
        if train_id:
            cur.execute(
                "INSERT INTO Train_Seat ( train_id, train_seat_name, created_at) VALUES ( %s, %s, %s)",
                (train_id[0], row['train_seat_name'], created_at)
            )
        else:
            print(f"Train '{train_name}' not found in Train table.")
    
    
    conn.commit()
    cur.close()
    conn.close()
    
    rows = cur.fetchall()
    created_at = datetime.now()
    
    for row in rows:
        train_id,train_class_id= row
        cur.execute(
            "INSERT INTO TrainSeat (train_id, train_class_id, created_at) VALUES ( %s, %s, %s)",
            ( train_id,train_class_id)
        )
    
    conn.commit()
    
    cur.close()
    conn.close()
    
    


if __name__ == "__main__":
    create_table_load_data()