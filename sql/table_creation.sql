CREATE DATABASE PlantPal;
USE PlantPal;

CREATE TABLE Users (
 user_id varchar(15) not null,
 first_name varchar(55) not null,
 last_name varchar(55) not null,
 email varchar(55),
 phone_number varchar(55),
 dob date ,
 address varchar(55),
 password varchar(55),
 primary key (`user_id`)
);


CREATE TABLE Plants (
 plant_id varchar(15) not null,
 user_id varchar(15) not null,
 plant_name varchar(55),
 plant_type ENUM('FLOWERING',
 'FRUIT-BEARING',
 'HERB',
 'SHRUB',
 'TREE',
 'SUCCULENT',
 'FERNS',
 'GRASS',
 'VINE') DEFAULT 'FLOWERING',
 primary key (`plant_id`)
);

CREATE TABLE PlantDetails (
  plant_id varchar(15),
  plant_name VARCHAR(55),
  botanical_name VARCHAR(55),
  plant_description TEXT,
  plant_care_instructions TEXT,
  diseases VARCHAR(55),
  plant_type ENUM('FLOWERING',
 'FRUIT-BEARING',
 'HERB',
 'SHRUB',
 'TREE',
 'SUCCULENT',
 'FERNS',
 'GRASS',
 'VINE') DEFAULT 'FLOWERING',
  soil_type ENUM('SANDY',
   'CLAY',
   'LOAMY',
   'SILT',
   'PEATY') DEFAULT 'LOAMY',
  watering_frequency ENUM('DAILY',
  'WEEKLY',
  'BIWEEKLY',
  'MONTHLY',
  'BIMONTHLY') DEFAULT 'WEEKLY',
  fertilizing_frequency ENUM('DAILY',
  'WEEKLY',
  'BIWEEKLY',
  'MONTHLY',
  'BIMONTHLY'
  )  DEFAULT 'MONTHLY',
  fertilizer_type ENUM('ORGANIC',
  'INORGANIC',
  'NITROGEN',
  'PHOSPHATE',
  'POTASSIUM') DEFAULT 'ORGANIC',
  sunlight_type ENUM('FULL_SUN',
  'PARTIAL_SUN',
  'PARTIAL_SHADE',
  'DAPPLED_SUN',
  'FULL_SHADE'
  )  DEFAULT 'PARTIAL_SUN',
  watering_time ENUM(
  'MORNING',
  'EVENING'
  ) DEFAULT 'MORNING',
  watering_methods ENUM(
  'MISTING',
  'WATERING_CAN',
  'BOTTOM_WATERING',
  'GRADUAL_FLOW'
  ) DEFAULT 'WATERING_CAN',
  last_watered_date DATE,
  last_fertilized_date DATE,
  next_watering_date DATE,
  next_fertilizing_date DATE,
  plant_image VARCHAR(255)
)
