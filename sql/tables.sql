CREATE EXTENSION postgis;

CREATE TABLE Restaurants (
    coordinate GEOMETRY(POINT,4326),
    restaurant_name varchar(255),
    restaurant_id int UNIQUE,
);

CREATE TABLE Orders (
    coordinate GEOMETRY(POINT,4326),
    restaurant int,
    id int unique,
);
