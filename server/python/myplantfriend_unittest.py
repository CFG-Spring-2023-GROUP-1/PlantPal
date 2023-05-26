# this is the unit test file for 'My Plant Friend' feature:
import unittest
from unittest.mock import patch
from unittest import TestCase, mock
import json
# import mysql.connector

from app import app, VideoNotFoundException_current_week, VideoTopicsNotFoundException, VideosByTopicNotFoundException, \
    AdsNotFetchedException


# Unit tests for current week videos :
class VideoEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    @patch('app.db_cursor')
    # Mock the behavior of the database cursor to return some info:
    def test_get_current_videos_success(self, mock_db_cursor):
        mock_db_cursor.execute.return_value = None
        mock_db_cursor.fetchall.return_value = [('18', 'How To Make A Terrarium | A Beginners Guide',
                                                 'In this video, you can find a beginner guide on how to make and care '
                                                 'of a terrarium.', 'https://www.youtube.com/watch?v=t2jL3QP4hTA'),
                                                ('19', '10 ESSENTIAL Terrarium Tips For Beginners!',
                                                 'In this video, you can find 10 essential tips to making & keeping '
                                                 'healthy terrariums.', 'https://www.youtube.com/watch?v=GIWy75QPxkI')]

        # Make a GET request to the '/videos/current' endpoint:
        response = self.app.get('/videos/current')
        data = response.get_json()

        # Assert the response status code and content:
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'feature week videos fetched successfully')
        self.assertEqual(len(data['videos']), 2)
        self.assertEqual(data['videos'][0]['video_id'], '18')
        self.assertEqual(data['videos'][0]['title'], 'How To Make A Terrarium | A Beginners Guide')
        self.assertEqual(data['videos'][0]['description'],
                         'In this video, you can find a beginner guide on how to make and care of a terrarium.')
        self.assertEqual(data['videos'][0]['url'], 'https://www.youtube.com/watch?v=t2jL3QP4hTA')
        self.assertEqual(data['videos'][1]['video_id'], '19')
        self.assertEqual(data['videos'][1]['title'], '10 ESSENTIAL Terrarium Tips For Beginners!')
        self.assertEqual(data['videos'][1]['description'],
                         'In this video, you can find 10 essential tips to making & keeping healthy terrariums.')
        self.assertEqual(data['videos'][1]['url'], 'https://www.youtube.com/watch?v=GIWy75QPxkI')

    # Mock the behavior of the database cursor to return an empty list with no data inside:
    @patch('app.db_cursor')
    def test_get_current_videos_no_videos_found(self, mock_db_cursor):
        mock_db_cursor.execute.return_value = None
        mock_db_cursor.fetchall.return_value = []

        with self.assertRaises(VideoNotFoundException_current_week) as context:
            self.app.get('/videos/current')

        # Assert the response status code and content:
        self.assertEqual(context.exception.message, "No videos found for the current week")
        self.assertEqual(context.exception.status_code, 404)


if __name__ == '__main__':
    unittest.main()


# Unit tests for fetching topics' names from db:
class VideoTopicsTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    @patch('app.db_cursor')
    def test_get_video_topics_success(self, mock_db_cursor):
        mock_db_cursor.execute.return_value = None
        mock_db_cursor.fetchall.return_value = [('Repotting',), ('Houseplant Care Tips',), ('Watering',),
                                                ('Propagation',),
                                                ('Houseplant Deco Tips',), ('Pest Care',),
                                                ('Terrariums & Greenhouses',),
                                                ('Natural Lighting & Growth Lights',)]

        response = self.app.get('/videos/topics')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'topics fetched successfully')
        self.assertEqual(len(data['topics']), 8)
        self.assertEqual(data['topics'][0]['name'], 'Repotting')
        self.assertEqual(data['topics'][1]['name'], 'Houseplant Care Tips')
        self.assertEqual(data['topics'][2]['name'], 'Watering')
        self.assertEqual(data['topics'][3]['name'], 'Propagation')
        self.assertEqual(data['topics'][4]['name'], 'Houseplant Deco Tips')
        self.assertEqual(data['topics'][5]['name'], 'Pest Care')
        self.assertEqual(data['topics'][6]['name'], 'Terrariums & Greenhouses')
        self.assertEqual(data['topics'][7]['name'], 'Natural Lighting & Growth Lights')

    @patch('app.db_cursor')
    def test_get_video_topics_empty(self, mock_db_cursor):
        mock_db_cursor.execute.return_value = None
        mock_db_cursor.fetchall.return_value = []

        with self.assertRaises(VideoTopicsNotFoundException) as context:
            self.app.get('/videos/topics')

        self.assertEqual(context.exception.message, 'No video topics found.')
        self.assertEqual(context.exception.status_code, 404)


if __name__ == '__main__':
    unittest.main()


# Unit tests for the get_videos_by_topic endpoint
class GetVideosByTopicTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    @patch('app.db_cursor')
    def test_get_videos_by_topic_success(self, mock_db_cursor):
        mock_db_cursor.execute.return_value = None
        mock_db_cursor.fetchall.return_value = [
            ('10', 'WHEN AND HOW TO REPOT HOUSEPLANTS | complete visual guide with tips!',
             'In this video, you can learn how and when to repot your houseplants.',
             'https://www.youtube.com/watch?v=K1gMQnwpBDI'),
            ('11', 'Best potting mix & soil for indoor plants | Beginners Guide to Soil & Amendments',
             'In this video, you can learn about different potting mix & soil types for different plants.',
             'https://www.youtube.com/watch?v=Z8uuQyPV_34'),
            ('12', 'How to repot a plant? | Beginners Guide to Repotting',
             'in this video, you can learn how to repot as a beginner.',
             'https://www.youtube.com/watch?v=Fy8kP2EYpcY&t')
        ]

        response = self.app.get('/videos/topics/Repotting')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'videos by topic fetched successfully')
        self.assertEqual(len(data['videos']), 3)
        self.assertEqual(data['videos'][0]['video_id'], '10')
        self.assertEqual(data['videos'][0]['title'],
                         'WHEN AND HOW TO REPOT HOUSEPLANTS | complete visual guide with tips!')
        self.assertEqual(data['videos'][0]['description'],
                         'In this video, you can learn how and when to repot your houseplants.')
        self.assertEqual(data['videos'][0]['url'], 'https://www.youtube.com/watch?v=K1gMQnwpBDI')
        self.assertEqual(data['videos'][1]['video_id'], '11')
        self.assertEqual(data['videos'][1]['title'],
                         'Best potting mix & soil for indoor plants | Beginners Guide to Soil & Amendments')
        self.assertEqual(data['videos'][1]['description'],
                         'In this video, you can learn about different potting mix & soil types for different plants.')
        self.assertEqual(data['videos'][1]['url'], 'https://www.youtube.com/watch?v=Z8uuQyPV_34')
        self.assertEqual(data['videos'][2]['video_id'], '12')
        self.assertEqual(data['videos'][2]['title'], 'How to repot a plant? | Beginners Guide to Repotting')
        self.assertEqual(data['videos'][2]['description'], 'in this video, you can learn how to repot as a beginner.')
        self.assertEqual(data['videos'][2]['url'], 'https://www.youtube.com/watch?v=Fy8kP2EYpcY&t')

    @patch('app.db_cursor')
    def test_get_videos_by_topic_no_results(self, mock_db_cursor):
        # Mock the database cursor to return an empty list with no values:
        mock_db_cursor.execute.return_value = None
        mock_db_cursor.fetchall.return_value = []

        with self.assertRaises(VideosByTopicNotFoundException) as context:
            self.app.get('/videos/topics/MossPoles')

        self.assertEqual(context.exception.message, "No videos found for this topic.")
        self.assertEqual(context.exception.status_code, 404)


if __name__ == '__main__':
    unittest.main()


# Unit tests for get_all_videos endpoint:
class AdsTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    @patch('app.db_cursor')
    def test_get_all_ads_success(self, mock_db_cursor):
        mock_db_cursor.execute.return_value = None
        mock_db_cursor.fetchall.return_value = [
            ('Plant Fertilizer Sale', 'Get 15% off on all plant fertilizers!',
             'https://example.com/images/fertilizer-ad.jpg', 'https://example.com/sale'),
            ('Plant Care Workshop', 'Join our plant care workshop and learn expert tips!',
             'https://example.com/images/workshop-ad.jpg', 'https://example.com/workshop'),
            ('Plant Pot Collection', 'Explore our new collection of stylish plant pots.',
             'https://example.com/images/pot-ad.jpg', 'https://example.com/pots')
        ]

        response = self.app.get('/ads')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'ads fetched successfully')
        self.assertEqual(len(data['ads']), 3)
        self.assertEqual(data['ads'][0]['title'], 'Plant Fertilizer Sale')
        self.assertEqual(data['ads'][0]['description'], 'Get 15% off on all plant fertilizers!')
        self.assertEqual(data['ads'][0]['image_url'], 'https://example.com/images/fertilizer-ad.jpg')
        self.assertEqual(data['ads'][0]['ad_url'], 'https://example.com/sale')
        self.assertEqual(data['ads'][1]['title'], 'Plant Care Workshop')
        self.assertEqual(data['ads'][1]['description'], 'Join our plant care workshop and learn expert tips!')
        self.assertEqual(data['ads'][1]['image_url'], 'https://example.com/images/workshop-ad.jpg')
        self.assertEqual(data['ads'][1]['ad_url'], 'https://example.com/workshop')
        self.assertEqual(data['ads'][2]['title'], 'Plant Pot Collection')
        self.assertEqual(data['ads'][2]['description'], 'Explore our new collection of stylish plant pots.')
        self.assertEqual(data['ads'][2]['image_url'], 'https://example.com/images/pot-ad.jpg')
        self.assertEqual(data['ads'][2]['ad_url'], 'https://example.com/pots')

    @patch('app.db_cursor')
    def no_ads_fetched(self, mock_db_cursor):
        mock_db_cursor.execute.return_value = None
        mock_db_cursor.fetchall.return_value = []

        with self.assertRaises(AdsNotFetchedException) as context:
            self.app.get('/ads')

        self.assertEqual(context.exception.message, "No ads were fetched successfully.")
        self.assertEqual(context.exception.status_code, 404)


if __name__ == '__main__':
    unittest.main()


class VideoRatingTestCase(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    @mock.patch('app.db_cursor')
    def test_rate_video_success(self, mock_db_cursor):
        mock_db_cursor.execute.return_value = None
        mock_db_cursor.fetchall.return_value = None
        video_id = 10
        rating = 4
        comment = 'This was a great video!'

        with app.test_client() as client:
            response = client.post(f'/videos/{video_id}/rate',
                                   json={'rating': rating, 'comment': comment})

            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data['message'], 'Rating and comment submitted successfully.')

    @mock.patch('app.db_cursor')
    def test_rate_video_missing_inputs(self, mock_db_cursor):
        mock_db_cursor.execute.return_value = None
        mock_db_cursor.fetchall.return_value = None
        video_id = 10
        rating = 4

        with app.test_client() as client:
            response = client.post(f'/videos/{video_id}/rate',
                                   json={'rating': rating})

            self.assertEqual(response.status_code, 400)
            data = json.loads(response.data)
            self.assertEqual(data['error'], 'Missing rating or comment.')


if __name__ == '__main__':
    unittest.main()
