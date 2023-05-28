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
  Image varchar(255)
)

-- creating a table, named 'topics' which contains all the available topics:
CREATE TABLE topics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- creating a table, named 'videos' which contains all necessary data for all YT videos uploaded:
CREATE TABLE videos (
    video_id INT NOT NULL,
    topic VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    url VARCHAR(255) NOT NULL,
    week INT NOT NULL,
    date DATE NOT NULL
);

-- Create index on video_id column in topics table
CREATE INDEX idx_video_id ON videos (video_id);

-- Create an index on the topic_name column in the videos table
CREATE INDEX idx_videos_topic_name ON videos (topic);

-- creating a table, named 'ratings' which contains ratings + comments for each video:
CREATE TABLE ratings (
    video_id INT NOT NULL,
    rating INT NOT NULL,
    comment TEXT,
    FOREIGN KEY (video_id) REFERENCES videos(video_id)
);


-- user = User(
--     "Emina",
--     "Ergul",
--     "emina.ergul@example.com",
--     "+1234567890",
--     "1990-01-01",
--     "123 Main Street, City, Country",
--     "password123",
-- )
