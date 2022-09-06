create table MyDimDate(
    Dateid SMALLINT NOT NULL PRIMARY KEY,
    Date DATE NOT NULL,
    Year SMALLINT NOT NULL,
    Quarter SMALLINT NOT NULL,
    Quartername VARCHAR(10) NOT NULL,
    Month SMALLINT NOT NULL,
    Monthname VARCHAR(10) NOT NULL,
    Day SMALLINT NOT NULL,
    Weekday SMALLINT NOT NULL,
    Weekdayname VARCHAR(10) NOT NULL
);

create table MyDimWaste(
    Wasteid SMALLINT NOT NULL PRIMARY KEY,
    Wastetype VARCHAR(5) NOT NULL,
    Wastecollected DECIMAL(6,2) NOT NULL
);

create table MyFactTrips(
    Tripid INT NOT NULL PRIMARY KEY,
    Dateid SMALLINT NOT NULL REFERENCES MyDimDate(Dateid),
    Stationid SMALLINT NOT NULL REFERENCES DimStation(Stationid),
    Truckid SMALLINT NOT NULL REFERENCES DimTruck(Truckid),
    Wastecollected DECIMAL(6,2) NOT NULL
);