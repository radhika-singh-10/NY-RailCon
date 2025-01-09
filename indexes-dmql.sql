


CREATE INDEX train_train_id_idx ON train (train_id);

CREATE INDEX train_seat_train_id_idx ON train_seat (train_id);

CREATE INDEX train_class_train_id_idx ON train_class (train_id);

CREATE INDEX line_id_idx ON line (line_id);

CREATE INDEX operator_id_idx ON operator (operator_id);

CREATE INDEX railway_road_id_idx ON railway_road (railway_road_type_id);

CREATE INDEX station_id_idx ON station (station_id);

CREATE INDEX track_id_idx ON track (track_id);

CREATE INDEX trackline_id_idx ON trackline (tl_id);

