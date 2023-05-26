CREATE DATABASE PlantPal;
USE PlantPal;


CREATE TABLE Users (
 UserId varchar(255) not null,
 FirstName varchar(55) not null,
 LastName varchar(55) not null,
 Email varchar(55),
 PhoneNo varchar(55),
 Dob date ,
 Address varchar(55),
 Password varchar(255),
 primary key (`UserId`)
);

CREATE TABLE Plants (
 PlantId varchar(15) not null,
 UserId varchar(15) not null,
 CommonNames varchar(255),
 Category varchar(55),
 primary key (`PlantId`)
);

CREATE TABLE PlantDetails (
  PlantId INT PRIMARY KEY,
  Category varchar(55),
  LatinName varchar(55),
  CommonNames varchar(255),
  CurrentDisease varchar(255),
  LightLevel varchar(255),
  Watering TEXT,
  Climate varchar(55),
  MaxTemp JSON,
  MinTemp JSON,
  GrowthSpeed varchar(55),
  CommonDiseases TEXT,
  LeafColour varchar(25),
  BloomingSeason varchar(25),
  Perfume varchar(55),
  ColourOfBloom varchar(25),
  Image varchar(255),
)


user = User(
    "Emina",
    "Ergul",
    "emina.ergul@example.com",
    "+1234567890",
    "1990-01-01",
    "123 Main Street, City, Country",
    "password123",
)