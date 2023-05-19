--USER TABLE
INSERT INTO Users (UserId, FirstName, LastName, Email, PhoneNo, Dob, Address, Password_Hash, Password_Salt)
VALUES
('1', 'John', 'Doe', 'johndoe@example.com', '1234567890', '1990-01-01', '123 Main Street', 'c2c8a2a2249f97e8b63f7843e5e9f5f56e7fd16a', '32b137fcfae6e989a8aee56a0a378d414db8c678'),
('2', 'Jane', 'Smith', 'janesmith@example.com', '0987654321', '1985-05-10', '456 Elm Street', 'b9350d26994a9a4a4e1bca2f4ce70828a7dbfd3d', 'c4a9b48a3e897b37213fc2d63cbb41a5a93b19e4');


--PLANTS
INSERT INTO Plants (PlantId, UserId, CommonNames, Category)
VALUES
('1', '1', 'Boston Fern', 'Ferns'),
('2', '2', 'Rose', 'Flowering Plants');

--PLANT DETAILS
INSERT INTO PlantDetails (PlantId, Category, LatinName, CommonNames, LightLevel, Watering, Climate, MaxTemp, MinTemp, GrowthSpeed, CommonDiseases, PlantDescription, LeafColour, BloomingSeason, Perfume, ColourOfBloom, Image)
VALUES
('1', 'Ferns', 'Nephrolepis exaltata', 'Boston Fern', 'Medium to bright indirect light', 'Regular watering to keep soil moist', 'Tropical', '{"C": 28, "F": 82.4}', '{"C": 10, "F": 50}', 'Moderate', 'Leaf spot, root rot', 'The Boston Fern is a popular indoor plant known for its lush, green fronds.', 'Green', 'N/A', 'None', 'N/A', 'image1.jpg'),
('2', 'Flowering Plants', 'Rosa', 'Rose', 'Full sun', 'Regular watering, allowing the soil to dry slightly between waterings', 'Temperate', '{"C": 35, "F": 95}', '{"C": -5, "F": 23}', 'Slow', 'Powdery mildew, black spot', 'Roses are classic flowering plants that come in various colors and have a pleasant fragrance.', 'Various colors', 'Spring, summer', 'Fragrant', 'Varies', 'image2.jpg');
