CREATE EXTENSION postgis;

CREATE TABLE Restaurants (
    coordinate GEOMETRY(POINT,4326),
    restaurant_name varchar(255),
    restaurant_id int UNIQUE,
    PRIMARY KEY(restaurant_id)
);

CREATE TABLE Orders (
    coordinate GEOMETRY(POINT,4326),
    restaurant int unique,
    id int unique,
    PRIMARY KEY(id),
    FOREIGN KEY(restaurant) references Restaurants(restaurant_id)
    ON DELETE CASCADE
);
