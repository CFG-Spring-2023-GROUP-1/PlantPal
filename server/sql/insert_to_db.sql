--USER TABLE
INSERT INTO Users (UserId, FirstName, LastName, Email, PhoneNo, Dob, Address, Password) VALUES
('1', 'John', 'Doe', 'johndoe@example.com', '1234567890', '1990-01-01', '123 Main St', 'password123'),
('2', 'Jane', 'Smith', 'janesmith@example.com', '9876543210', '1995-05-10', '456 Elm St', 'password456');



--PLANTS
INSERT INTO Plants (PlantId, UserId, CommonNames, Category) VALUES
('1', '1', 'Boston Fern', 'Indoor'),
('2', '2', 'Rose', 'Outdoor');


--PLANT DETAILS
INSERT INTO PlantDetails (PlantId, Category, LatinName, CommonNames, CurrentDisease, LightLevel, Watering, Climate, MaxTemp, MinTemp, GrowthSpeed, CommonDiseases, LeafColour, BloomingSeason, Perfume, ColourOfBloom, Image) VALUES
(1, 'Fern', 'Nephrolepis exaltata', 'Boston Fern', 'None', 'Medium', 'Regular watering', 'Tropical', '{"C": 28, "F": 82.4}', '{"C": 10, "F": 50}', 'Medium', 'None', 'Green', 'Year-round', 'None', 'None', 'boston_fern.jpg'),
(2, 'Rose', 'Rosa', 'Rose', 'None', 'Full Sun', 'Regular watering', 'Temperate', '{"C": 35, "F": 95}', '{"C": 5, "F": 41}', 'Slow', 'Powdery Mildew, Black Spot', 'Red, Pink, White, Yellow', 'Spring to Fall', 'Fragrant', 'Varies', 'rose.jpg');


-- TOPICS
INSERT INTO topics (name) VALUES
    ('Repotting'),
    ('Houseplant Care Tips'),
    ('Watering'),
    ('Propagation'),
    ('Houseplant Deco Tips'),
    ('Pest Care'),
    ('Terrariums & Greenhouses'),
    ('Natural Lighting & Growth Lights');
  
-- insert all the necessary data into 'videos' table:
INSERT INTO videos (video_id, topic, title, description, url, week, date) VALUES
    -- Repotting videos:
    (10, 'Repotting', 'WHEN AND HOW TO REPOT HOUSEPLANTS | complete visual guide with tips!', 'In this video, you can learn how and when to repot your houseplants.', 'https://www.youtube.com/watch?v=K1gMQnwpBDI', 4, '2023-05-01'),
    (11, 'Repotting', 'Best potting mix & soil for indoor plants | Beginners Guide to Soil & Amendments', 'In this video, you can learn about different potting mix & soil types for different plants.', 'https://www.youtube.com/watch?v=Z8uuQyPV_34', 4, '2023-05-01'),
    (12, 'Repotting', 'How to repot a plant? | Beginners Guide to Repotting', 'in this video, you can learn how to repot as a beginner.', 'https://www.youtube.com/watch?v=Fy8kP2EYpcY&t', 4, '2023-05-01'),
   -- Houseplant Care Tips videos:
    (1, 'Houseplant Care Tips', 'HOUSEPLANT CARE TIPS FOR BEGINNERS » + printable guide', 'In this video, you can find basic houseplant care tips for beginners.', 'https://www.youtube.com/watch?v=LZhnCxG5c6s', 1, '2023-04-10'),
    (2, 'Houseplant Care Tips', 'PLANT CARE » 7 mistakes to avoid', 'In this video, you can find basic houseplant mistakes that beginners commonly make.', 'https://www.youtube.com/watch?v=J1LW1Nz0pd4', 1, '2023-04-10'),
    (3, 'Houseplant Care Tips', 'MOSS POLES, STAKES & TRELLISES | what does your houseplant need for bigger leaves and faster growth?', 'In this video, you can find guides on using moss poles, stakes and trellises.', 'https://www.youtube.com/watch?v=WAwHbXv5gyg', 1, '2023-04-10'),
    -- Watering videos:
    (4, 'Watering', '5 Tips on Watering Houseplants | How to Water Plants for Beginners', 'In this video, you can find and learn the basics of watering your houseplants.', 'https://www.youtube.com/watch?v=lNzPahs-UAg', 2, '2023-04-17'),
    (5, 'Watering', 'Houseplant 101: How Often to Water Your Houseplants', 'In this video, you will learn how to tell how often your houseplants need watering.', 'https://www.youtube.com/watch?v=VfN6_hzAfPY', 2, '2023-04-17'),
    (6, 'Watering', 'Houseplant 101: How to Water Houseplants Properly', 'In this video, you can learn the different methods/ techniques on watering your houseplants.', 'https://www.youtube.com/watch?v=QuIeuchzAos', 2, '2023-04-17'),
    (7, 'Watering', 'Bottom Watering Indoor Plants | How to water really dry houseplants!', 'In this video, you can learn about bottom watering houseplants that are really dry/ with hydrophobic soil.', 'https://www.youtube.com/watch?v=UR7meOqFq6c', 2, '2023-04-17'),
    -- Propagation videos:
    (15, 'Propagation', 'Plant propagation for beginners » 5 indoor plants', 'In this video, you can explore the different methods of plant propagation.', 'https://www.youtube.com/watch?v=Jh5oX0VRnzk', 6, '2023-05-15'),
    (16, 'Propagation', 'how to grow herbs at home without soil', 'In this video, you can learn how to grow herbs at home via water propagation.', 'https://www.youtube.com/watch?v=W5oCcgGixR0', 6, '2023-05-15'),
    (17, 'Propagation', 'tips for successful vine propagations | propagate houseplants with me!', 'In this video, you can learn how to vine propagate your houseplants.', 'https://www.youtube.com/watch?v=cjjaXujP1hE', 6, '2023-05-15'),
   -- Houseplant Deco Tips videos:
    (20, 'Houseplant Deco Tips', 'Ways to make your houseplants look a little bit nicer', 'In this video, you can find creative plant display ideas for your houseplants.', 'https://www.youtube.com/watch?v=yNHsTC1c_HA&t', 8, '2023-05-29'),
    (21, 'Houseplant Deco Tips', 'Cool Alternatives to Popular Houseplants | This not That', 'In this video, you can find other alternatives for popular houseplants to buy and care for.', 'https://www.youtube.com/watch?v=ZEM13kK3FUk', 8, '2023-05-29'),
	(22, 'Houseplant Deco Tips', 'Creative ways to display houseplants | how to', 'In this video, you can find unique creative ways to display your houseplants (i.e. kokedama, vanda pot, etc).', 'https://www.youtube.com/watch?v=3eLgUzAAfmM', 8, '2023-05-29'),
   -- Pest Care videos:
    (13, 'Pest Care', 'Houseplant Pest Management | simple effective method for all plant pests', 'In this video, you can learn how using a mix of systemic insecticide + a foliar spray applied with a pressurized spray bottle can help combat most pests.', 'https://www.youtube.com/watch?v=-GJUyapeYXo',5, '2023-05-08'),
    (14, 'Pest Care', 'Houseplant Pests Control | Identify Fungus Gnats, Spider Mites, Mealybugs & Scales', 'In this video, you can learn how to identify the different types of pests as well as control/ preventive methods that you can use against them.', 'https://www.youtube.com/watch?v=JN4GgS9zarg', 5, '2023-05-08'),
    -- Terrariums & Greenhouses videos:
    (18, 'Terrariums & Greenhouses', 'How To Make A Terrarium | A Beginners Guide', 'In this video, you can find a beginner guide on how to make and care of a terrarium.', 'https://www.youtube.com/watch?v=t2jL3QP4hTA', 7, '2023-05-22'),
    (19, 'Terrariums & Greenhouses', '10 ESSENTIAL Terrarium Tips For Beginners!', 'In this video, you can find 10 essential tips to making & keeping healthy terrariums.', 'https://www.youtube.com/watch?v=GIWy75QPxkI', 7, '2023-05-22'),
    -- Natural Lighting & Growth Lights videos:
    (8, 'Natural Lighting & Growth Lights', 'My houseplant grow lights and set up | no natural light', 'In this video, you can learn how to choose/ select the right type of Growth Lights for your houseplants.', 'https://www.youtube.com/watch?v=mIDvUrtkjyE', 3, '2023-04-24'),
    (9, 'Natural Lighting & Growth Lights', 'houseplant lighting guide | best plants for each window direction', 'Discover techniques to optimize natural light (i.e. facing your houseplants in which window direction) for better plant growth.', 'https://www.youtube.com/watch?v=Jnt96eF9zZc', 3, '2023-04-24');

-- insert all the necessary data into 'ratings' table:
INSERT INTO ratings (video_id, rating, comment) VALUES
    (1, 4, 'This tutorial was very helpful.'),
    (2, 5, 'I learned a lot from this video. Highly recommended!'),
    (3, 3, 'The video quality could be better, but the instructions were clear.');
    -- Insert more example ratings/testimonials in the future

-- insert all the necessary data into 'ads' table:
-- used example domains for image and ad url (as don't need permission to use)
INSERT INTO ads (title, description, image_url, ad_url) VALUES
    ('Plant Fertilizer Sale', 'Get 15% off on all plant fertilizers!', 'https://example.com/images/fertilizer-ad.jpg', 'https://example.com/sale'),
    ('Plant Care Workshop', 'Join our plant care workshop and learn expert tips!', 'https://example.com/images/workshop-ad.jpg', 'https://example.com/workshop'),
    ('Plant Pot Collection', 'Explore our new collection of stylish plant pots.', 'https://example.com/images/pot-ad.jpg', 'https://example.com/pots');






